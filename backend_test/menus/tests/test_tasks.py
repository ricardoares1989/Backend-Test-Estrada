import datetime

import pytest
from django.template.loader import render_to_string

from backend_test.menus.models import Menu
from backend_test.menus.tasks import close_menu, send_menu
from backend_test.menus.utils import slack_notifier
from backend_test.settings import SLACK_HOOK_CHANNELS as slack_channels

pytestmark = pytest.mark.django_db


def test_slack_notifier():
    """
    Given a destiny.
    When you need to send a special notification to slack
    Then send the template with http request.
    """
    slack_test_notification = render_to_string("slack_test_notification.json")
    destiny = slack_channels["ch"]
    assert slack_notifier(slack_message=slack_test_notification, destiny=destiny) == 200


def test_send_menu_for_country(menu_with_meals):
    """
    Given a menu with its meals.
    When you finish the meals capture.
    Then send a slack notification with the Menu depends
    of the Country.
    Args:
        menu_with_meals(Menu): Menu instance with meals.
    """
    slack_menu_notification = "slack_menu_notification.json"
    assert (
        send_menu.run(
            menu=menu_with_meals,
            template=slack_menu_notification,
            notifier=slack_notifier,
            destiny=slack_channels["ch"],
        )
        == 200
    )


def test_close_menu_task():
    """
    When creates a Menu, You need to close the menu
    at the 11:00 am.
    Then close_menu task close the menus.
    """
    menu = Menu.objects.create(date=datetime.datetime.now().date())
    assert close_menu.run()
    assert Menu.objects.get(id=menu.id).closed
