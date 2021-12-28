from rest_framework import serializers

from ..models import SiteConfig, Slider


class SiteConfigSerializer(serializers.ModelSerializer):
    # image=serializers.SerializerMethodField()
    class Meta:
        model = SiteConfig
        fields = ("Title", "Icon")


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ("picture",)
