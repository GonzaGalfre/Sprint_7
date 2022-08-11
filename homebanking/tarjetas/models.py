from django.db import models

# Create your models here.
class AccountType(models.Model):
    customer = models.ForeignKey('Cliente', models.DO_NOTHING)
    account_type_id = models.AutoField(primary_key=True)
    account_tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'account_type'


class AuditoriaCuenta(models.Model):
    old_id = models.IntegerField(blank=True, null=True)
    new_id = models.IntegerField(blank=True, null=True)
    old_balance = models.IntegerField(blank=True, null=True)
    new_balance = models.IntegerField(blank=True, null=True)
    old_iban = models.TextField(blank=True, null=True)
    new_iban = models.TextField(blank=True, null=True)
    old_type = models.TextField(blank=True, null=True)
    new_type = models.TextField(blank=True, null=True)
    user_action = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditoria_cuenta'


class CardBrand(models.Model):
    card_brand_description = models.TextField()
    card_brand_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'card_brand'


class ClientType(models.Model):
    customer = models.ForeignKey('Cliente', models.DO_NOTHING)
    client_tier = models.TextField()
    client_tier_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'client_type'


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        managed = False
        db_table = 'cuenta'


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


class Movimientos(models.Model):
    account = models.ForeignKey(Cuenta, models.DO_NOTHING)
    amount = models.IntegerField()
    transaction_type = models.TextField()
    created_at = models.TextField()

    class Meta:
        managed = False
        db_table = 'movimientos'


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


class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
    card_number = models.IntegerField(unique=True)
    card_cvv = models.IntegerField()
    card_granted_date = models.IntegerField()
    card_expiration_date = models.IntegerField()
    card_brand = models.ForeignKey(CardBrand, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tarjeta'