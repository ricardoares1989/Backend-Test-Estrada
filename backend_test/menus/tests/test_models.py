from uuid import UUID

import pytest

from backend_test.menus.models import Meal, Menu, Options

pytestmark = pytest.mark.django_db


def test_create_menu(date):
    menu = Menu.objects.create(date=date)
    assert menu.date == date
    assert not menu.closed
    assert str(menu) == f"Menu for - {menu.date}"
    assert isinstance(menu.id, UUID)


def test_create_option(meals):
    meals = Meal.objects.bulk_create([Meal(**option) for option in meals])
    all_meals = Meal.objects.all()
    assert len(all_meals) == len(meals)


def test_create_options(menu, meals_instances):
    option = Options.objects.create(menu=menu)
    option.meals.add(*meals_instances)
    assert list(option.meals.all()) == meals_instances
    assert option.menu == menu
    assert str(option) == f"Menu {option.menu.date} - option {option.id}"
