from django.urls import path

from .views import (
    ClinicCreateView,
    ClinicDeleteView,
    ClinicDetailView,
    ClinicListView,
    ClinicUpdateVIew,
    CreateDiscount,
    DiscountDelete,
    DiscountListView,
    UnverifiedClinicListView,
    UpdateDiscount,
    VerifyClinic,
)

app_name = "clinic"
urlpatterns = [
    path("", ClinicListView.as_view(), name="Home"),
    path("unverified/", UnverifiedClinicListView.as_view(), name="unverified"),
    path("create/", ClinicCreateView.as_view(), name="create"),
    path("delete/<int:pk>/", ClinicDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", ClinicUpdateVIew.as_view(), name="update"),
    path("verify/<int:id>/", VerifyClinic.as_view(), name="verify"),
    path("<int:pk>/", ClinicDetailView.as_view(), name="detail"),
    path("discount_list/", DiscountListView.as_view(), name="discount_list"),
    path("discount_create/", CreateDiscount.as_view(), name="discount_create"),
    path("discount_update/<int:id>/", UpdateDiscount.as_view(), name="discount_update"),
    path("discount_delete/<int:id>/", DiscountDelete, name="discount_delete"),
]
