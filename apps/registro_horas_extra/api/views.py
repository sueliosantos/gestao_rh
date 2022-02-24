from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from apps.registro_horas_extra.api.serializers import RegistroHorasExtraSerializer
from apps.registro_horas_extra.models import RegistroHorasExtra


class RegistroHorasExtraViewSet(viewsets.ModelViewSet):
    queryset = RegistroHorasExtra.objects.all()
    serializer_class = RegistroHorasExtraSerializer
    permission_classes = [permissions.IsAuthenticated]