from django.urls import path

from .views import DoctorListApiView, ExpertiseList, TimeListApiView

app_name = "doctor_api"

urlpatterns = [
    path("", ExpertiseList.as_view(), name="Home"),
    path("doctor/", DoctorListApiView.as_view(), name="list"),
    path("time/", TimeListApiView.as_view(), name="time"),
]
