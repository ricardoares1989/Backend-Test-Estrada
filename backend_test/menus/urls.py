from django.urls import path

from .views import meal_create_view, menu_detail_view

app_name = "menus"
urlpatterns = [
    path("meals/", view=meal_create_view, name="create_meal"),
    path("<pk>/", view=menu_detail_view, name="detail"),
]
