from django.shortcuts import render
from clientes.models import Cliente
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
#Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user_dni = form.cleaned_data.get('dni')
            cliente = Cliente.objects.filter(customer_dni = user_dni)
            if cliente != None:
                form.save()
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect(reverse('clientes:index'))

            
            
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

