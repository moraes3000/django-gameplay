from django.contrib import admin

from .models import CategoriaModel, JogoModel

# Register your models here.

# personalizar o djangoadmin

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome','slug']
    search_fields = ['nome','slug']
    list_filter = ['nome']


class JogoAdmin(admin.ModelAdmin):
    list_display = ['nome','slug']
    search_fields = ['nome','slug','categoria__nome']
    list_filter = ['categoria__nome']

admin.site.register(CategoriaModel, CategoriaAdmin)
admin.site.register(JogoModel,JogoAdmin)


