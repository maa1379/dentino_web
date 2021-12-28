from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  View)

from config.mixins import SuperUserMixin
from doctor.models import Doctor
from reservation.models import Reservation
from .forms import ClinicCreateForm, ServiceCreateForm
from .models import Clinic, Service
from doctor.models import Insurance

# from django_filters.views import FilterView


class ClinicListView(SuperUserMixin, ListView):
    model = Clinic
    template_name = "clinic/list.html"
    paginate_by = 12


class ClinicDetailView(SuperUserMixin, DetailView):
    def get_object(self, **kwargs):
        global clinic
        pk = self.kwargs.get("pk")
        clinic = get_object_or_404(Clinic, pk=pk)
        return clinic

    template_name = "clinic/detail.html"
    context_object_name = "clinic"

    def get_context_data(self, *args, **kwargs):
        context_data = super(ClinicDetailView, self).get_context_data(*args, **kwargs)
        context_data["reserve"] = Reservation.objects.filter(doctor__clinic=clinic)
        context_data["doctor_list"] = Doctor.objects.filter(clinic=clinic)
        context_data["insurance_list"] = Insurance.objects.filter(doctor__clinic=clinic)

        return context_data


class ClinicDeleteView(SuperUserMixin, View):
    def get(self, request, pk):
        clinic = get_object_or_404(Clinic, pk=pk)
        clinic.delete()
        messages.success(request, "حذف شد", "success")
        return redirect("clinic:Home")


class ClinicCreateView(SuperUserMixin, CreateView, SuccessMessageMixin):
    model = Clinic
    form_class = ClinicCreateForm
    success_url = reverse_lazy("clinic:Home")
    SuccessMessageMixin = "OK"
    template_name = "clinic/create.html"


class ClinicUpdateVIew(SuperUserMixin, UpdateView, SuccessMessageMixin):
    model = Clinic
    form_class = ClinicCreateForm
    success_url = reverse_lazy("clinic:Home")
    success_message = "ok"
    slug_field = "id"
    slug_url_kwarg = "id"
    SuccessMessageMixin = reverse_lazy("clinic:Home")
    template_name = "clinic/update.html"


class ServiceListView(ListView):
    model = Service
    template_name = "clinic/services.html"
    context_object_name = "services"


class ServiceCreateView(CreateView):
    form_class = ServiceCreateForm

    success_url = reverse_lazy("m:Services")

    # SuccessMessageMixin = "OK"
    def form_valid(self, form):
        messages.success(self.request, "this is success message", "success")
        return super(ServiceCreateView, self).form_valid(form)

    template_name = "clinic/AddService.html"


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ("title",)
    SuccessMessageMixin = "OK"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            "mapbox_access_token"
        ] = "pk.eyJ1IjoidHVuYWhvYmJ5IiwiYSI6ImNra3IwaDNxcTBtbzAycm81dTFpOWhvcjAifQ.8ixXcuSDUuAlDSlazSLMCA"
        return context


class ServiceDelete(View):
    def get(self, slug):
        service = get_object_or_404(Service, slug=slug)
        service.delete()
        messages.success(self.request, "با موفقیت حذف شد", "success")
        return redirect("m:Services")
