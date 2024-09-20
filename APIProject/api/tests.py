from django.test import TestCase
from .classes import CalculadoraDiasSumaIniciarInversion, Producto, CalculadoraInversionRequest
from datetime import datetime

# Create your tests here.

# 1. Cantidad de días a sumar cuando la hora de creación de la inversión es
# menor o igual a la hora operativa: 2 días
# 2. Cantidad de días a sumar cuando la hora de creación de la inversión es
# mayor a la hora operativa: 3 días
# 3. Cantidad de días a sumar cuando la hora de creación de la inversión es
# menor o igual a la hora operativa y es una reinversión: 1 día
# 4. Cantidad de días a sumar cuando la hora de creación de la inversión es
# mayor a la hora operativa y es una reinversión: 2 días
class CalculadorDiasSumaIniciarInversionTests(TestCase):

    def test_calcula_dias_fecha_creacion_menor_o_igual_horario_inicializar_dias_correcto(self):
        
        # Arrange
        producto1 = Producto(1,2,1,3,2)
        request = CalculadoraInversionRequest(1, False, 33, datetime(2022, 7, 12, 9,0,0))

        # Act
        resultado = CalculadoraDiasSumaIniciarInversion.calcula_dias(producto1, request)

        # Assert
        self.assertEqual(resultado, producto1.diasFechaPreviaIgual)
        
    def test_calcula_dias_fecha_creacion_menor_o_igual_con_reinversion_horario_inicializar_dias_correcto(self):
        producto1 = Producto(1,2,1,3,2)
        request = CalculadoraInversionRequest(1, True, 33, datetime(2022, 7, 12, 9,0,0))

        # Llamamos a la función
        resultado = CalculadoraDiasSumaIniciarInversion.calcula_dias(producto1, request)

        # Comparamos el resultado con la fecha esperada
        self.assertEqual(resultado, producto1.diasFechaPreviaIgualConReinversion)
