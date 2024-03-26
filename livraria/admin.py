from django.contrib import admin

# Register your models here.

from livraria.models import Categoria, Editora


admin.site.register(Categoria)
admin.site.register(Editora)
