import pytest
from django.contrib.auth import get_user_model


@pytest.fixture(scope="module")
def user_model():
    return get_user_model()
