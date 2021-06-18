import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_menu_detail_url(menu):
    """
    Resolve and get the url for menu detail.
    """
    assert reverse("menus:detail", kwargs={"pk": menu.id}) == f"/menus/{menu.id}/"
    assert resolve("/menus/{menu.id}/").view_name == "menus:detail"


def test_create_meal_url():
    """
    Resolve and get the url for create a meal.
    """
    assert reverse("menus:create_meal") == "/menus/meals/"
    assert resolve("/menus/meals/").view_name == "menus:create_meal"


def test_create_options_url():
    """
    Resolve and get the url for create options.
    """
    assert reverse("menus:create_options") == "/menus/options/"
    assert resolve("/menus/options/").view_name == "menus:create_options"
