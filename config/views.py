from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, View
from doctor.models import Doctor
from clinic.models import Clinic
from .forms import PanelLoginForm, SliderForm
from .models import About_Us, SiteConfig, Slider
from reservation.models import Reservation
user = get_user_model()


# Create your views here.


class HomeView(View):
    def get(self, request):

        # print(user_number)
        return render(
            request,
            "config/Home.html",
            {

            },
        )


class PanelView(LoginRequiredMixin, View):
    def get(self, request):
        clinic=request.user.profile.clinic
        clinic_number = Clinic.objects.count()
        doctor_number = Doctor.objects.count()
        user_number = user.objects.count()
        reserve_number=Reservation.objects.count()
        if request.user.profile.is_clinic:
            clinic_number=Clinic.objects.filter(clinic=clinic).count()
            doctor_number = Doctor.objects.filter(clinic=clinic).count()
            reserve_number = Reservation.objects.filter(clinic=clinic).count()

        context={
            "clinic_number":clinic_number,
            "doctor_number":doctor_number,
            "user_number":user_number,
            "reserve_number":reserve_number
        }
        return render(request, "config/panel.html",context)


class PanelLoginView(View):
    template_name = "config/panel_login.html"
    form_class = PanelLoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("config:Panel")
        return super(PanelLoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        form = PanelLoginForm
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = PanelLoginForm(request.POST)
        if form.is_valid():
            human = True
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                login(request, user)
                messages.success(request, "", "success")
                return redirect("config:Panel")
            messages.error(request, "", "danger")
        return render(request, self.template_name, {"form": form})


class PanelLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "با موفقیت خارج شدید", "success")
        return redirect("config:login")


class SliderListView(ListView):
    model = Slider
    template_name = "config/slider_list.html"


class AddSliderView(CreateView):
    template_name = "config/slider_add.html"
    form_class = SliderForm
    success_url = reverse_lazy("config:slider_list")


class SliderUpdate(UpdateView):
    model = Slider
    form_class = SliderForm
    template_name = "config/slider_update.html"
    slug_field = "id"
    slug_url_kwarg = "id"
    success_url = reverse_lazy("config:slider_list")


from django.shortcuts import get_object_or_404


class SliderDelete(View):
    def get(self, request, id):
        slider = get_object_or_404(Slider, id=id)
        slider.delete()
        return redirect("config:slider_list")


class AboutUS_View(ListView):
    model = About_Us
    template_name = "config/about_us.html"


class SiteConfigView(ListView):
    model = SiteConfig
    template_name = "config/site_config.html"
