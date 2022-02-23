from django.urls import path
from .views import FuncionariosList, FuncionarioEdit, FuncionarioDeletar, FuncionarioNovo, Pdf

urlpatterns = [
    path('', FuncionariosList.as_view(), name='funcionario_list'),
    path('editar/<int:pk>', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>', FuncionarioDeletar.as_view(), name='delete_funcionario'),
    path('novo/', FuncionarioNovo.as_view(), name='create_funcionario'),
    path('relatorio_funcionario_html/', Pdf.as_view, name='relatorio_funcionario_html'),

]
