# Generated by Django 4.1 on 2022-09-02 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
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
                ('client_tier', models.TextField()),
                ('client_tier_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'client_type',
                'managed': False,
            },
        ),
    ]
