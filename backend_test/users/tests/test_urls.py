import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_signup_url():
    """
    Resolve and get the url and a view for signup.
    """
    assert reverse("users:signup") == "/users/signup/"
    assert resolve("/users/signup/").view_name == "users:signup"


def test_login_url():
    """
    Resolve and get the url for login.
    """
    assert reverse("users:login") == "/users/login/"
    assert resolve("/users/login/").view_name == "users:login"


def test_logout_url():
    """
    Resolve and get the url for logout.
    """
    assert reverse("users:logout") == "/users/logout/"
    assert resolve("/users/logout/").view_name == "users:logout"
