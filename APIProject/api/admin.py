from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Producto, DiaFeriado

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'dias_fecha_previa_igual', 'dias_fecha_previa_igual_con_reinversion', 'dias_horario_posterior_igual', 'dias_horario_posterior_igual_con_reinversion')
    search_fields = ('id',)
    list_filter = ('dias_fecha_previa_igual', 'dias_fecha_previa_igual_con_reinversion')
    
@admin.register(DiaFeriado)
class DiaFeriadoAdmin(admin.ModelAdmin):
    list_display = ('fecha',)
    search_fields = ('fecha',)
    list_filter = ('fecha',)

