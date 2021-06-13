import secrets
import string
from collections import namedtuple

import pytest

pytestmark = pytest.mark.django_db

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


@pytest.mark.parametrize(
    "user_data", [UserData("name@gmail.com", password_generator())]
)
def test_user_creation(user_model, user_data):
    user = user_model.objects.create_user(
        email=user_data.email, password=user_data.password
    )
    assert user.email == user_data.email
