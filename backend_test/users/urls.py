from django.urls import path

from .views import user_signup_view, user_login_view

app_name = "users"
urlpatterns = [
    path("signup/", view=user_signup_view, name="signup"),
    path("login/", view=user_login_view, name="login")
]
