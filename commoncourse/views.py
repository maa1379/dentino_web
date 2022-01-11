from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView, UpdateView,
                                  View)

from .forms import CommenCourseForm
from .models import Common_Course


# Create your views here.
class CommonCourseList(ListView):
    model = Common_Course
    template_name = "common_course/list.html"


def CommonCourseDetail(request, id):
    course = get_object_or_404(Common_Course, id=id)
    return render(request, "common_course/detail.html", {"object": course})


class CommonCourseCreate(CreateView):
    model = Common_Course
    form_class = CommenCourseForm
    template_name = "common_course/create.html"
    success_url = reverse_lazy("common_course:list")




class CommonCourseUpdate(UpdateView):
    model = Common_Course
    form_class = CommenCourseForm
    template_name = "common_course/update.html"
    success_url = reverse_lazy("common_course:list")
    slug_field = "pk"
    slug_url_kwarg = "pk"


def CommonCourseDelete(request, pk):
    course = get_object_or_404(Common_Course, pk=pk)
    course.delete()
    return redirect("common_course:list")
