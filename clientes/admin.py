from django.contrib import admin
from .models import Cliente, Documento, Venda, Produto

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Documento)
admin.site.register(Venda)
admin.site.register(Produto)