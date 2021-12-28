from django.urls import path

from .views import (  # InsuranceCreateVIew,; InsuranceDeleteView,; InsuranceListView,; InsuranceUpdateView,
    ComanyDeleteView, CompanyCreateView, CompanyListView, CompanyUpdateView,
    ComplimentListVIew, PrescriptionCreate, PrescriptionDeleteVIew,
    PrescriptionDetailView, PrescriptionListView, PrescriptionUpdate,
    PriceCreateVIew, PriceDeleteView, PriceListView, PriceUpdateView,DoctorDictionaryList,DoctorDictionaryCreate,DoctoDictonaryUpdate,DoctorDictionaryDelete)

app_name = "partial"
urlpatterns = (
    path("prescription/", PrescriptionListView.as_view(), name="prescription_list"),
    path("dict_list/", DoctorDictionaryList.as_view(), name="dict_list"),
    path("dict_create/", DoctorDictionaryCreate.as_view(), name="dict_create"),
    path("dict_update/<int:id>/", DoctoDictonaryUpdate.as_view(), name="dict_update"),
    path("dict_delete/<int:id>/", DoctorDictionaryDelete.as_view(), name="dict_delete"),
    path(
        "prescription/<int:id>/",
        PrescriptionDetailView.as_view(),
        name="prescription_detail",
    ),
    path(
        "prescription/create/", PrescriptionCreate.as_view(), name="prescription_create"
    ),
    path(
        "prescription/update/<int:id>/",
        PrescriptionUpdate.as_view(),
        name="prescription_update",
    ),
    path(
        "prescription/delete/<int:id>/",
        PrescriptionDeleteVIew,
        name="prescription_delete",
    ),
    path("company/", CompanyListView.as_view(), name="company_list"),
    path("company/create/", CompanyCreateView.as_view(), name="company_create"),
    path(
        "company/update/<int:id>/",
        CompanyUpdateView.as_view(),
        name="company_update",
    ),
    path("company/delete/<int:id>/", ComanyDeleteView, name="company_delete"),
    # path("insurance/", InsuranceListView.as_view(), name="insurance_list"),
    # path(
    #     "insurance/delete/<slug:slug>/",
    #     InsuranceDeleteView.as_view(),
    #     name="insurance_delete",
    # ),
    # path(
    #     "insurance/update/<slug:slug>/",
    #     InsuranceUpdateView.as_view(),
    #     name="insurance_update",
    # ),
    # path("insurance/create/", InsuranceCreateVIew.as_view(), name="insurance_create"),
    path("price/", PriceListView.as_view(), name="price_list"),
    path("price/update/<int:id>/", PriceUpdateView.as_view(), name="price_update"),
    path("price/create/", PriceCreateVIew.as_view(), name="price_create"),
    path("price/delete/<int:id>/", PriceDeleteView, name="price_delete"),
    path("compliment_list/", ComplimentListVIew.as_view(), name="compliment"),
)
