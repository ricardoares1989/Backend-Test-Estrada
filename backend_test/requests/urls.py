from django.urls import path

from .views import create_request_view, request_list_view

app_name = "requests"
urlpatterns = [
    path("", view=create_request_view, name="create_request"),
    path("today/", view=request_list_view, name="list_request"),
]
