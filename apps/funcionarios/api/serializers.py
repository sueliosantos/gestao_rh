from apps.funcionarios.models import Funcionario
from rest_framework import serializers
from apps.registro_horas_extra.api.serializers import RegistroHorasExtraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):
    registrohorasextra_set = RegistroHorasExtraSerializer(many=True)

    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'user', 'departamentos', 'empresa', 'total_horas_extra', 'registrohorasextra_set']

