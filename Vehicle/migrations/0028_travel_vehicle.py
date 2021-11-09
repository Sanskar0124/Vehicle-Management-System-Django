# Generated by Django 3.2.9 on 2021-11-08 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0001_initial'),
        ('Driver', '0001_initial'),
        ('Vehicle', '0027_delete_travel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_ownerShip', models.CharField(max_length=30)),
                ('vehicle_model', models.CharField(max_length=30)),
                ('vehicle_type', models.CharField(max_length=15)),
                ('fuel_type', models.CharField(choices=[('Petrol', 'PETROL'), ('Diesel', 'DIESEL'), ('CNG', 'CNG'), ('Electric', 'ELECTRIC')], default='Diesel', max_length=15)),
                ('permit_type', models.CharField(max_length=15)),
                ('vehicle_status', models.CharField(max_length=15)),
                ('capacity', models.CharField(max_length=15)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rc_number', models.CharField(default='', max_length=30)),
                ('vehicle_image', models.ImageField(default='', upload_to='vehicles/images')),
                ('documents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicle.vehicledoc')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Driver.driver')),
                ('maintainence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicle.vehiclemaintainance')),
                ('manifest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.manifest')),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=15)),
                ('departure_time', models.CharField(max_length=15)),
                ('departure_loc', models.CharField(max_length=15)),
                ('destination', models.CharField(max_length=15)),
                ('estimated_time', models.CharField(max_length=15)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Driver.driver')),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.manifest')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicle.vehicle')),
            ],
        ),
    ]
