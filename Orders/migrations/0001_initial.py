# Generated by Django 3.2.6 on 2021-11-14 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manifest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sender', models.CharField(max_length=30)),
                ('reciver', models.CharField(max_length=30)),
                ('total_items', models.CharField(max_length=30)),
                ('total_ammount', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=30)),
                ('payment_mode', models.CharField(max_length=10)),
                ('payment_status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
    ]
