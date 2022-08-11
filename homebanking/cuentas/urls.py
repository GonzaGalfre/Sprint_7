from django.urls import path, include
from . import views

app_name = 'cuentas'
urlpatterns = [
    path('', views.index, name='index'),

]