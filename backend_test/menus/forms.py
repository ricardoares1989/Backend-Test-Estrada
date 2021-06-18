from django.forms import ModelForm

from backend_test.menus.models import Meal


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
