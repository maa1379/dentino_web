from django.urls import path

from .views import (DoctorCreateView, DoctorDeleteView, DoctorDetailView,
                    DoctorListView, DoctorUpdateView, ExpertiseCreateView,
                    ExpertiseDelete, ExpertiseListView, ExpertiseUpdateView,
                    InsuranceCreateVIew, InsuranceDeleteView,
                    InsuranceListView, InsuranceUpdateView,
                    Unverified_Doctor_ListView, VisitTimeView, verify_doctor)

app_name = "doctor"

urlpatterns = [
    path("doctor_lsit/", DoctorListView, name="list"),
    path("verify_doctor/<int:id>/", verify_doctor.as_view(), name="verify_doctor"),
    path(
        "unverified_doctor_list/",
        Unverified_Doctor_ListView.as_view(),
        name="unverified_doctor",
    ),
    path("docotr/<int:pk>/", DoctorDetailView.as_view(), name="detail"),
    path("doctor/create/", DoctorCreateView.as_view(), name="create"),
    path("doctor/delete/<int:pk>/", DoctorDeleteView.as_view(), name="delete"),
    path("doctor/update/<int:pk>/", DoctorUpdateView.as_view(), name="update"),
    path("expertise_add/", ExpertiseCreateView.as_view(), name="expertise_create"),
    path("expertise_list", ExpertiseListView.as_view(), name="expertise_list"),
    path(
        "expertise/update/<int:id>/",
        ExpertiseUpdateView.as_view(),
        name="expertise_update",
    ),
    path("expertise/delete/<int:pk>/", ExpertiseDelete, name="expertise_delete"),
    path("visittime/", VisitTimeView, name="visit_time"),
    path("insurance/", InsuranceListView.as_view(), name="insurance_list"),
    path("insurance/create/", InsuranceCreateVIew.as_view(), name="insurance_create"),
    path(
        "insurance/update/<int:id>/",
        InsuranceUpdateView.as_view(),
        name="insurance_update",
    ),
    path("insurance/delete/<int:id>/", InsuranceDeleteView, name="insurance_delete"),
]
