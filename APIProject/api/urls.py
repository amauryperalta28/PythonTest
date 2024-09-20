
from django.urls import path, include
from .views import CustomObjectView
from .views import ProductoListView

urlpatterns = [
    path('api/responses/', CustomObjectView.as_view(), name='responses'),
    path('productos/', ProductoListView.as_view(), name='producto-list'),
]