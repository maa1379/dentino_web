import django_filters

from doctor.models import Doctor

# from location.models import Location


class DoctorFilter(django_filters.FilterSet):
    # loc = Location.objects.all()

    class Meta:
        model = Doctor
        fields=["name"]
        # fields = ["clinic", "insurance", "clinic__type"]
        # fields = ["clinic__type"]
