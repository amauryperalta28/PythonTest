from django.db import models

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    dias_fecha_previa_igual = models.IntegerField()
    dias_fecha_previa_igual_con_reinversion = models.IntegerField()
    dias_horario_posterior_igual = models.IntegerField()
    dias_horario_posterior_igual_con_reinversion = models.IntegerField()

    def __str__(self):
        return f"Producto {self.id}"
    
class DiaFeriado(models.Model):
    descripcion = models.CharField(max_length=60, blank=False, null=False, default='Dia deriado')
    fecha = models.DateField(unique=True)

    def __str__(self):
        return self.fecha.strftime('%Y-%m-%d')