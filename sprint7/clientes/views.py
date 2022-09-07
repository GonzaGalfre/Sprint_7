from django.shortcuts import render
from .models import Cliente
from cuentas.models import Cuenta, Movimientos, AccountType
from tarjetas.models import Tarjeta, CardBrand
from django.contrib.auth.decorators import login_required
from .forms import loanform
from django.http import HttpResponse


# Create your views here.

@login_required(login_url='/login/login/')
def index(request):

    
    clientdata = Cliente.objects.get(user_id = request.user.id)
    try:
        accdata = Cuenta.objects.filter(customer_id = clientdata.customer_id)
        accdatalen = len(Cuenta.objects.filter(customer_id = clientdata.customer_id))
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

    if accdatalen <= 1:
        try:
            transactionsdata = [Movimientos.objects.filter(account_id = accdata[0].account_id)]
        except:
            transactionsdata = None
    else:
        transactionsdata = []
        for a in accdata:
            i = Movimientos.objects.filter(account_id = a.account_id)
            transactionsdata.append(i)


    context = {'clientdata':clientdata, 'accdata':accdata, 'cardsdata':cardsdata, 'cbdata':cbdata}
    return render(request, 'clientes/index.html', context)

@login_required(login_url='/login/login/')
def prestamos(request):
    
            
    clientdata = Cliente.objects.get(user_id = request.user.id)
    
    try:
        accdata = Cuenta.objects.filter(customer_id = clientdata.customer_id)
    except:
        accdata = None
        
    try:
        acctype = AccountType.objects.filter(customer_id = clientdata.customer_id)
    except:
        acctype = None
        
    if request.method == 'POST':
        form = loanform(request.POST)
        if form.is_valid():
            loan = form.cleaned_data.get('loan')
            print(loan)
    else: 
        form = loanform()

    context = {'clientdata':clientdata, 'accdata':accdata, 'acctype':acctype, 'form': form}
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


def formulario(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            monto = form.cleaned_data.get('monto')
            
            clientdata = Cliente.objects.get(user_id = request.user.id)

            try:
                accdata = Cuenta.objects.filter(customer_id = clientdata.customer_id)
            except:
                accdata = None

            pass