from django.contrib.auth.models import AbstractUser
from django.db import models

from backend_test.users.managers import CustomUserManager
from backend_test.utils.timestamped_model import TimeStampedModel


class CustomUser(AbstractUser, TimeStampedModel):
    """
    CustomUser without username, only receive email and password.
    Args:
        email(str): String with email pattern.
        password(str):
    """

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
