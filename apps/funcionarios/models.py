from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

from apps.departamentos.models import Departamento
from apps.empresa.models import Empresa
from django.urls import reverse


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('funcionario_list')

    @property
    def total_horas_extra(self):
        return self.registrohorasextra_set.all().aggregate(Sum('horas'))['horas__sum']

    def __str__(self):
        return self.nome