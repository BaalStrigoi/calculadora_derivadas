# derivadas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calcular_derivada/', views.calcular_derivada, name='calcular_derivada'),
]
