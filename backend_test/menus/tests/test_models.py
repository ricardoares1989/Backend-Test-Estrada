from uuid import UUID

import pytest

from backend_test.menus.models import Meal, Menu, Options

pytestmark = pytest.mark.django_db


def test_create_menu(date):
    """
    Given a specific date.
    When you create a menu with that date.
    Then the menu is open to edit,
    and has a UUID as identifier.
    Args:
        date (datetime.date)

    """
    menu = Menu.objects.create(date=date)
    assert menu.date == date
    assert not menu.closed
    assert str(menu) == f"Menu for - {menu.date}"
    assert isinstance(menu.id, UUID)


def test_create_meal(meals):
    """
    Given a list of Meals.
    When you create the meals.
    Then you need to ensure all will be created.
    Args:
        meals (List(Meal)): Meal instances
    """
    meals = Meal.objects.bulk_create([Meal(**option) for option in meals])
    all_meals = Meal.objects.all()
    assert len(all_meals) == len(meals)


def test_create_options(menu, meals_instances):
    """
    Args:
        menu (Menu.): Menu instance
        meals_instances (List(Meal)): Meal instances
    """
    menu.meals.add(*meals_instances)
    assert list(menu.meals.all()) == meals_instances
    assert isinstance(menu.options_set.first(), Options)


def test_options_ids_per_user(menu_with_meals, user):
    """
    Given a user you and a menu with meals.
    When you associate a option, with a request and a user.
    Then you can't add another request for the same menu.
    """
    from backend_test.requests.models import Request

    Request.objects.create(user=user, option=menu_with_meals.options_set.first())
    assert len(Options.exclude_options_and_menus_per_user(user)) == 0
