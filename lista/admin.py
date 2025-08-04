from django.contrib import admin

from .models import Lista



class ListaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')
    list_per_page = 35
    search_fields = ('nome',)
   

admin.site.register(Lista, ListaAdmin)