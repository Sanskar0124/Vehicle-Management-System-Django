from django.db import models

# Create your models here.
class Order(models.Model):
    id = models.AutoField
    items = models.CharField(max_length=100)
    state = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    address = models.CharField(max_length=150)

class Manifest(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=30)
    sender = models.CharField(max_length=30)
    reciver = models.CharField(max_length=30)
    total_items = models.CharField(max_length=30)
    total_ammount = models.IntegerField(default=0)
    status = models.CharField(max_length=30)
    payment_mode= models.CharField(max_length=10)
    payment_status = models.CharField(max_length=10)
    def __str__(self):
        return self.name