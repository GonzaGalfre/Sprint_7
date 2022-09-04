# Generated by Django 4.1 on 2022-08-15 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.TextField()),
                ('customer_surname', models.TextField()),
                ('customer_dni', models.TextField(db_column='customer_DNI')),
                ('dob', models.TextField(blank=True, null=True)),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClientType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_tier', models.TextField()),
            ],
            options={
                'db_table': 'client_type',
                'managed': False,
            },
        ),
    ]
