from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from backend_test.requests.forms import RequestCreateForm


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
