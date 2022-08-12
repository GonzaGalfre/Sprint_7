from django.shortcuts import render
from .models import Tarjeta

def index(request):
    tarjetas = Tarjeta.objects.all()
    return render(request, 'tarjetas/tarjetas.html', {'tarjetas':tarjetas})