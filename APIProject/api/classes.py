from datetime import datetime, timedelta
from .models import DiaFeriado

class MyResponse:
    def __init__(self, producto, plazo, fechaInicio, fechaFin, plazoReal):
        self.producto = producto
        self.plazo = plazo
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.plazoReal = plazoReal


class CalculadoraInversionRequest:
    def __init__(self, producto, en_reinversion, plazo, fecha_creacion: datetime):
        self.producto = producto
        self.enReinversion = en_reinversion
        self.plazo = plazo
        self.fechaCreacion = fecha_creacion


class ProductoDto:
    def __init__(self, id, dias_fecha_previa_igual, dias_fecha_previa_igual_con_reinversion, dias_horario_posterior_igual, dias_horario_posterior_igual_con_reinversion):
        self.id = id
        self.dias_fecha_previa_igual = dias_fecha_previa_igual
        self.dias_fecha_previa_igual_con_reinversion = dias_fecha_previa_igual_con_reinversion
        self.dias_horario_posterior_igual = dias_horario_posterior_igual
        self.dias_horario_posterior_igual_con_reinversion = dias_horario_posterior_igual_con_reinversion


class CalculadorFechaInversion:

    def calcular_fecha_inversion(self, producto: ProductoDto, solicitud: CalculadoraInversionRequest):
        SABADO = 5
        DOMINGO = 6
        
        plazo = solicitud.plazo
        
        dias = CalculadoraDiasSumaIniciarInversion.calcula_dias(
            producto, solicitud)
        
        fecha_inicio_inversion = solicitud.fechaCreacion + timedelta(days=dias)
        while fecha_inicio_inversion.weekday() == SABADO or fecha_inicio_inversion.weekday() == DOMINGO or  DiaFeriado.objects.filter(fecha=fecha_inicio_inversion.strftime('%Y-%m-%d')).first():
            fecha_inicio_inversion = fecha_inicio_inversion + timedelta(days=1)
            
        fecha_inversion_final = fecha_inicio_inversion + timedelta(days=solicitud.plazo)
            
        while fecha_inversion_final.weekday() == SABADO or fecha_inversion_final.weekday() == DOMINGO or  DiaFeriado.objects.filter(fecha=fecha_inversion_final.strftime('%Y-%m-%d')).first():
            fecha_inversion_final = fecha_inversion_final + timedelta(days=1)
            plazo = plazo + 1
          
        return CalculadoraFechaInversionResult(fecha_inicio_inversion, fecha_inversion_final, plazo)  
   


class CalculadoraDiasSumaIniciarInversion:
    def calcula_dias(producto: ProductoDto, solicitud: CalculadoraInversionRequest):
        horario_operativo = datetime(
            solicitud.fechaCreacion.year, solicitud.fechaCreacion.month, solicitud.fechaCreacion.day, 10, 30, 0)
        fecha_creacion = datetime(
            solicitud.fechaCreacion.year, solicitud.fechaCreacion.month, solicitud.fechaCreacion.day, solicitud.fechaCreacion.hour, solicitud.fechaCreacion.minute, solicitud.fechaCreacion.second)

        if solicitud.enReinversion:

            if fecha_creacion <= horario_operativo:
                return producto.dias_fecha_previa_igual_con_reinversion
            elif fecha_creacion >= horario_operativo:
                return producto.dias_horario_posterior_igual_con_reinversion
            else:
                return 0

        else:
            if fecha_creacion <= horario_operativo:
                return producto.dias_fecha_previa_igual
            elif fecha_creacion >= horario_operativo:
                return producto.dias_horario_posterior_igual
            else:
                return 0

class CalculadoraFechaInversionResult:
   def __init__(self, fecha_inicio:datetime, fecha_fin:datetime, plazo:int):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.plazo = plazo
        
        
        