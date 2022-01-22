from rest_framework import serializers

from ..models import Doctor, Expertise, VisitTime


class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = "__all__"

    # def get_doctor_time(self, obj):
    # return VisitTime.objects.filter(doctor__clinic__name=obj.name)


from django_jalali.serializers.serializerfield import (JDateField,
                                                       JDateTimeField)


class VisitTimeSerializer(serializers.ModelSerializer):
    date = JDateField()

    class Meta:
        model = VisitTime
        exclude = []


class DoctorSer(serializers.ModelSerializer):
    profile_url = serializers.SerializerMethodField()
    clinic_name = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = (
            "id",
            "full_name",
            "clinic_name",
            "profile_url",
            "expertise",
            "insurance",
        )

        depth = 1

    def get_profile_url(self, obj):
        return obj.profile.url

    def get_clinic_name(self, obj):
        return obj.clinic.name


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitTime
        fields = ("start_time", "finish_time")


# from rest_framework import serializers
# from ..models import Expertise, Doctor, VisitTime
#
#
# class ExpertiseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Expertise
#         fields = ("title", "id", "image")
#
#
# class DoctorListSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Doctor
#         fields = ("id", "full_name", "expertise", "clinic", "image")
#
#
# class VisitTimeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = VisitTime
#         fields = ("id", "date")
#
#
# class TimeSer(serializers.ModelSerializer):
#     class Meta:
#         model = VisitTime
#         fields = ("start_time",
#                   "finish_time")
#
#
# class Test(serializers.Serializer):
#     time = serializers.DateTimeField()
