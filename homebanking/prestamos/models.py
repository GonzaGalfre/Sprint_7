from django.db import models
from clientes.models import Cliente
# Create your models here.

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'

class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'

class Direcciones(models.Model):
    adress_id = models.AutoField(primary_key=True)
    adress_street = models.TextField()
    adress_city = models.TextField()
    customer = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey('Empleado', models.DO_NOTHING, blank=True, null=True)
    branch = models.ForeignKey('Sucursal', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direcciones'

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'