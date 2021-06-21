from django.template.loader import render_to_string

import urllib3

from backend_test.menus.models import Menu

http = urllib3.PoolManager()


def menu_parser(menu: Menu, template: str):
    """
    This function is for create a menu template, for send the notification.
    The template it's any string format, like json, html, etc., and
    use the django template engine and django template language to inject
    the menu inside the template.
    Args:
        menu (Menu)
        template (str)
    """
    menu_url = menu.absolute_url
    menu_meals = menu.get_list_meals()
    menu_date = menu.date
    return render_to_string(
        template,
        {"menu_date": menu_date, "menu_url": menu_url, "menu_meals": menu_meals},
    )


def slack_notifier(slack_message: str, destiny: str) -> int:
    """
    Args:
        slack_template (str)): Enter a JSON string
        destiny (str): Url path to channel.
    Returns:
        status_code (int)
    """

    request = http.request(
        "POST",
        destiny,
        body=slack_message,
        headers={"Content-type": "application/json"},
    )
    return request.status
