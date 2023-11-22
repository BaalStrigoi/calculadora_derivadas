from django.contrib import admin
from django.urls import path, include
from derivadas import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    #path('calcular_derivada/', views.calcular_derivada, name='calcular_derivada')
    path('derivadas/', include('derivadas.urls')),

]
