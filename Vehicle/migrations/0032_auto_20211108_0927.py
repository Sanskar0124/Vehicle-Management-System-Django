# Generated by Django 3.2.9 on 2021-11-08 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle', '0031_alter_vehicle_vehicle_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='vehicle_model',
            new_name='model',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='vehicle_ownerShip',
            new_name='ownerShip',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='vehicle_status',
            new_name='status',
        ),
    ]