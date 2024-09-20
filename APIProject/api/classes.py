from datetime import datetime, timedelta


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


class Producto:
    def __init__(self, id, dias_fecha_previa_igual, dias_fecha_previa_igual_con_reinversion, dias_horario_posterior_igual, dias_horario_posterior_igual_con_reinversion):
        self.id = id
        self.dias_fecha_previa_igual = dias_fecha_previa_igual
        self.dias_fecha_previa_igual_con_reinversion = dias_fecha_previa_igual_con_reinversion
        self.dias_horario_posterior_igual = dias_horario_posterior_igual
        self.dias_horario_posterior_igual_con_reinversion = dias_horario_posterior_igual_con_reinversion


class CalculadorFechaInversion:

    def calcular_fecha_inversion(self, producto: Producto, solicitud: CalculadoraInversionRequest):
        SABADO = 5
        DOMINGO = 6
        dias = CalculadoraDiasSumaIniciarInversion.calcula_dias(
            producto, solicitud)
        
        fecha_inversion = solicitud.fechaCreacion + timedelta(days=dias)
        
        if fecha_inversion.weekday() == SABADO:
          return solicitud.fechaCreacion + timedelta(days=dias) + timedelta(days= 2)  + timedelta(days= solicitud.plazo)
        elif fecha_inversion.weekday() == DOMINGO:
          return solicitud.fechaCreacion + timedelta(days=dias) + timedelta(days= 1)  + timedelta(days= solicitud.plazo)
        else:
          return solicitud.fechaCreacion + timedelta(days=dias) + timedelta(days=solicitud.plazo)


class CalculadoraDiasSumaIniciarInversion:
    def calcula_dias(producto: Producto, solicitud: CalculadoraInversionRequest):
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
