from django import forms
from django.conf import settings
from django.forms import ModelForm
from django.utils import timezone

from backend_test.menus.models import Meal, Menu, Options
from backend_test.menus.tasks import send_menu
from backend_test.menus.utils import menu_parser


class MealCreationForm(ModelForm):
    """
    Form to create a Meal Object.
     Args:
         name (str): meal name
         description (str): meal description
    """

    class Meta:
        model = Meal
        fields = ("name", "description")


class OptionsCreateForm(ModelForm):
    """
    Form to create a Meal Object.
     Args:
         menu (id): Send the menu id
         meal (id): Send the meal id
    """

    menu = forms.ModelChoiceField(queryset=Menu.new_menus())

    class Meta:
        model = Options
        fields = ("menu", "meal")


class MenuCreateForm(ModelForm):
    """
    Form to create a Meal Object.
     Args:
         date
         meals
    """

    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Menu
        fields = ("date", "meals")

    def clean_date(self):
        """Validate if the date its greater than the current date"""
        date = self.cleaned_data["date"]
        if timezone.now().date() > date:
            raise forms.ValidationError("You can't create a menu for a past date.")
        return date

    def save(self, commit=True):
        """Send the menu in the form saving."""
        menu = super(MenuCreateForm, self).save()
        template = menu_parser(menu=menu, template="slack_menu_notification.json")
        send_menu.delay(
            destiny=settings.SLACK_HOOK_CHANNELS["ch"],
            template=template,
        )
        return menu
