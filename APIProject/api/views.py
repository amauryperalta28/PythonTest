from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from .serializers import CalculadoraInversionResponseSerializer, CalculadoraInversionRequestSerializer
from .classes import MyResponse, ProductoDto, CalculadoraInversionRequest, CalculadorFechaInversion, CalculadoraFechaInversionResult
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import UserSerializer
from datetime import datetime
from rest_framework.generics import ListAPIView
from .models import Producto
from .serializers import ProductoSerializer

# Create your views here.

class ProductoListView(ListAPIView):
    queryset = Producto.objects.all()
 
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

class CustomObjectView(APIView):
    def get(self, request):
        serializer = CalculadoraInversionRequestSerializer(data = request.query_params)
        serializer.is_valid(raise_exception=True)
        request_data = serializer.validated_data
        
        producto:int = request_data['producto']
        en_reinversion:bool = request_data['enReinversion']
        plazo:int = request_data['plazo']
        fecha_creacion:str = request_data['fechaCreacion']
        
        fecha_creacion_datetime = datetime.strptime(fecha_creacion, '%Y-%m-%d %H:%M:%S')
        
        producto_db: Producto = Producto.objects.filter(id=producto).first()
        
        if not producto_db:
            return Response({'error': 'Producto no existe'}, status=status.HTTP_404_NOT_FOUND )
       
        producto1 = ProductoDto(producto, 
                                producto_db.dias_fecha_previa_igual, 
                                producto_db.dias_fecha_previa_igual_con_reinversion, 
                                producto_db.dias_horario_posterior_igual, 
                                producto_db.dias_horario_posterior_igual_con_reinversion)
        
        request = CalculadoraInversionRequest(producto, en_reinversion, plazo, fecha_creacion_datetime)
        resultado: CalculadoraFechaInversionResult = CalculadorFechaInversion.calcular_fecha_inversion(None, producto1, request)
        custom_data = MyResponse(
            producto, 
            request.plazo, 
            resultado.fecha_inicio.strftime('%Y-%m-%d'), 
            resultado.fecha_fin.strftime('%Y-%m-%d'), 
            resultado.plazo)

        response_serializer = CalculadoraInversionResponseSerializer(custom_data)

        return Response(response_serializer.data)

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_data_view(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)
    

