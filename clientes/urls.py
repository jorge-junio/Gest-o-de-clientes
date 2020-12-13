from django.urls import path
from .views import listaCliente
from .views import adicionarCliente
from .views import editarCliente
from .views import excluirCliente

urlpatterns = [
    path('listar/', listaCliente, name='listarCliente'),
    path('adicionar/', adicionarCliente, name='adicionarCliente'),
    path('editar/<int:id>/', editarCliente, name='editarCliente'),
    path('excluir/<int:id>/', excluirCliente, name='excluirCliente'),
]
