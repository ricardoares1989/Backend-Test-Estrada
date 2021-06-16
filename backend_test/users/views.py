from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from .forms import UserCreationForm, LoginForm


class SignupUser(CreateView):
    """
    Form View with the userCreationForm for signup
    to the application.
    """

    template_name = "users/signup.html"
    form_class = UserCreationForm
    success_url = "/users/login/"


user_signup_view = SignupUser.as_view()


class LoginUserView(LoginView):
    success_url = '/'
    next = '/'
    template_name = "registration/login.html"


user_login_view = LoginUserView.as_view()