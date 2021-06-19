from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from backend_test.menus.forms import MealCreationForm, MenuCreateForm, OptionsCreateForm
from backend_test.menus.models import Menu


class MenuListView(ListView):
    queryset = Menu.objects.all().order_by("date")
    context_object_name = "menus"
    template_name = "all_menus.html"


menu_all_view = MenuListView.as_view()


class MenuDetailView(DetailView):
    """
    View for retrieve a detail of menus of the day or new_menus.
    """

    queryset = Menu.new_menus()
    template_name = "menu_detail_view.html"
    context_object_name = "menu"


menu_detail_view = MenuDetailView.as_view()


class MenuCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    View for create a menu.
    """

    success_url = reverse_lazy("menus:create_menu")
    template_name = "create_menu.html"
    form_class = MenuCreateForm
    login_url = reverse_lazy("users:login")
    permission_denied_message = "Please you need superuser attribute"

    def test_func(self):
        return self.request.user.is_superuser


menu_create_view = MenuCreateView.as_view()


class MealCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    success_url = reverse_lazy("menus:create_meal")
    template_name = "create_meals.html"
    form_class = MealCreationForm
    login_url = reverse_lazy("users:login")
    permission_denied_message = "Please you need superuser attribute"

    def test_func(self):
        return self.request.user.is_superuser


meal_create_view = MealCreateView.as_view()


class OptionsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = OptionsCreateForm
    success_url = reverse_lazy("menus:options")
    template_name = "create_option.html"
    login_url = reverse_lazy("users:login")
    permission_denied_message = "Please you need superuser attribute"

    def test_func(self):
        return self.request.user.is_superuser


options_create_view = OptionsCreateView.as_view()
