from django.test import TestCase
from .classes import CalculadoraDiasSumaIniciarInversion, Producto, CalculadoraInversionRequest, CalculadorFechaInversion
from datetime import datetime,timedelta

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
    dias_sumar_sabado = 2
    dias_sumar_domingo = 1
    
    def test_calcular_fecha_inversion_debe_sumar_dias_inicio_inversion_mas_plazo(self):

        # Arrange
        producto1 = Producto(1, 2, 1, 3, 2)
        request = CalculadoraInversionRequest(1, False, 5, datetime(2022, 7, 12, 9, 0, 0))

        # Act
        fecha = CalculadorFechaInversion().calcular_fecha_inversion(producto1, request)
        dias_a_sumar = producto1.dias_fecha_previa_igual  + request.plazo
        # Assert
        self.assertEqual(fecha, request.fechaCreacion + timedelta(days=dias_a_sumar))
        
    def test_calcular_fecha_inversion_fecha_inicio_mas_dias_inicio_cae_sabado_debe_sumar_dias_hasta_proximo_dia_laboral_mas_plazo(self):

        # Arrange
        producto1 = Producto(1, 2, 1, 3, 2)
        request = CalculadoraInversionRequest(1, False,3, datetime(2024, 9, 19, 9, 0, 0))

        # Act
        fecha = CalculadorFechaInversion().calcular_fecha_inversion(producto1, request)
        dias_a_sumar = producto1.dias_fecha_previa_igual + self.dias_sumar_sabado  + request.plazo
        # Assert
        self.assertEqual(fecha, request.fechaCreacion + timedelta(days=dias_a_sumar) )
        
        
    def test_calcular_fecha_inversion_fecha_inicio_mas_dias_inicio_cae_domingo_debe_sumar_dias_hasta_proximo_dia_laboral_mas_plazo(self):

        # Arrange
        producto1 = Producto(1, 2, 1, 3, 2)
        request = CalculadoraInversionRequest(1, False, 3, datetime(2024, 9, 20, 9, 0, 0))

        # Act
        fecha = CalculadorFechaInversion().calcular_fecha_inversion(producto1, request)
        
        dias_a_sumar = producto1.dias_fecha_previa_igual + self.dias_sumar_domingo  + request.plazo
        
        # Assert
        self.assertEqual(fecha, request.fechaCreacion + timedelta(days=dias_a_sumar) )
        
    def test_calcular_fecha_inversion_fecha_fin_mas_plazo_cae_sabado_debe_sumar_dias_hasta_proximo_dia_laboral(self):

        # Arrange
        producto1 = Producto(1, 2, 1, 3, 2)
        request = CalculadoraInversionRequest(1, False, 5, datetime(2024, 9, 19, 9, 0, 0))

        # Act
        fecha = CalculadorFechaInversion().calcular_fecha_inversion(producto1, request)
        
        dias_a_sumar = producto1.dias_fecha_previa_igual + self.dias_sumar_sabado  + request.plazo + self.dias_sumar_sabado
        # Assert
        self.assertEqual(fecha, request.fechaCreacion + timedelta(dias_a_sumar))
        
    def test_calcular_fecha_inversion_fecha_fin_mas_plazo_cae_domingo_debe_sumar_dias_hasta_proximo_dia_laboral(self):

        # Arrange
        producto1 = Producto(1, 2, 1, 3, 2)
        request = CalculadoraInversionRequest(1, False, 6, datetime(2024, 9, 19, 9, 0, 0))

        # Act
        fecha = CalculadorFechaInversion().calcular_fecha_inversion(producto1, request)
        
        dias_a_sumar = producto1.dias_fecha_previa_igual + self.dias_sumar_sabado  + request.plazo + self.dias_sumar_domingo
        # Assert
        self.assertEqual(fecha, request.fechaCreacion + timedelta(dias_a_sumar))
    
        
