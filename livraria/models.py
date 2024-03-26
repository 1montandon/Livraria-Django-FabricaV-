from django.db import models

# Create your models here.

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)