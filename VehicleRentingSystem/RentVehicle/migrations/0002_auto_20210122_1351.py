# Generated by Django 3.0.4 on 2021-01-22 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentVehicle', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentvehicle',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='rentvehicle',
            name='manager_authorized_id',
        ),
        migrations.RemoveField(
            model_name='rentvehicle',
            name='owner_authorized_id',
        ),
        migrations.RemoveField(
            model_name='rentvehicle',
            name='vehicle_id',
        ),
    ]