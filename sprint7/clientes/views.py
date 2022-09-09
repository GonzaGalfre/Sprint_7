from turtle import update
from django.shortcuts import render
from .models import Cliente
from cuentas.models import Cuenta, Movimientos, AccountType
from tarjetas.models import Tarjeta, CardBrand
from django.contrib.auth.decorators import login_required
from .forms import loanform
from django.http import HttpResponse
from django.db import connection
from django.contrib import messages
from datetime import datetime


# Create your views here.

@login_required(login_url='/login/login/')
def index(request):

    
    clientdata = Cliente.objects.get(user_id = request.user.id)
    try:
        accdata = Cuenta.objects.filter(customer_id = clientdata.customer_id)
    except:
        accdata = None

    try:
        cardsdata = Tarjeta.objects.filter(customer_id = clientdata.customer_id)
    except:
        cardsdata = None

    try:
        cbdata = CardBrand.objects.filter(card_brand_id = cardsdata.card_brand_id)
    except:
        cbdata = None

    try:
        transactionsdata = Movimientos.objects.filter(account = accdata[0].account_id)
    except:
        transactionsdata = None
    print(transactionsdata)


    context = {'clientdata':clientdata, 'accdata':accdata, 'cardsdata':cardsdata, 'cbdata':cbdata, 'transactionsdata':transactionsdata}
    return render(request, 'clientes/index.html', context)

@login_required(login_url='/login/login/')
def prestamos(request):
    
    form = loanform()
    today = datetime.now()
    hour = today.strftime('%H:%M:%S')
    clientdata = Cliente.objects.get(user_id = request.user.id)
    
    try:
        accdata = Cuenta.objects.filter(customer_id = clientdata.customer_id)
    except:
        accdata = None
        
    try:
        acctype = AccountType.objects.filter(customer_id = clientdata.customer_id)
    except:
        acctype = None
        
    context = {'clientdata':clientdata, 'accdata':accdata, 'acctype':acctype, 'form': form}
    if request.method == 'POST':
        form = loanform(request.POST)
        if form.is_valid():
            loan = int(request.POST.get('valor')) * 100
            print(loan)
            acc_id = accdata[0].account_id

            if acctype[0].account_tipo == "Classic":
                if loan < 10000000:
                    with connection.cursor() as cursor:
                        cursor.execute("UPDATE cuenta SET balance = balance + %s WHERE account_id = %s", [loan, acc_id])
                        cursor.execute("INSERT INTO movimientos(account_id, amount, transaction_type, created_at) VALUES(%s, %s, 'Prestamo', %s)", [acc_id,loan,hour])
                    messages.success(request, 'Prestamo acreditado correctamente')
                    return render(request, 'clientes/prestamos.html', context)
                else:
                    messages.error(request, 'Los clientes Classic solo pueden pedir hasta $100.000')
                    return render(request, 'clientes/prestamos.html', context)
            
            if acctype[0].account_tipo == "Gold":
                if loan < 30000000:
                    with connection.cursor() as cursor:
                        cursor.execute("UPDATE cuenta SET balance = balance + %s WHERE account_id = %s", [loan, acc_id])
                        cursor.execute("INSERT INTO movimientos(account_id, amount, transaction_type, created_at) VALUES(%s, %s, 'Prestamo', %s)", [acc_id,loan,hour])
                    messages.success(request, 'Prestamo acreditado correctamente')
                    return render(request, 'clientes/prestamos.html', context)
                else:
                    messages.error(request, 'Los clientes Gold solo pueden pedir hasta $300.000')
                    return render(request, 'clientes/prestamos.html', context)   
                
            if acctype[0].account_tipo == "Black":
                if loan < 50000000:
                    with connection.cursor() as cursor:
                        cursor.execute("UPDATE cuenta SET balance = balance + %s WHERE account_id = %s", [loan, acc_id])
                        cursor.execute("INSERT INTO movimientos(account_id, amount, transaction_type, created_at) VALUES(%s, %s, 'Prestamo', %s)", [acc_id,loan,hour])
                    messages.info(request, 'Prestamo acreditado correctamente')
                    return render(request, 'clientes/prestamos.html', context)
                else:
                    messages.error(request, 'Los clientes Black solo pueden pedir hasta $500.000')
                    return render(request, 'clientes/prestamos.html', context)
            
                
  
            
    else: 
        form = loanform()

    
    return render(request, 'clientes/prestamos.html', context)

@login_required(login_url='/login/login/')
def cotizaciones(request):
    clientdata = Cliente.objects.get(user_id = request.user.id)

    try:
        accdata = Cuenta.objects.filter(customer_id = clientdata.customer_id)
    except:
        accdata = None

    context = {'clientdata':clientdata, 'accdata':accdata}
    return render(request, 'clientes/cotizaciones.html', context)


