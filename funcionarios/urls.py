from django.urls import path

from .views import FuncionariosView, FuncionarioAddView, FuncionarioUpdateView, FuncionarioDeleteView

urlpatterns = [
    path('funcionarios/', FuncionariosView.as_view(), name='funcionarios'),
    path('funcionarios/adicionar', FuncionarioAddView.as_view(), name='funcionario_adicionar'),
    path('<int:pk>/funcionarios/editar/', FuncionarioUpdateView.as_view(), name='funcionario_editar'),
    path('<int:pk>/funcionarios/apagar/', FuncionarioDeleteView.as_view(), name='funcionario_apagar'),
]