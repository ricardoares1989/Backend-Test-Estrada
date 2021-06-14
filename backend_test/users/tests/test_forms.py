import pytest

from backend_test.users.forms import ProfileCreationForm, UserCreationForm

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
        form = UserCreationForm(
            {
                "email": user_data.email,
                "password": user_data.password,
                "password2": user_data.password,
            }
        )
        user = form.save()
        assert form.is_valid()
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
