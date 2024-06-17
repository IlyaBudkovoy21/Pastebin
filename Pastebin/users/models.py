import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
