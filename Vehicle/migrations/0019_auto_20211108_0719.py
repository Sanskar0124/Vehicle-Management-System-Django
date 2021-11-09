# Generated by Django 3.2.9 on 2021-11-08 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle', '0018_auto_20211107_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='documents',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='message',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='orders',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='vehicle',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='documents',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='maintainence',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='orders',
        ),
        migrations.DeleteModel(
            name='Courier',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='DriverDoc',
        ),
        migrations.DeleteModel(
            name='DriverMsg',
        ),
        migrations.DeleteModel(
            name='Travel',
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
        migrations.DeleteModel(
            name='VehicleDoc',
        ),
        migrations.DeleteModel(
            name='VehicleMaintainance',
        ),
    ]