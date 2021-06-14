import pytest

from backend_test.requests.models import Request

pytestmark = pytest.mark.django_db


def test_request_creation(menu, option, user):
    request = Request.objects.create(user=user, option=option)
    assert request.option.menu == menu
