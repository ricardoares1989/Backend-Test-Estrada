from django.db import models

from backend_test.utils.timestamped_model import TimeStampedModel


class Request(TimeStampedModel):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    option = models.ForeignKey("menus.Options", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} - {self.option.meal.name}"
