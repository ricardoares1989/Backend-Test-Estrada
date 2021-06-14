import pytest
from django.utils import timezone

from backend_test.menus.models import Meal, Menu
from backend_test.users.tests.conftest import user, user_data, user_model


@pytest.fixture()
def menu():
    date = timezone.now().date()
    return Menu.objects.create(date=date)


@pytest.fixture()
def meals():
    return Meal.objects.bulk_create(
        [Meal(name=f"comida {id}", description=f"descr {id}") for id in range(10)]
    )


@pytest.fixture()
def option(meals, menu):
    menu.meals.add(*meals)
    return menu.options_set.first()
