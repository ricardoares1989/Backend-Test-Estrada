from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from backend_test.requests.forms import RequestCreateForm
from backend_test.requests.models import Request


class RequestCreateView(LoginRequiredMixin, CreateView):
    template_name = "create_request.html"
    form_class = RequestCreateForm
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("users:login")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


create_request_view = RequestCreateView.as_view()


class RequestListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "list_requests.html"
    login_url = reverse_lazy("users:login")
    permission_denied_message = "Please you need superuser attribute"
    queryset = Request.today_requests()
    context_object_name = "requests"

    def test_func(self):
        return self.request.user.is_superuser


request_list_view = RequestListView.as_view()
