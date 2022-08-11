from django.urls import path, include
from . import views

app_name = 'tarjetas'
urlpatterns = [
    path('', views.index, name='index'),

]