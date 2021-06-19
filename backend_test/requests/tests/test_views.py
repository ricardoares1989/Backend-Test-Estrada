import pytest
from django.test import Client
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_creation_view_fail(user, user_data, option):
    """
    Given a user that want to register his option of menu.
    When you try to create the request,
    Then get a 200 satus code.
    """
    client = Client()
    login = client.login(
        username=user.email,
        password=user_data.password,
    )
    assert login
    response = client.get(
        reverse("requests:create_request"),
        content_type="application/x-www-form-urlencoded",
    )
    assert response.status_code == 200
