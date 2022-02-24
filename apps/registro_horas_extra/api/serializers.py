from apps.registro_horas_extra.models import RegistroHorasExtra
from rest_framework import serializers


class RegistroHorasExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroHorasExtra
        fields = ['motivo', 'funcionario', 'horas', 'utilizadas']

