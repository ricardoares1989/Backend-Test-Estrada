from django.views.generic import FormView

from .forms import UserCreationForm


class SignupUser(FormView):
    template_name = "users/signup.html"
    form_class = UserCreationForm
    success_url = "/"


user_signup_view = SignupUser.as_view()
