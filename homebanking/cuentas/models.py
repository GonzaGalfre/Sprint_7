from django.db import models
from clientes.models import Cliente

# Create your models here.
class AccountType(models.Model):
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
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

class Cuenta(models.Model):
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()

    class Meta:
        managed = False
        db_table = 'cuenta'

class Movimientos(models.Model):
    account = models.ForeignKey(Cuenta, models.DO_NOTHING)
    amount = models.IntegerField()
    transaction_type = models.TextField()
    created_at = models.TextField()

    class Meta:
        managed = False
        db_table = 'movimientos'
