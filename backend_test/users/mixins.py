from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


class LoginSuperUserMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    This mixin validate the superuser quality of a user, and require the login.
    """

    login_url = reverse_lazy("users:login")
    permission_denied_message = "Please you need superuser attribute"

    def test_func(self):
        return self.request.user.is_superuser
