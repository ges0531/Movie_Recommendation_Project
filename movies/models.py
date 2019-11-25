from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

class Genre(models.Model):
    genre_id = models.IntegerField(null=True)
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


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    rate = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


