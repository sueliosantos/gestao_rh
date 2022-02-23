import io

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
from django.views.generic.base import View
"""from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
"""

class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDeletar(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionario_list')


class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1])
        funcionario.save()
        return super(FuncionarioNovo, self).form_valid(form)


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        pass

        """ template = get_template(path)
        html = template.render(params)

        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)

        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)
"""


class Pdf(View):
    pass
    """def get(self, request):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',
            'request': request,
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')
"""