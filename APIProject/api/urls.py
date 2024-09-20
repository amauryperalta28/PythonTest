
from django.urls import path, include
from .views import CustomObjectView


urlpatterns = [
    path('api/responses/', CustomObjectView.as_view(), name='responses'),
]