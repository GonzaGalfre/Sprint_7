from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse
from tkinter import Widget
import datetime


# Create your views here.

class loanform(forms.Form):
    # loan = forms.IntegerField(required=True)
    # months = forms.DateField(required=False)
    fecha_inicio = forms.DateField(initial=datetime.date.today, widget = forms.HiddenInput())
    PRESTAMO_PERSONAL = "PP"
    PRESTAMO_ESTUDIANTE = "PE"
    PRESTAMO_COMERCIOS = "PC"
    PRESTAMO_HIPOTECARIO= "PH"
    TIPO_PRESTAMO = [
      (PRESTAMO_PERSONAL,"Prestamo personal"),
      (PRESTAMO_COMERCIOS,"Prestamo comercios"),
      (PRESTAMO_HIPOTECARIO, "Prestamo hipotecario"),
    ] 
    valor = forms.IntegerField(label='Total del prestamo',widget=forms.TextInput(attrs={'class': 'form-control'}), required= True)
    tipo_prestamo = forms.CharField(label='Tipo de prestamo',widget=forms.Select(choices=TIPO_PRESTAMO, attrs={'class': 'form-control'}), initial= PRESTAMO_PERSONAL ,required=True)
 


