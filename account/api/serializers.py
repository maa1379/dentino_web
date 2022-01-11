from rest_framework import serializers

from ..models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_number",)


class UserVerifySerializer(serializers.Serializer):
    verify_code = serializers.CharField()


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "family",
            "profile_image",
            "insurance_scan",
            "insurance_code",
            "national_code",
        )
