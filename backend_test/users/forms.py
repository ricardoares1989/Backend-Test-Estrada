from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Profile


class UserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "username")


class ProfileCreationForm(forms.ModelForm):
    """
    Form to create a Profile object associated with a CustomUser instance.
    Args:
        user (CustomUser): CustomUser Instance.
        country (Choices): CustomUser.Countries
    """

    class Meta:
        model = Profile
        fields = ("user", "country")
