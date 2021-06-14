import pytest

from backend_test.users.models import Profile

pytestmark = pytest.mark.django_db


def test_user_creation(user_model, user_data):
    user = user_model.objects.create_user(
        email=user_data.email, password=user_data.password
    )
    assert user.email == user_data.email
    assert user.created_at.date() == user.updated_at.date()


def test_create_profile(user):
    profile = Profile.objects.create(user=user, country=Profile.Countries.CHILE)
    assert profile.user == user
    assert profile.country == Profile.Countries.CHILE


def test_superuser_creation(user_model, user_data):
    user = user_model.objects.create_superuser(
        email=user_data.email, password=user_data.password
    )
    assert user.is_staff
    assert user.is_superuser
    assert user.is_active


def test_superuser_isnt_superuser(user_model, user_data):
    """test for raise a Exception when a user is not superuser"""
    with pytest.raises(ValueError):
        user_model.objects.create_superuser(
            email=user_data.email, password=user_data.password, is_superuser=False
        )


def test_superuser_isnt_staff(user_model, user_data):
    """test for raise a Exception when a user is not superuser"""
    with pytest.raises(ValueError):
        user_model.objects.create_superuser(
            email=user_data.email, password=user_data.password, is_staff=False
        )
