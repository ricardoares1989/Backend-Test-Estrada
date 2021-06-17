import pytest

from backend_test.users.forms import ProfileCreationForm, UserCreateForm
from backend_test.users.models import CustomUser

pytestmark = pytest.mark.django_db


class TestCreationForm:
    """Test class for creation form"""

    def test_create_user(self, user_data):
        """
        Given a email and password
        When you enter the information in the UserCreationForm
        then validate the form and retrieve a user instance.
        Args:
            user_data (NamedTuple(email, password)): NamedTuple with
            email and password.

        """
        form = UserCreateForm(
            {
                "username": user_data.email,
                "email": user_data.email,
                "password1": user_data.password,
                "password2": user_data.password,
            }
        )
        assert form.is_valid()
        form.save()
        user = CustomUser.objects.get(email=user_data.email)
        assert user.email == user_data.email

    def test_create_profile(self, user):
        """
        Given a CustomUser
        When you register your country in the ProfileCreationForm
        Then retrieve a profile object and gives the attribute profile
        to user.
        Args:
            user (CustomUser): Instance of CustomUser
        """
        form = ProfileCreationForm({"user": user, "country": "ch"})
        profile = form.save()
        assert form.is_valid()
        assert user.profile == profile
        assert user.profile.country == profile.country
