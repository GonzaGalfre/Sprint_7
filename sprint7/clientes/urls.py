from django.urls import path, include
from . import views

app_name = 'clientes'
urlpatterns = [
    path('', views.inicio, name ='inicio'),
    path('resumen/', views.index, name='index'),
    path('prestamos/', views.prestamos, name='prestamos'),
]