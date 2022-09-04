from django.urls import path
from . import views as core_views

app_name = 'login'
urlpatterns = [
    path('signup/', core_views.signup, name='signup'),
]
