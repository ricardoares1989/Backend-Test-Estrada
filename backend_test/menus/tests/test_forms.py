import pytest

from backend_test.menus.forms import MealCreationForm
from backend_test.menus.models import Meal

pytestmark = pytest.mark.django_db


def test_meal_creation_form(meals):
    """
    Given a meal data
    when you fill the MealCreationForm
    Then you obtain a Meal object.
    """
    form = MealCreationForm(
        {"name": meals[0]["name"], "description": meals[0]["description"]}
    )
    assert form.is_valid()
    form.save()
    assert Meal.objects.get(name=form["name"].value())
