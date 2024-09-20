from django.test import TestCase
from .classes import CalculadoraDiasSumaIniciarInversion, Producto, CalculadoraInversionRequest, CalculadorFechaInversion
from datetime import datetime

# Create your tests here.


class CalculadorDiasSumaIniciarInversionTests(TestCase):

    def test_calcula_dias_fecha_creacion_menor_o_igual_horario_inicializar_dias_correcto(self):

        # Arrange
        producto1 = Producto(1, 2, 1, 3, 2)
        request = CalculadoraInversionRequest(
            1, False, 33, datetime(2022, 7, 12, 9, 0, 0))

        # Act
        resultado = CalculadoraDiasSumaIniciarInversion.calcula_dias(
            producto1, request)

        # Assert
        self.assertEqual(resultado, producto1.dias_fecha_previa_igual)

    def test_calcula_dias_fecha_creacion_menor_o_igual_con_reinversion_horario_inicializar_dias_correcto(self):

        # Arrange
        producto1 = Producto(1, 2, 1, 3, 2)
        request = CalculadoraInversionRequest(
            1, True, 33, datetime(2022, 7, 12, 9, 0, 0))

        # Act
        resultado = CalculadoraDiasSumaIniciarInversion.calcula_dias(
            producto1, request)

        # Assert
        self.assertEqual(
            resultado, producto1.dias_fecha_previa_igual_con_reinversion)

    def test_calcula_dias_fecha_creacion_mayor_o_igual_horario_inicializar_dias_correcto(self):

        # Arrange
        producto1 = Producto(1, 2, 1, 3, 2)
        request = CalculadoraInversionRequest(
            1, False, 33, datetime(2022, 7, 12, 12, 30, 0))

        # Act
        resultado = CalculadoraDiasSumaIniciarInversion.calcula_dias(
            producto1, request)

        # Assert
        self.assertEqual(resultado, producto1.dias_horario_posterior_igual)

    def test_calcula_dias_fecha_creacion_mayor_o_igual_con_reinversion_horario_inicializar_dias_correcto(self):

        # Arrange
        producto1 = Producto(1, 2, 1, 3, 2)
        request = CalculadoraInversionRequest(
            1, True, 33, datetime(2022, 7, 12, 13, 0, 0))

        # Act
        resultado = CalculadoraDiasSumaIniciarInversion.calcula_dias(
            producto1, request)

        # Assert
        self.assertEqual(
            resultado, producto1.dias_horario_posterior_igual_con_reinversion)


class CalculadorFechaInversionTests(TestCase):
    def test_calcula_fecha_inversion_debe_sumar_dias_inicio_inversion_mas_plazo(self):

        # Arrange
        producto1 = Producto(1, 2, 1, 3, 2)
        request = CalculadoraInversionRequest(1, False, 5, datetime(2022, 7, 12, 9, 0, 0))

        # Act
        fecha = CalculadorFechaInversion().calcula_fecha_inversion(producto1, request)
        
        # Assert
        self.assertEqual(fecha.day, request.fechaCreacion.day + request.plazo + producto1.dias_fecha_previa_igual)
        
        
