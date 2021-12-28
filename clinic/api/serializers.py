from rest_framework import serializers

from doctor.models import Doctor, Expertise, VisitTime


class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = ("title", "id", "image")


class DoctorListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ("id", "full_name", "expertise", "clinic", "image")


class VisitTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitTime
        fields = ("id", "date")


class TimeSer(serializers.ModelSerializer):
    class Meta:
        model = VisitTime
        fields = ("start_time", "finish_time")


class Test(serializers.Serializer):
    time = serializers.DateTimeField()
