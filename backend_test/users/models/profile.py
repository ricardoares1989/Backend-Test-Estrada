from django.db import models

from backend_test.utils.timestamped_model import TimeStampedModel


class Profile(TimeStampedModel):
    """
    Model to contain all the data that can change in a user.
    """

    class Countries(models.TextChoices):
        MEXICO = "mx", "Mexico"
        BRAZIL = "br", "Brazil"
        CANADA = "cn", "Canada"
        CHILE = "ch", "Chile"
        COLOMBIA = "co", "Colombia"
        USA = "us", "USA"
        PERU = "pr", "Peru"

    user = models.OneToOneField("users.CustomUser", on_delete=models.CASCADE)
    country = models.CharField(max_length=2, choices=Countries.choices)

    def __str__(self):
        return f"{self.user} Profile"
