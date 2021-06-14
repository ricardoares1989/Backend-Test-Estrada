import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_signup_url():
    assert reverse("users:signup") == "/users/signup/"
    assert resolve("/users/signup/").view_name == "users:signup"
