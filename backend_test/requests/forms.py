from django import forms

from backend_test.menus.models import Options
from backend_test.requests.models import Request
from backend_test.users.models import CustomUser


class RequestCreateForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ("user", "option", "customization")

    def __init__(self, request, *args, **kwargs):
        """
        Insert the request in the form, with propose of extract the user,
        that sends the request.
        """
        self.request = request
        super().__init__(*args, **kwargs)
        self.fields["user"].queryset = CustomUser.objects.filter(
            username=self.request.user.username
        )
        self.fields["option"].queryset = Options.exclude_options_and_menus_per_user(
            self.request.user
        )
