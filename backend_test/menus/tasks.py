from typing import Any, Callable

from celery import shared_task
from django.template.loader import render_to_string

from backend_test.menus.models import Menu


@shared_task
def send_menu(
    menu: Menu, template: str, notifier: Callable[[Any, Any], Any], destiny: str
):
    """
    Task to send the menu to destiny, the notifier
    is a callable, with the special logic for each destiny

    """
    menu_url = menu.absolute_url
    menu_meals = menu.get_list_meals()
    menu_date = menu.date
    template = render_to_string(
        template,
        {"menu_date": menu_date, "menu_url": menu_url, "menu_meals": menu_meals},
    )
    return notifier(template, destiny)
