from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView,View
from config.mixins import SuperUserMixin

from .forms import CompanyForm, PrescriptionForm, PriceForm,DoctorDictionaryForm
from .models import Company, Complaint, Prescriptions, Price,DoctorDictionary




class PrescriptionListView(SuperUserMixin, ListView):
    model = Prescriptions
    template_name = "partial/prescription_list.html"


class PrescriptionDetailView(SuperUserMixin, DetailView):
    model = Prescriptions
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "partial/prescription_detail.html"


class PrescriptionCreate(SuperUserMixin, CreateView):
    model = Prescriptions
    form_class = PrescriptionForm
    template_name = "partial/prescription_create.html"
    success_url = reverse_lazy("partial:prescription_list")


class PrescriptionUpdate(SuperUserMixin, UpdateView):
    model = Prescriptions
    form_class = PrescriptionForm
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "prescription_update.html"
    success_url = reverse_lazy("partial:prescription_list")


def PrescriptionDeleteVIew(request, id):
    prescription = get_object_or_404(Prescriptions, id=id)
    prescription.delete()
    return redirect("partial:prescription_list")


# company completed
class CompanyListView(SuperUserMixin, ListView):
    model = Company
    template_name = "company_list.html"


class CompanyCreateView(SuperUserMixin, CreateView):
    model = Company
    template_name = "company_create.html"
    form_class = CompanyForm
    success_url = reverse_lazy("partial:company_list")


class CompanyUpdateView(SuperUserMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = "company_update.html"
    success_url = reverse_lazy("partial:company_list")
    slug_field = "id"
    slug_url_kwarg = "id"


def ComanyDeleteView(request, id):
    company = get_object_or_404(Company, id=id)
    company.delete()
    return redirect("partial:company_list")


# price compeleted
class PriceListView(SuperUserMixin, ListView):
    model = Price
    template_name = "price_list.html"


class PriceUpdateView(SuperUserMixin, UpdateView):
    model = Price
    form_class = PriceForm
    template_name = "price_update.html"
    success_url = reverse_lazy("partial:price_list")
    slug_field = "id"
    slug_url_kwarg = "id"


class PriceCreateVIew(SuperUserMixin, CreateView):
    model = Price
    template_name = "price_create.html"
    success_url = reverse_lazy("partial:price_list")
    form_class = PriceForm


def PriceDeleteView(request, id):
    price = get_object_or_404(Price, id=id)
    price.delete()
    return redirect("partial:price_list")


class ComplimentListVIew(SuperUserMixin, ListView):
    model = Complaint
    template_name = "partial/compliment.html"


class DoctorDictionaryList(ListView):
    model = DoctorDictionary
    template_name = "partial/DoctorDictionaryList.html"


class DoctorDictionaryCreate(CreateView):
    model = DoctorDictionary
    template_name = "partial/DoctorDictionaryCreate.html"
    form_class = DoctorDictionaryForm
    success_url = reverse_lazy("partial:dict_list")


class DoctoDictonaryUpdate(UpdateView):
    model = DoctorDictionary
    template_name = "partial/DoctorDictionaryUpdate.html"
    form_class = DoctorDictionaryForm
    success_url = reverse_lazy("partial:dict_list")
    slug_field = "id"
    slug_url_kwarg = "id"


class DoctorDictionaryDelete(View):
    def get(self, request, id):
        dic = get_object_or_404(DoctorDictionary, id=id)
        dic.delete()
        return redirect("partial:dict_list")
