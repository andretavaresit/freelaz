from django.contrib import admin

# Register your models here.

from .models import Listing

class ListAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','owner','categoria','preco','is_published','list_date')
    list_display_links = ('id','titulo')
    list_filter = ('categoria',)
    search_field = ('titulo','descricao','endereco','cidade','cep','estado','preco')
    list_editable = ('is_published',)
    list_per_page = 30
admin.site.register(Listing,ListAdmin)
