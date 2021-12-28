from django.shortcuts import render
from django.views.generic import ListView

from .models import Reservation

# Create your views here.


class ReserveListView(ListView):
    model = Reservation
    template_name = "reserve/reserve_list.html"
