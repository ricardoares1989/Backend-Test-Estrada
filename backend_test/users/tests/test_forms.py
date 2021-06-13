import pytest

from backend_test.users.forms import UserCreationForm

pytestmark = pytest.mark.django_db


class TestCreationForm:
    """Test class for creation form"""

    def test_create_user(self, user_data):
        """
        Test the UserCreationForm
        Args:
            user_data (UserData): NamedTuple with email
                and password.

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
