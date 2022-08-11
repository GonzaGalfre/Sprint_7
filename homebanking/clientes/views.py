from django.shortcuts import render
from .models import Cliente

# Create your views here.
def index(request):
    clients = Cliente.objects.all()
    return render(request, 'clientes/index.html', {'clients':clients})