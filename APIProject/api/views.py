from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from .serializers import CalculadoraInversionResponseSerializer, CalculadoraInversionRequestSerializer
from .classes import MyResponse, Producto
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Create your views here.

from rest_framework.generics import ListAPIView
from .models import Producto
from .serializers import ProductoSerializer


class ProductoListView(ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

class CustomObjectView(APIView):
    def get(self, request):
        serializer = CalculadoraInversionRequestSerializer(data = request.query_params)
        serializer.is_valid(raise_exception=True)
        requestData = serializer.validated_data
        
        producto = requestData['producto']
        enReinversion = requestData['enReinversion']
        plazo = requestData['plazo']
        fecha_creacion = requestData['fechaCreacion']
        
        producto1 = Producto(1,2,1,3,2)
        
        custom_data = MyResponse(
            1, 
            33, 
            "2022-07-14 00:00:00", 
            "2022-08-17 00:00:00", 
            34)

        # Serialize the data
        response_serializer = CalculadoraInversionResponseSerializer(custom_data)

        # Return the serialized data as a response
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
    

