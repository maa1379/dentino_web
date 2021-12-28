from django.urls import path

from .views import (ClinicCreateView, ClinicDeleteView, ClinicDetailView,
                    ClinicListView, ClinicUpdateVIew)

app_name = "clinic"
urlpatterns = [
    path("", ClinicListView.as_view(), name="Home"),
    path("create/", ClinicCreateView.as_view(), name="create"),
    path("delete/<int:pk>/", ClinicDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", ClinicUpdateVIew.as_view(), name="update"),
    path("<int:pk>/", ClinicDetailView.as_view(), name="detail"),
]
