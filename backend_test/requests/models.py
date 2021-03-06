from django.db import models
from django.utils import timezone

from backend_test.utils.timestamped_model import TimeStampedModel


class Request(TimeStampedModel):
    """
    Request object is the selection of a Meal option for the user.
    Args:
        user(CustomUser): Instance of CustomUser.
        option(Options): Instance of options, the object have
            the menu related and the meal.
        customization(str): Set specification about the meal.
    """

    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    option = models.ForeignKey("menus.Options", on_delete=models.CASCADE)
    customization = models.CharField(max_length=50, null=True, blank=True)

    @classmethod
    def today_requests(cls, date=timezone.now().date()):
        return cls.objects.filter(option__menu__date__exact=date)

    def __str__(self):
        return f"{self.user.email} - {self.option.meal.name}"
