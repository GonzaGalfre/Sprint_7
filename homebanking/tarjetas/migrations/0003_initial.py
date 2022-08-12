# Generated by Django 4.0.6 on 2022-08-12 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tarjetas', '0002_delete_accounttype_delete_auditoriacuenta_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardBrand',
            fields=[
                ('card_brand_description', models.TextField()),
                ('card_brand_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'card_brand',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('card_id', models.AutoField(primary_key=True, serialize=False)),
                ('card_number', models.IntegerField(unique=True)),
                ('card_cvv', models.IntegerField()),
                ('card_granted_date', models.IntegerField()),
                ('card_expiration_date', models.IntegerField()),
            ],
            options={
                'db_table': 'tarjeta',
                'managed': False,
            },
        ),
    ]
