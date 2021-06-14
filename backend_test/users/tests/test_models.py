import pytest

from backend_test.users.models import Profile

pytestmark = pytest.mark.django_db


def test_user_creation(user_model, user_data):
    """
    Given email and password,
    When you want to create a user.
    Then you need to define and email and password.
    Args:
        user_model (CustomUser): Get the CustomUser model, for the application.
        user_data (NamedTuple(email, password)): NamedTuple with the emails,
            and password for the user.
    """
    user = user_model.objects.create_user(
        email=user_data.email, password=user_data.password
    )
    assert user.email == user_data.email
    assert user.created_at.date() == user.updated_at.date()


def test_create_profile(user):
    """
    Given a User.
    When you need to set your residence country.
    Then you need to create a profile.
    Args:
        user (CustomUser): A instance of CustomUser
    """
    profile = Profile.objects.create(user=user, country=Profile.Countries.CHILE)
    assert profile.user == user
    assert profile.country == Profile.Countries.CHILE


def test_superuser_creation(user_model, user_data):
    """
    Given a email and password.
    When you need to create a superuser
    Then you need to set the attributes is_staff
        is_superuser, is_active

    Args:
        user_model (CustomUser): CustomUser model.
        user_data (NamedTuple(email, password)):  Data
            for the authentication.
    """
    user = user_model.objects.create_superuser(
        email=user_data.email, password=user_data.password
    )
    assert user.is_staff
    assert user.is_superuser
    assert user.is_active


def test_superuser_isnt_superuser(user_model, user_data):
    """
    Given a email and password.
    When you try to create a superuser without is_superuser
    attribute.
    Then rise a ValueError Exception.
    Args:
        user_model (CustomUser)
        user_data (NamedTuple(email, password)):
    """
    with pytest.raises(ValueError):
        user_model.objects.create_superuser(
            email=user_data.email, password=user_data.password, is_superuser=False
        )


def test_superuser_isnt_staff(user_model, user_data):
    """
    Given a email and password.
    When you try to create a superuser without is_staff
    attribute.
    Then rise a ValueError Exception.
    Args:
        user_model (CustomUser)
        user_data (NamedTuple(email, password)):
    """
    with pytest.raises(ValueError):
        user_model.objects.create_superuser(
            email=user_data.email, password=user_data.password, is_staff=False
        )
