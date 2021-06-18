from django.urls import path

from .views import (
    meal_create_view,
    menu_create_view,
    menu_detail_view,
    options_create_view,
)

app_name = "menus"
urlpatterns = [
    path("", view=menu_create_view, name="create_menu"),
    path("meals/", view=meal_create_view, name="create_meal"),
    path("options/", view=options_create_view, name="create_options"),
    path("<pk>/", view=menu_detail_view, name="detail"),
]
