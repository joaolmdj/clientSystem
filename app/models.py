from django.db import models

# Create your models here.


class Pedidos(models.Model):
    nome = models.CharField(max_length=150)
    preco = models.CharField(max_length=100)
    multiplo = models.IntegerField()
