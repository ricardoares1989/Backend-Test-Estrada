from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from backend_test.requests.forms import RequestCreateForm
from backend_test.requests.models import Request
from backend_test.users.mixins import LoginSuperUserMixin


class RequestCreateView(LoginRequiredMixin, CreateView):
    """
    This view is to create a Request, but only if the user is login.
    """

    template_name = "create_request.html"
    form_class = RequestCreateForm
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("users:login")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


create_request_view = RequestCreateView.as_view()


class RequestListView(LoginSuperUserMixin, ListView):
    """
    This View is to see all the request that the users sends,
    only the super user can see it, in the current day.
    """

    template_name = "list_requests.html"
    queryset = Request.today_requests()
    context_object_name = "requests"


request_list_view = RequestListView.as_view()
