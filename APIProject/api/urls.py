
from django.urls import path, include
from .views import CustomObjectView, ProductoListView, login_view, user_data_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/fechas-inversion/', CustomObjectView.as_view(), name='fechas-inversion'),
    path('productos/', ProductoListView.as_view(), name='producto-list'),
    path('login/', login_view, name='login'),
    path('user/', user_data_view, name='user-data'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
