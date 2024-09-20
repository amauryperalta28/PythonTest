from datetime import datetime


class MyResponse:
    def __init__(self, producto, plazo, fechaInicio, fechaFin, plazoReal):
        self.producto = producto
        self.plazo = plazo
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.plazoReal = plazoReal


class CalculadoraInversionRequest:
    def __init__(self, producto, enReinversion, plazo, fechaCreacion: datetime):
        self.producto = producto
        self.enReinversion = enReinversion
        self.plazo = plazo
        self.fechaCreacion = fechaCreacion


class Producto:
    def __init__(self, id, diasFechaPreviaIgual, diasFechaPreviaIgualConReinversion, diasHorarioPosteriorIgual, diasHorarioPosteriorIgualConReinversion):
        self.id = id
        self.diasFechaPreviaIgual = diasFechaPreviaIgual
        self.diasFechaPreviaIgualConReinversion = diasFechaPreviaIgualConReinversion
        self.diasHorarioPosteriorIgual = diasHorarioPosteriorIgual
        self.diasHorarioPosteriorIgualConReinversion = diasHorarioPosteriorIgualConReinversion


# class CalculadorFechaInversion:

#     def calcula_fecha_inversion(producto: Producto, solicitud: CalculadoraInversionRequest):
#         horarioOperativo = datetime(
#             solicitud.fechaCreacion.year, solicitud.fechaCreacion.month, solicitud.fechaCreacion.day, 10, 30, 0)
#         fechaCreacion = datetime(
#             solicitud.fechaCreacion.year, solicitud.fechaCreacion.month, solicitud.fechaCreacion.day, solicitud.fechaCreacion.hour, solicitud.fechaCreacion.minute, solicitud.fechaCreacion.second)

#         if fechaCreacion <= horarioOperativo:
#             diasAjuste = producto.diasFechaPreviaIgual

#         return ''

class CalculadoraDiasSumaIniciarInversion:
    def calcula_dias(producto: Producto, solicitud: CalculadoraInversionRequest):
        horarioOperativo = datetime(
            solicitud.fechaCreacion.year, solicitud.fechaCreacion.month, solicitud.fechaCreacion.day, 10, 30, 0)
        fechaCreacion = datetime(
            solicitud.fechaCreacion.year, solicitud.fechaCreacion.month, solicitud.fechaCreacion.day, solicitud.fechaCreacion.hour, solicitud.fechaCreacion.minute, solicitud.fechaCreacion.second)

        if solicitud.enReinversion:

          if fechaCreacion <= horarioOperativo:
            return producto.diasFechaPreviaIgualConReinversion
          else:
            return 0

        else:
           if fechaCreacion <= horarioOperativo:
            return producto.diasFechaPreviaIgual
           else:
            return 0
          
      
