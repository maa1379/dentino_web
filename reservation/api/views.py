from rest_framework import generics

from utilities.respones import ErrorResponse, SuccessResponse

from ..models import Reservation
from .serializers import RseSerializer


class ReserveCreateView(generics.CreateAPIView):
    queryset = Reservation
    serializer_class = RseSerializer

    def perform_create(self, serializer):
        serializer.save(
            day=self.request.POST.get("day"),
            time=self.request.POST.get("time"),
            doctor_id=self.request.POST.get("id"),
        )
