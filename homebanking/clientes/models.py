from django.db import models

# Create your models here.

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

class ClientType(models.Model):
    customer = models.ForeignKey('Cliente', models.DO_NOTHING)
    client_tier = models.TextField()
    client_tier_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'client_type'
