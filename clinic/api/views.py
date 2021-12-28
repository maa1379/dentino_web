import datetime

from rest_framework import generics
from rest_framework.response import Response

from doctor.api.serailizers import DoctorSer, VisitTimeSerializer
from doctor.models import Doctor, Expertise, VisitTime
from utilities.respones import ErrorResponse, SuccessResponse

from .serializers import ExpertiseSerializer, Test, TimeSer


class ExpertiseListApiView(generics.ListAPIView):
    serializer_class = ExpertiseSerializer
    model = Expertise

    def get(self, request, *args, **kwargs):
        try:
            instance = self.model.objects.all()
            serialized_data = self.serializer_class(instance, many=True).data
            return SuccessResponse(data=serialized_data).send()
        except:
            return ErrorResponse(message="failed").send()


# class ExpertiseListApiView(generics.ListAPIView):
#     queryset = Expertise.objects.all()
#     serializer_class = ExpertiseSerializer


class DoctorListApiView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        # id=request.POST.get("pk")
        pk = request.POST.get("id")
        try:
            instance = Doctor.objects.filter(id=pk)
            serialize_data = DoctorSer(instance, many=True).data
            name = VisitTime.objects.filter(doctor=pk)
            date = VisitTimeSerializer(name, many=True).data
            tempe_data = {
                "doctor_list": serialize_data,
                "date_list": date,
            }
            return SuccessResponse(data=tempe_data).send()
        except Expertise.DoesNotExist as e:
            return ErrorResponse(message="Instance does not Found.", status=404).send()


class TimeListApiView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        pk = request.POST.get("pk")
        id = request.POST.get("id")

        try:
            my_list = []
            instance = VisitTime.objects.filter(doctor=pk, id=id)
            a = instance.values("start_time")
            b = instance.values("finish_time")
            my_list = []
            for v in instance:
                a = v.start_time
                b = v.finish_time
                while True:
                    a = a + datetime.timedelta(minutes=30)
                    my_list.append(
                        str(a.time().replace(hour=a.hour, minute=a.minute, second=00))[
                            :5
                        ]
                    )
                    if a >= b:
                        break
            print(my_list)
            ser_data = TimeSer(instance, many=True).data
            temp_data = {"data": ser_data, "my_list": my_list}
            return Response(data=temp_data, status=201)
        except:
            return ErrorResponse(message="Instance does not Found.", status=404).send()
