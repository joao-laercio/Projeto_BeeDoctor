from django.contrib.auth import get_user_model
from rest_framework import serializers
from dataclasses import fields
from django.db import models
from beedoctor.users.models import Medico

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }
class MedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'
