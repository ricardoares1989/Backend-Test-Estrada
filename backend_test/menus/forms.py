from django import forms
from django.forms import ModelForm

from backend_test.menus.models import Meal, Menu, Options


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
    menu = forms.ModelChoiceField(queryset=Menu.new_menus())

    class Meta:
        model = Options
        fields = ("menu", "meal")
