from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from utilities.respones import ErrorResponse, SuccessResponse

from ..models import Slider
from .serailizers import SliderSerializer


class HomeApiView(generics.ListAPIView):
    def get(self, request):
        try:
            slider_list = SliderSerializer(Slider.objects.all(), many=True).data
            temp_data = {"slider": slider_list}
            return SuccessResponse(temp_data).send()
        except Exception as e:
            return ErrorResponse(message=str(e)).send()


class ReserveApiView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
