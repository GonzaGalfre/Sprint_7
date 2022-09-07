from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse


# Create your views here.

class loanform(forms.Form):
    loan = forms.IntegerField(required=True)
    months = forms.DateField(required=False)
