from django.db import models

# Create your models here.
class Documento(models.Model):
        num_doc = models.CharField(max_length=30)

        def __str__(self):
                return self.num_doc

class Cliente(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        age = models.IntegerField()
        salary = models.DecimalField(max_digits=5, decimal_places=2)
        photo = models.ImageField(upload_to='clientes_photos', null=True, blank=True)
        doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

        def __str__(self):
                return self.first_name + ' ' + self.last_name

class Produto(models.Model):
        descricao = models.CharField(max_length=30)
        preco = models.DecimalField(max_digits=5, decimal_places=2)

        def __str__(self):
                return self.descricao

class Venda(models.Model):
        num_venda = models.CharField(max_length=7)
        valor = models.DecimalField(max_digits=5, decimal_places=2)
        desconto = models.DecimalField(max_digits=5, decimal_places=2)
        impostos = models.DecimalField(max_digits=5, decimal_places=2)
        pessoa = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.PROTECT)
        produtos = models.ManyToManyField(Produto, blank=True)

        def __str__(self):
                return self.num_venda