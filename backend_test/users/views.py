from django.views.generic import CreateView

from .forms import UserCreateForm


class SignupUserView(CreateView):
    """
    Form View with the userCreationForm for signup
    to the application.
    """

    template_name = "users/signup.html"
    form_class = UserCreateForm
    success_url = "/users/login/"


user_signup_view = SignupUserView.as_view()
