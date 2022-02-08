from django.views.generic.edit import CreateView
from .models import Documento


class DocumentoCreate(CreateView):
    model = Documento
    fields = {'descricao', 'arquivo'}

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

