from django.urls import path

from .views import ReserveCreateView

app_name = "reservation_api"
urlpatterns = [
    path("", ReserveCreateView.as_view(), name="Home"),
]
