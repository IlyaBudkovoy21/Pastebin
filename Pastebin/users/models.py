import uuid
from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    username = models.CharField(
        primary_key=False,
        max_length=150
    )

    email = models.EmailField(
        primary_key=False,
        max_length=100,
        unique=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
