import pytest

from backend_test.requests.models import Request

pytestmark = pytest.mark.django_db


def test_request_creation(menu, option, user):
    """
    Given a menu, option and user.
    When you request a option of meal associated to a Menu
    Then create a Request.
    Args:
        menu (Menu): Instance of Menu model.
        option (Option): Instance of Option model
        user (CustomUser): Instance of CustomUser model
    """
    request = Request.objects.create(user=user, option=option)
    assert request.option.menu == menu
    assert not (request.customization)
    assert str(request) == f"{user.email} - {option.meal.name}"
