from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'cliente'

class ClientType(models.Model):
    customer = models.ForeignKey('Cliente', models.DO_NOTHING)
    client_tier = models.TextField()

    class Meta:
        managed = False
        db_table = 'client_type'
