# Generated by Django 3.2.9 on 2021-11-04 09:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Vehicle', '0010_auto_20211104_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sender_name', models.CharField(max_length=30)),
                ('reciver_name', models.CharField(max_length=30)),
                ('total_items', models.CharField(max_length=30)),
                ('total_ammount', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=30)),
                ('payment_mode', models.CharField(max_length=10)),
                ('payment_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DriverMsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=20)),
                ('time_stamp', models.DateTimeField(verbose_name=datetime.time(9, 16, 1, 379013))),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=30)),
                ('rc_number', models.CharField(default='', max_length=30)),
                ('owner_fir_name', models.CharField(max_length=15)),
                ('owner_sec_name', models.CharField(max_length=15)),
                ('owner_phone', models.IntegerField(default=0)),
                ('cost_per_km', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('registration_plate', models.CharField(max_length=15)),
                ('vehicle_status', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=25)),
                ('speed', models.CharField(max_length=15)),
                ('insurance_exp', models.DateField()),
                ('insurance_status', models.CharField(default='', max_length=15)),
                ('puc_exp', models.DateField()),
                ('puc_status', models.CharField(default='', max_length=15)),
                ('no_of_km_travelled', models.IntegerField(default=0)),
                ('fuel_type', models.CharField(max_length=15)),
                ('mileage', models.IntegerField(default=0)),
                ('vehicle_type', models.CharField(max_length=15)),
                ('capacity', models.CharField(max_length=15)),
                ('departure', models.CharField(max_length=15)),
                ('departure_time', models.CharField(max_length=15)),
                ('destination', models.CharField(max_length=15)),
                ('kilometers', models.CharField(max_length=15)),
                ('estimated_time', models.CharField(max_length=15)),
                ('vehicle_image', models.ImageField(default='', upload_to='vehicles/images')),
                ('courier_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicle.courier')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('phone1', models.IntegerField(default=0)),
                ('phone2', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=0)),
                ('experience', models.CharField(max_length=20)),
                ('license_no', models.CharField(max_length=15)),
                ('license_exp_date', models.DateField()),
                ('license_status', models.CharField(default='', max_length=15)),
                ('marritial_status', models.CharField(max_length=20)),
                ('salary', models.IntegerField(default=0)),
                ('driver_image', models.ImageField(default='', upload_to='drivers/images')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicle.drivermsg')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicle.vehicle')),
            ],
        ),
    ]
