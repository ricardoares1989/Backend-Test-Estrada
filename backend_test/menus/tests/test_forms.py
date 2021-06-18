import pytest

from backend_test.menus.forms import MealCreationForm, OptionsCreateForm
from backend_test.menus.models import Meal, Options

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


def test_option_create_form(meals_instances, menu):
    form = OptionsCreateForm({"menu": menu.id, "meal": meals_instances[0].id})
    assert form.is_valid()
    form.save()
    assert Options.objects.get(
        menu__pk=form["menu"].value(), meal__pk=form["meal"].value()
    )
