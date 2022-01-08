from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  View)
from kavenegar import KavenegarAPI

from clinic.models import Clinic
from .forms import DoctorForm, ExpertiseForm, InsuranceForm, TestForm
from .models import Doctor, Expertise, Insurance, VisitTime


# Expertise Views .
def ClinicVerifyOk(request, clinic_id):
    clinic = get_object_or_404(Clinic,clinic_id=clinic_id)
    api = KavenegarAPI(
        "38502F546846716559723175674E49324A674B2B62654B58724D61314B474777"
    )
    params = {
        "receptor": clinic.phone_number,
        "template": "dentinoClinicVerify",
        "token": str(clinic.name),
        "token2": "",
        "token3": "",
        "type": "sms",
    }
    api.verify_lookup(params)


class VisitTimeCreate(CreateView):
    model = VisitTime
    form_class = TestForm
    template_name = "doctor/visit_time.html"


def VisitTimeView(request):
    print(request.META.get("HTTP_REFERER"))
    perviouse_url = request.META.get("HTTP_REFERER")
    # doctor=perviouse_url[-2]
    # print(doctor)
    # doctor=get_object_or_404(Doctor,id=doctor.id)

    form = TestForm
    # print(request.POST.get("date"))
    date = request.POST.get("date")
    day = request.POST.get("day")
    # print(request.POST.get("start_time1"))
    start_time1 = request.POST.get("start_time1")
    start_time2 = request.POST.get("start_time2")
    finish_time1 = request.POST.get("finish_time1")
    finish_time2 = request.POST.get("finish_time2")
    # hour_1=str(start_time1[0:2])
    # print(hour_1)
    # minutes_1=int(start_time1[3:5])
    # hour_2= int(start_time2[0:2])
    # minutes_2 = int(start_time2[3:5])
    # hour_3 = int(finish_time1[0:2])
    # minutes_3 = int(finish_time1[3:5])
    # hour_4 = int(finish_time2[0:2])
    # minutes_4 = int(finish_time2[3:5])

    # test=finish_time1(0,2)
    # print(test)
    # print(start_time1[:2])
    # date_string = f'2021-12-31 +{start_time1}'
    # dateobj = datetime.date(2021, 12, 31)
    # timeobj = datetime.time(start_time1[:2],start_time1[3:5], 00)
    # datetimeobj = datetime(2021,12,31,hour,minutes,00)
    # print(datetimeobj)
    # start_time1_value=datetime.datetime(2021,5,12,hour_1,minutes_1)
    # start_time2_value=datetime.datetime(2021,5,12,hour_2,minutes_2)
    # finish_time2_value=datetime.datetime(2021,5,12,hour_2,minutes_2)
    # _time2_value=datetime.datetime(2021,5,12,hour_2,minutes_2)
    # datetime = datetime.strptime(date_string, '%Y-%m-%d')
    # print(request.POST.get("finish_time1"))
    # print(request.POST.get("start_time2"))
    # print(request.POST.get("finish_time2"))
    # print(request.POST.get("finish_time1"))
    # print(request.POST.get("time1"))
    # print(request.POST.get("doctor"))
    # print(request.POST.get("date"))
    # print(request.POST.get("start_time"))
    # print(request.POST.get("finish_time"))
    # print(request.POST.get("start_time2"))
    # print(request.POST.get("finish_time2"))
    # if request.method=="POST":
    #     if form.is_valid():
    #         day=form.cleaned_data["day"]
    #         date=form.cleaned_data["date"]
    #
    # VisitTime.objects.create(day=day,date=date,doctor=,start_time=start_time1,start_time2=start_time2,finish_time=finish_time1,finish_time2=finish_time2)
    return render(request, "doctor/visit_time.html", {"form": form})


class ExpertiseListView(ListView):
    model = Expertise
    template_name = "doctor/expertise_list.html"
    context_object_name = "expertise"


class ExpertiseCreateView(CreateView):
    form_class = ExpertiseForm
    success_url = reverse_lazy("doctor:expertise_list")

    def form_valid(self, form):
        messages.success(self.request, "this is success message", "success")
        return super(ExpertiseCreateView, self).form_valid(form)

    template_name = "doctor/expertise_add.html"


class ExpertiseUpdateView(UpdateView):
    slug_field = "id"
    slug_url_kwarg = "id"
    form_class = ExpertiseForm
    model = Expertise
    success_url = reverse_lazy("doctor:expertise_list")
    template_name = "doctor/expertise_update.html"


def ExpertiseDelete(request, pk):
    service = Expertise.objects.filter(id=pk)
    # print(service)
    service.delete()
    # messages.success(self.request, "با موفقیت حذف شد", "success")
    return redirect("doctor:expertise_list")


# Doctor Views
class Unverified_Doctor_ListView(ListView):
    queryset = Doctor.objects.filter(verified=False)
    template_name = "doctor/unverified_doctor.html"
    context_object_name = "doctor"


class verify_doctor(View):
    def get(self, request, id):
        doctor = get_object_or_404(Doctor, id=id)
        doctor.verified = True
        doctor.save()
        return redirect("doctor:unverified_doctor")


def DoctorListView(request):
    queryset = Doctor.objects.filter(verified=True)
    if request.user.profile.is_clinic:
        clinic = request.user.profile.clinic
        queryset = Doctor.objects.filter(clinic=clinic)

    return render(request, "doctor/doctor_list.html", {"object_list": queryset})


class DoctorDetailView(DetailView):
    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        doctor = get_object_or_404(Doctor, id=pk)
        return doctor

    template_name = "doctor/doctor_detail.html"
    context_object_name = "doctor"


class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy("doctor:list")
    template_name = "doctor/doctor_create.html"

    def form_valid(self, form):
        new = form.save(commit=False)
        if self.request.user.profile.is_clinic:
            clinic = Clinic.objects.get(id=self.request.user.profile.clinic.id)
        else:
            clinic = form.cleaned_data["clinic"]
        new.clinic = clinic
        new.save()
        return super(DoctorCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.has_error("clinic"))
        return super(DoctorCreateView, self).form_invalid(form)


class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    slug_field = "pk"
    slug_url_kwarg = "pk"
    template_name = "doctor/doctor_update.html"
    success_url = reverse_lazy("doctor:list")

    def form_valid(self, form):
        new = form.save(commit=False)
        if self.request.user.profile.is_clinic:
            clinic = Clinic.objects.get(id=self.request.user.profile.clinic.id)
        else:
            clinic = form.cleaned_data["clinic"]
        new.clinic = clinic
        new.save()
        return super(DoctorUpdateView, self).form_valid(form)


class DoctorDeleteView(View):
    def get(self, request, pk):
        doctor = get_object_or_404(Doctor, id=pk)
        doctor.delete()
        messages.success(request, f"{doctor} حذف شد", "success")
        return redirect("doctor:list")


# insurance  completed


class InsuranceListView(ListView):
    model = Insurance
    template_name = "insurance_list.html"


class InsuranceUpdateView(UpdateView):
    model = Insurance
    form_class = InsuranceForm
    template_name = "insurance_update.html"
    success_url = reverse_lazy("doctor:insurance_list")
    slug_field = "id"
    slug_url_kwarg = "id"


class InsuranceCreateVIew(CreateView):
    model = Insurance
    form_class = InsuranceForm
    template_name = "insurance_create.html"
    success_url = reverse_lazy("doctor:insurance_list")


def InsuranceDeleteView(request, id):
    insurance = get_object_or_404(Insurance, id=id)
    insurance.delete()
    return redirect("doctor:insurance_list")
