from django.shortcuts import render
from .models import Cliente


def index(request):
    # clients = Cliente.objects.all()
    return render(request, 'clientes/index.html')