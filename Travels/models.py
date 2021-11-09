from django.db import models
from Orders.models import Manifest
from Vehicle.models import Vehicle
from Driver.models import Driver

#Choices
TRAVEL_STATUS = (
    ('Active', 'ACTIVE'),
    ('Delivered', 'DELIVERED'),
    ('Cancelled', 'CANCELLED'),
)

# Create your models here.

class Routes(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=15)
    destination_1 = models.CharField(max_length=15)
    destination_2 = models.CharField(max_length=15)
    destination_3 = models.CharField(max_length=15)
    destination_4 = models.CharField(max_length=15)
    destination_5 = models.CharField(max_length=15)
    destination_6 = models.CharField(max_length=15)
    destination_7 = models.CharField(max_length=15)
    destination_8 = models.CharField(max_length=15)
    destination_9 = models.CharField(max_length=15)
    destination_10 = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Travel(models.Model):
    id = models.AutoField
    manifest = models.ForeignKey(Manifest, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    routes = models.ForeignKey(Routes, on_delete=models.CASCADE)
    location = models.CharField(max_length=15)
    departure_time = models.CharField(max_length=15)
    departure_loc = models.CharField(max_length=15)
    destination = models.CharField(max_length=15)
    estimated_time = models.CharField(max_length=15)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, choices=TRAVEL_STATUS, default='Ready to deliver')
    def __str__(self):
        return self.departure_loc+" to " +self.destination



