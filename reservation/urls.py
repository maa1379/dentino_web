from django.urls import path

from .views import ReserveListView

app_name = "reserve"
urlpatterns = [
    path("reserve_list/", ReserveListView.as_view(), name="list"),
]
