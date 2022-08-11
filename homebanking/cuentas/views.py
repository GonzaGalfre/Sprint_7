from django.shortcuts import render
from .models import Cuenta

# Create your views here.
def index(request):
    cuentas = Cuenta.objects.all()
    return render(request, 'cuentas/index.html', {'cuentas':cuentas})