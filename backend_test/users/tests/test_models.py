import pytest

pytestmark = pytest.mark.django_db


def test_user_creation(user_model, user_data):
    user = user_model.objects.create_user(
        email=user_data.email, password=user_data.password
    )
    assert user.email == user_data.email
    assert user.created_at.date() == user.updated_at.date()
