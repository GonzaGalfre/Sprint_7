from django.urls import path, include
from . import views

app_name = 'formulario'
urlpatterns = [
    path('', views.index, name='index'),

]