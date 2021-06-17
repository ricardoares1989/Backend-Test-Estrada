import pytest
from django.test import Client, RequestFactory
from django.urls import reverse_lazy

from backend_test.users.views import SignupUserView

pytestmark = pytest.mark.django_db


class TestUserCreation:
    def test_get_success_url(self, rf: RequestFactory):
        view = SignupUserView()
        request = rf.get("/generic_url/")
        view.request = request

        assert view.success_url == "/users/login/"

    def test_signup_view(self, user_data, client: Client):
        """
        Given a user data,
        When you send the request in the form.
        Then you obtain a 200 status code.
        """
        response = client.post(
            reverse_lazy("users:signup"),
            {
                "username": user_data.email,
                "email": user_data.email,
                "password1": user_data.password,
                "password2": user_data.password,
            },
            content_type="application/x-www-form-urlencoded",
        )
        assert response.status_code == 200
