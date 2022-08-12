from django.shortcuts import render
from .models import Cuenta

def index(request):
    cuentas = Cuenta.objects.all()
    return render(request, 'cuentas/cuentas.html', {'cuentas':cuentas})