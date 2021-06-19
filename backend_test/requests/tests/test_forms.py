from unittest.mock import Mock

import pytest

from backend_test.requests.forms import RequestCreateForm
from backend_test.requests.models import Request

pytestmark = pytest.mark.django_db


def test_meal_creation_form(user, option):
    """
    Given a meal data
    when you fill the MealCreationForm
    Then you obtain a Meal object.
    """
    mock_request = Mock()
    attr = {"user": user}
    mock_request.configure_mock(**attr)
    form = RequestCreateForm(
        mock_request, {"user": user, "option": option, "customization": "Without Sauce"}
    )
    assert form.is_valid()
    form.save()
    assert Request.objects.get(user=form["user"].value(), option=form["option"].value())
