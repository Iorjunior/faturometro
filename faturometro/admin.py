from django.contrib import admin
from .models import Venda


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_per_page = 20
