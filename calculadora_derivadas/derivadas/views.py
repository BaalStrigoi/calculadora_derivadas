from django.shortcuts import render
from sympy import symbols, diff

def index(request):
    return render(request, 'derivadas/index.html')

def calcular_derivada(request):
    if request.method == 'POST':
        funcion = request.POST.get('funcion', '')
        x = symbols('x')
        derivada = diff(funcion, x)
        return render(request, 'derivadas/index.html', {'funcion': funcion, 'derivada': derivada})
    else:
        return render(request, 'derivadas/index.html')

