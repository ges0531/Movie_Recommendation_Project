from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

class Genre(models.Model):
    # genre_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100, blank=True)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    popularity = models.FloatField(null=True)
    poster_url = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre, related_name='movie_genre')
    like_users = models.ManyToManyField(User, related_name='like_movies')
    def get_absolute_url(self):
        return reverse("movies:movie_detail", kwargs={"movie_id": self.pk})

    # @classmethod
    # def import_data(cls):
    #     with open('./movies/fixtures/movie.json', 'r', encoding='utf-8') as f:
    #         movies = json.load(f)
    #         for movie in movies:
    #             genres_in_movie = movie['fields']
    #             m = cls.objects.create(                    
    #                 title = movie['title'],
    #                 overview = movie['overview'],
    #                 popularity = movie['popularity'],
    #                 poster_url = movie['poster_path'],
    #                 release_date = movie['release_date'],
    #                 genre = movie['genre_ids']
    #                 # genres = ','.join(gl)
    #                 # watch_grade = movie['audits'],
    #             )
    #             for genre_1 in genres_in_movie:
    #                 g = Genre.objects.get(gnere_id=genre_1)
    #                 m.genre_1.add(g)



class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    rate = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


