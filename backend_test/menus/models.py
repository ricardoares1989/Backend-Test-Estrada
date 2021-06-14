from django.db import models

from backend_test.utils.timestamped_model import TimeStampedModel


class Menu(TimeStampedModel):
    date = models.DateField(unique=True)

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
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
    )
    meals = models.ManyToManyField(Meal)

    def __str__(self):
        return f"Menu {self.menu.date} - option {self.id}"
