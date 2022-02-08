from django.urls import reverse_lazy
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
