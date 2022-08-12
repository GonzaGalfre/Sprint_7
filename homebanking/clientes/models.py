from django.db import models

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
