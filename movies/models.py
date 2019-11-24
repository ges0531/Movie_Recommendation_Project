from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

class Genre(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    popularity = models.IntegerField()
    poster_url = models.CharField(max_length=100)
    runtime = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(User, related_name='like_movies')
    def get_absolute_url(self):
        return reverse("movies:movie_detail", kwargs={"movie_id": self.pk})




class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    rate = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Date(models.Model):
    release_date = models.DateField()