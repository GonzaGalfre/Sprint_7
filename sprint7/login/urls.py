from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.signup, name='signup'),
    path('login2/', views.login2, name='login2'),
    path('signout/', views.signout, name='signout')
]
