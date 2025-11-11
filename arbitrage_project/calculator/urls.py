from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate_arbitrage, name='calculate_arbitrage'),
]