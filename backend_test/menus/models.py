import uuid

from django.db import models
from django.urls import reverse
from django.utils import timezone

from backend_test.utils.timestamped_model import TimeStampedModel


class Menu(TimeStampedModel):
    """
    Model for create a specific Menu for a specific Date.
    The date field must be unique.
    The meals object has a M2M relationship with Meals options, through
    Options Objects.
    Args:
        id(UUID): UUID identifier.
        date(datetime.date): Specific date for the Menu.
        meals(List(Meal)): Meals for the Menu.

    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(unique=True)
    meals = models.ManyToManyField(
        "menus.Meal", through="Options", through_fields=("menu", "meal")
    )
    closed = models.BooleanField(default=False)

    @property
    def absolute_url(self):
        return reverse("menus:detail", kwargs={"pk": self.id})

    def get_list_meals(self):
        return list(self.meals.all().values("name", "description"))

    @classmethod
    def new_menus(cls):
        return cls.objects.filter(date__gte=timezone.now().date())

    def __str__(self):
        return f"Menu for - {self.date}"


class Meal(TimeStampedModel):
    """
    Meal model with a name and description Attribute.
    Args:
        name(str): This field must be unique.
        description: Description of the meal.
    """

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"Meal - {self.name}"

    class Meta:
        ordering = ("id",)


class Options(TimeStampedModel):
    """
    Options are objects that contain the relationship
    between menu and the meals. There are many meals for a menu,
    and many menus with a meal.
    Args:
        menu(Menu): instance of Menu.
        meal(Meal): instance of Meal
    """

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Menu {self.menu.date} - {self.meal.name}"
