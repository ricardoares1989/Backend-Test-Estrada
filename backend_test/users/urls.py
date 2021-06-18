from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import user_signup_view

app_name = "users"
urlpatterns = [
    path("signup/", view=user_signup_view, name="signup"),
    path("login/", view=LoginView.as_view(), name="login"),
    path("logout/", view=LogoutView.as_view(), name="logout"),
]
