# Generated by Django 4.0.6 on 2022-08-12 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AccountType',
        ),
        migrations.DeleteModel(
            name='AuditoriaCuenta',
        ),
        migrations.DeleteModel(
            name='CardBrand',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='ClientType',
        ),
        migrations.DeleteModel(
            name='Cuenta',
        ),
        migrations.DeleteModel(
            name='Direcciones',
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
        migrations.DeleteModel(
            name='Movimientos',
        ),
        migrations.DeleteModel(
            name='Prestamo',
        ),
        migrations.DeleteModel(
            name='Sucursal',
        ),
        migrations.DeleteModel(
            name='Tarjeta',
        ),
    ]
