from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from .forms import ZoneForm, CityForm, ProvinceForm, LocationForm
from .models import Zone, Province, City


class ProvinceCreate(CreateView):
    model = Province
    form_class = ProvinceForm
    template_name = "location/province_create.html"
    success_url = reverse_lazy("location:province")


class ProvinceUpdate(UpdateView):
    model = Province
    form_class = ProvinceForm
    template_name = "location/province_update.html"
    success_url = reverse_lazy("location:province")
    slug_field = "id"
    slug_url_kwarg = "id"


class ProvinceListView(ListView):
    model = Province
    template_name = "location/province_list.html"
    context_object_name = "province"


class ProvinceDetail(DetailView):
    def get_queryset(self):
        global province
        province = self.kwargs.get("pk")
        return Province.objects.filter(id=province)

    template_name = "location/city_list.html"
    context_object_name = "province"


def ProvinceDelete(request, id):
    province = get_object_or_404(Province, id=id)
    province.delete()
    return redirect("Location:province")





class CityCreateView(CreateView):
    model=City
    form_class = CityForm
    success_url = reverse_lazy("Location:city_list")
    template_name = "location/city_create.html"


class CityListView(ListView):
    model = City
    template_name = "location/city_lista.html"



class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    success_url = reverse_lazy("Location:city_list")
    template_name = "location/update_city.html"
    slug_field = "id"
    slug_url_kwarg = "id"


def CityDeleteView(request, id):
    location = get_object_or_404(City, id=id)
    location.delete()
    return redirect("Location:city_list")



class ZoneListView(ListView):
    model = Zone
    template_name = "location/zone_list.html"




class ZoneCreate(CreateView):
    model = Zone
    form_class = ZoneForm
    template_name = "location/zone_create.html"
    success_url = reverse_lazy("location:zone_list")



class ZoneUpdate(UpdateView):
    model=Zone
    form_class = ZoneForm
    slug_field = "id"
    slug_url_kwarg = "id"
    success_url = reverse_lazy("location:zone_list")
    template_name = "location/zone_update.html"

def ZoneDeleteView(request,id):
    zone=get_object_or_404(Zone,id=id)
    zone.delete()
    return redirect("location:zone_list")
