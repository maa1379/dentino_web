from django.urls import path

from .views import DoctorListApiView, ExpertiseListApiView, TimeListApiView

app_name = "clinic_api"

urlpatterns = [
    path("", ExpertiseListApiView.as_view(), name="Home"),
    path("doctor/", DoctorListApiView.as_view(), name="list"),
    path("abbas/", TimeListApiView.as_view(), name="time"),
]
