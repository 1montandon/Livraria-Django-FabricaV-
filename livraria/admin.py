from django.contrib import admin

from livraria.models import Autor, Categoria, Editora, Livro

# Register your models here.


admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)
admin.site.register(Autor)
