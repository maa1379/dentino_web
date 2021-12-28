from django.urls import path

from .views import HomeApiView

app_name = "config_api"

urlpatterns = [
    path("", HomeApiView.as_view(), name="Home"),
]
