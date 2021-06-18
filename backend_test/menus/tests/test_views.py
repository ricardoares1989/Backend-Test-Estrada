import pytest
from django.test import Client, RequestFactory
from django.urls import reverse_lazy

from backend_test.menus.views import MenuDetailView

pytestmark = pytest.mark.django_db


class TestMenuDetailView:
    def test_detail_view(self, menu, rf: RequestFactory):
        request = rf.get(f"menus/{menu.id}")
        view = MenuDetailView()
        view.setup(request, pk=f"{menu.id}")
        assert view.get_object() == menu


class TestMealCreationView:
    def test_creation_view(self, meals, superuser, user_data):
        """
        Given a meal, and a superuser
        When you try to create the meal as a superuser,
        Then get a 200 in the creation of meal.
        """
        client = Client()
        login = client.login(
            username=superuser.email,
            password=user_data.password,
        )
        assert login
        response = client.post(
            reverse_lazy("menus:create_meal"),
            data={"name": meals[0]["name"], "description": meals[0]["description"]},
            content_type="application/x-www-form-urlencoded",
        )
        assert response.status_code == 200

    def test_creation_view_fail(self, meals, user, user_data):
        """
        Given a meal, and a superuser
        When you try to create the meal as a superuser,
        Then get a 200 in the creation of meal.
        """
        client = Client()
        login = client.login(
            username=user.email,
            password=user_data.password,
        )
        assert login
        response = client.post(
            reverse_lazy("menus:create_meal"),
            data={"name": meals[0]["name"], "description": meals[0]["description"]},
            content_type="application/x-www-form-urlencoded",
        )
        assert response.status_code == 403
