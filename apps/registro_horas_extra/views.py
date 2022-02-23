import csv
import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import RegistroHorasExtra
from .forms import RegistroHoraExtraForm


class HoraExtraList(ListView):
    model = RegistroHorasExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHorasExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = RegistroHorasExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwards = super(HoraExtraEdit, self).get_form_kwargs()
        kwards.update({'user': self.request.user})
        return kwards


class HoraExtraDelete(DeleteView):
    model = RegistroHorasExtra
    success_url = reverse_lazy('list_hora_extra')


class HoraExtraNovo(CreateView):
    model = RegistroHorasExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwards = super(HoraExtraNovo, self).get_form_kwargs()
        kwards.update({'user': self.request.user})
        return kwards


class HoraExtraEditBase(UpdateView):
    model = RegistroHorasExtra
    form_class = RegistroHoraExtraForm
    success_url = reverse_lazy('list_hora_extra')

    def get_form_kwargs(self):
        kwards = super(HoraExtraEditBase, self).get_form_kwargs()
        kwards.update({'user': self.request.user})
        return kwards


class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHorasExtra.objects.get(id=kwargs['pk'])
        desmarcar = self.request.POST['reverter']

        if (desmarcar == 'True'):
            registro_hora_extra.utilizadas = True
        else:
            registro_hora_extra.utilizadas = False
        registro_hora_extra.save()
        empregado = self.request.user.funcionario

        response = json.dumps({'mensagem': 'Requisição executada', 'horas': float(empregado.total_horas_extra)})
        return HttpResponse(response, content_type='appication/json')


class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename"meuarquivo.csv"'

        registros = RegistroHorasExtra.objects.filter(utilizadas=False)
        writer = csv.writer(response)
        writer.writerow(['Id', 'Motivo', 'Funcionário', 'Horas'])

        for r in registros:
            writer.writerow([r.id, r.motivo, r.funcionario, r.funcionario.total_horas_extra])

        return response