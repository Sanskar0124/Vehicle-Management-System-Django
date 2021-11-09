# Generated by Django 3.2.9 on 2021-11-04 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='license_status',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='insurance_exp',
            field=models.DateField(default='01/10/2001', max_length=15),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='insurance_status',
            field=models.CharField(default='', max_length=15),
        ),
    ]