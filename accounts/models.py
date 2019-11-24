from django.db import models
from django.urls import reverse
# User 는 AbstractUser를 상속받고, 얘는 AbstractBaseUser를 상속받음. ctrl+click하면 확인 가능
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from faker import Faker



class User(AbstractUser):
    fans = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='stars')

    def __str__(self):
        return self.username

    
    def get_absolute_url(self):
        return reverse("accounts:user_page", kwargs={"user_id": self.pk})
