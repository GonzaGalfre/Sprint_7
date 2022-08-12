from django.shortcuts import render
from .models import Prestamo

def index(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamos/prestamos.html', {'prestamos':prestamos})