import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_menu_detail_url(menu):
    """
    Resolve and get the url for login.
    """
    assert reverse("menus:detail", kwargs={"pk": menu.id}) == f"/menus/{menu.id}/"
    assert resolve("/menus/{menu.id}/").view_name == "menus:detail"
