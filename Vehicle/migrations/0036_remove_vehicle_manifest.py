# Generated by Django 3.2.9 on 2021-11-08 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle', '0035_remove_vehicle_driver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='manifest',
        ),
    ]
