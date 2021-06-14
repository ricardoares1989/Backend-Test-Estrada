import uuid

from django.db import models

from backend_test.utils.timestamped_model import TimeStampedModel


class Menu(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(unique=True)
    meals = models.ManyToManyField(
        "menus.Meal", through="Options", through_fields=("menu", "meal")
    )
    closed = models.BooleanField(default=False)

    def __str__(self):
        return f"Menu for - {self.date}"


class Meal(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"Meal - {self.name}"

    class Meta:
        ordering = ("id",)


class Options(TimeStampedModel):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Menu {self.menu.date} - {self.meal.name}"
