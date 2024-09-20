from django.test import TestCase
from .classes import CalculadoraDiasSumaIniciarInversion, Producto, CalculadoraInversionRequest
from datetime import datetime

# Create your tests here.
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
        
          # Arrange
        producto1 = Producto(1,2,1,3,2)
        request = CalculadoraInversionRequest(1, True, 33, datetime(2022, 7, 12, 9,0,0))

         # Act
        resultado = CalculadoraDiasSumaIniciarInversion.calcula_dias(producto1, request)

         # Assert
        self.assertEqual(resultado, producto1.diasFechaPreviaIgualConReinversion)
        
    def test_calcula_dias_fecha_creacion_mayor_o_igual_horario_inicializar_dias_correcto(self):
        
        # Arrange
        producto1 = Producto(1,2,1,3,2)
        request = CalculadoraInversionRequest(1, False, 33, datetime(2022, 7, 12, 12,30,0))

        # Act
        resultado = CalculadoraDiasSumaIniciarInversion.calcula_dias(producto1, request)

        # Assert
        self.assertEqual(resultado, producto1.diasHorarioPosteriorIgual)
        
    def test_calcula_dias_fecha_creacion_mayor_o_igual_con_reinversion_horario_inicializar_dias_correcto(self):
        
         # Arrange
        producto1 = Producto(1,2,1,3,2)
        request = CalculadoraInversionRequest(1, True, 33, datetime(2022, 7, 12, 13,0,0))

         # Act
        resultado = CalculadoraDiasSumaIniciarInversion.calcula_dias(producto1, request)

         # Assert
        self.assertEqual(resultado, producto1.diasHorarioPosteriorIgualConReinversion)
