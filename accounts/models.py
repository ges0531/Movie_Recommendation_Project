from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings


class User(AbstractUser):
    fans = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='stars')

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse("accounts:user_detail", kwargs={"user_id": self.pk})
    