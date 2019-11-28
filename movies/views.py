from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReviewModelForm, GenreModelForm, MovieModelForm
from .models import Review, Genre, Movie
from django.core import serializers
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.
# Movie.genre.name

@login_required
def movie_list(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    # paginator = Paginator(Movie.objects.all(), 20)
    # movies = paginator.get_page(request.GET.get('page') or 1)
    movies = serializers.serialize('json', movies, fields=('title', 'poster_url', 'release_date','genre', ))
    genres = serializers.serialize('json', genres, fields=('name', ))
    return render(request, 'movies/movie_list.html', {
        'movies': movies,
        'genres': genres,
    })

@login_required
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    genres = movie.genre.all()
    reviews = movie.review_set.all()
    form = ReviewModelForm()
    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'genres': genres,
        'reviews': reviews,
        'form': form,
    })

@login_required
def create_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    form = ReviewModelForm(request.POST)
    review = Review()
    review.content = request.POST.get('input_content')
    review.rate = request.POST.get('input_rate')
    review.movie_id = movie.id
    review.user = request.user
    if review.rate and review.content:
        review.save()
    return redirect(movie)



@login_required
def delete_review(request, review_id, movie_id):
    review = get_object_or_404(Review, id=review_id, movie_id=movie_id)
    review.delete()
    return redirect(review.movie)

@login_required
def movie_like(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    user = request.user
    if user in movie.like_users.all():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)
    return redirect(movie)


def page_title(request):
    return render(request, 'movies/page_title.html')

def prac(request):
    return render(request, 'movies/prac.html')


# 시대와 장르를 이용한 추천 알고리즘 함수 만들기
# 로그인 됐을때만 추천해주도록 만들기
