from rest_framework import serializers
from .models import Usecase


class UsecaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usecase
        exclude = ("created_at",)
