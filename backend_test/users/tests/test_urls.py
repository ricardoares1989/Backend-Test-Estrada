import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_signup_url():
    """
    Resolve and get the url and a view for paths.
    """
    assert reverse("users:signup") == "/users/signup/"
    assert resolve("/users/signup/").view_name == "users:signup"
