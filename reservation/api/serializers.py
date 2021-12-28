from rest_framework import serializers

from ..models import Reservation


class RseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            "name",
            "family",
            "phone_number",
            "national_code",
        )
