from datetime import timedelta

import pytest
from django.utils import timezone

from backend_test.menus.models import Meal, Menu


@pytest.fixture()
def date():
    delta = timedelta(days=1)
    return (timezone.now() + delta).date()


@pytest.fixture()
def meals():
    return [
        {"name": f"meal {meal}", "description": f"Option meal {meal}"}
        for meal in range(10)
    ]


@pytest.fixture()
def meals_instances(meals):
    return Meal.objects.bulk_create([Meal(**option) for option in meals])


@pytest.fixture()
def menu(date):
    return Menu.objects.create(date=date)
