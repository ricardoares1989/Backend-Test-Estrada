from django.utils import timezone
from django.views.generic import TemplateView

from backend_test.menus.models import Menu


class HomeMenuView(TemplateView):
    """
    View for render the menu of the day in the root path.
    """

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        """
        This context data implements getting process of the current menu.
        """
        kwargs = super().get_context_data(**kwargs)
        try:
            menu = Menu.objects.get(date__exact=timezone.now().date())
            kwargs.update({"menu": menu})
        except Menu.DoesNotExist:
            pass
        return kwargs


home_view = HomeMenuView.as_view()
