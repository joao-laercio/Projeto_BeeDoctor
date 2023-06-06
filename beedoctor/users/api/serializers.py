from django.contrib.auth import get_user_model
from rest_framework import serializers
from dataclasses import fields
from django.db import models
from beedoctor.users.models import Medico,Especialidade, Clinica, Consulta

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "cpf", "data_nascimento", "endereco", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }

        
class MedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'


class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = "__all__"


class ClinicaSerializer(serializers.ModelSerializer):
    especialidades = EspecialidadeSerializer(many=True)

    class Meta:
        model = Clinica
        fields = "__all__"


class ConsultaSerializer(serializers.ModelSerializer):
    paciente = UserSerializer()
    medico = MedicosSerializer()
    clinica = ClinicaSerializer()

    class Meta:
        model = Consulta
        fields = "__all__"
