from datetime import timedelta

import pytest
from django.utils import timezone

from backend_test.menus.forms import MealCreationForm, MenuCreateForm, OptionsCreateForm
from backend_test.menus.models import Meal, Menu, Options

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
    """
    Given a menu id and meals instances id
    When you try to pass through the OptionsCreateForm
    Then you can create the Option instance.
    """
    form = OptionsCreateForm({"menu": menu.id, "meal": meals_instances[0].id})
    assert form.is_valid()
    form.save()
    assert Options.objects.get(
        menu__pk=form["menu"].value(), meal__pk=form["meal"].value()
    )


def test_menu_create_form(meals_instances, date):
    """
    Given a menu id and meals instances id
    When you try to pass through the MenuCreateForm
    Then you can create the menu instance.
    """
    meals_pk = [meals_instances[i].id for i in range(len(meals_instances))]
    form = MenuCreateForm(
        {
            "date": date,
            "meals": meals_pk,
        }
    )
    assert form.is_valid()
    form.save()
    assert Menu.objects.get(date__exact=form["date"].value())
    assert len(Options.objects.filter(meal__pk__in=meals_pk)) == len(meals_instances)


def test_menu_create_form_invalid(meals_instances, date):
    """
    Given a menu id and meals instances id
    When you try to pass through the MenuCreateForm
    Then you can create the menu instance.
    """
    meals_pk = [meals_instances[i].id for i in range(len(meals_instances))]
    form = MenuCreateForm(
        {
            "date": (timezone.now() - timedelta(days=1)).date(),
            "meals": meals_pk,
        }
    )
    assert not (form.is_valid())
