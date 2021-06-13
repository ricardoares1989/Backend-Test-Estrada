from django.contrib.auth.models import AbstractUser
from django.db import models

from backend_test.users.managers import CustomUserManager
from backend_test.utils.timestamped_model import TimeStampedModel


class CustomUser(AbstractUser, TimeStampedModel):
    username = None
    email = models.EmailField(
        "email address",
        unique=True,
        error_messages={"unique": "A user with that email already exists."},
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email