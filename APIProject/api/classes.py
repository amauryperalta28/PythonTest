class MyResponse:
    def __init__(self, producto, plazo, fechaInicio, fechaFin, plazoReal):
        self.producto = producto
        self.plazo = plazo
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.plazoReal = plazoReal
        
class MyRequest:
  def __init__(self, producto, enReinversion, plazo, fechaCreacion):
    self.producto = producto
    self.enReinversion = enReinversion
    self.plazo = plazo
    self.fechaCreacion = fechaCreacion
