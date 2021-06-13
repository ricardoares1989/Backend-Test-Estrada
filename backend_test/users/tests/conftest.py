import secrets
import string
from collections import namedtuple

import pytest
from django.contrib.auth import get_user_model


@pytest.fixture(scope="module")
def user_model():
    return get_user_model()


UserData = namedtuple("UserData", "email password")


def password_generator():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = "".join(secrets.choice(alphabet) for i in range(10))
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3
        ):
            break
    return password


@pytest.fixture(scope="module")
def user_data():
    return UserData("name@gmail.com", password_generator())
