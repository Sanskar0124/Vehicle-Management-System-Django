from django.db import models
from django.db.models.fields import AutoField, DateTimeField, TimeField
from Driver.models import DriverMsg, Driver
from Orders.models import Manifest
import datetime

# Choices
OWNER_SHIP = (
    ('Company', 'COMPANY'),
    ('Joint Tenants', 'JOINT TENANTS'),
    ('Business Partners', 'BUISNESS PARTNERS'),
)

VEHICLE_TYPE = (
    ('Truck', 'TRUCK'),
    ('Mini Truck', 'MNI TRUCK'),
    ('Heavy Truck', 'HEAVY TRUCK'),
    ('Tempo', 'TEMPO'),
    ('Cargo', 'CARGO'),
)

FUEL_TYPE = (
    ('Petrol', 'PETROL'),
    ('Diesel', 'DIESEL'),
    ('CNG', 'CNG'),
    ('Electric', 'ELECTRIC'),
)

PERMIT_TYPE = (
    ('City', 'CITY'),
    ('State', 'STATE'),
    ('National', 'NATIONAL'),
)

VEHICLE_STATUS = (
    ('Active', 'ACTIVE'),
    ('Engage', 'ENGAGE'),
    ('InActive', 'INACTIVE'),
)

# Create your models here.

class VehicleDoc(models.Model):
    id = models.AutoField
    owner_name = models.CharField(max_length=15, default="")
    owner_phone = models.IntegerField(default=0)
    rc_book = models.ImageField(upload_to="vehiclesDocs/images", default="")
    papers_img = models.ImageField(upload_to="vehiclesDocs/images", default="") 
    permit = models.ImageField(upload_to="vehiclesDocs/images", default="") 
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.owner_name

class VehicleMaintainance(models.Model):
    id = models.AutoField
    last_service = models.DateField()
    insurance_exp = models.DateField()
    insurance_status = models.CharField(max_length=15, default="")
    puc_exp = models.DateField()
    puc_status = models.CharField(max_length=15, default="")
    updated_at = models.DateTimeField(auto_now=True)

class Vehicle(models.Model):
    id = models.AutoField
    model = models.CharField(max_length=30)
    ownerShip = models.CharField(max_length=30, choices=OWNER_SHIP, default='Company')
    vehicle_type = models.CharField(max_length=15, choices=VEHICLE_TYPE)
    fuel_type = models.CharField(max_length=15, choices=FUEL_TYPE, default='Diesel')
    permit_type = models.CharField(max_length=15, choices=PERMIT_TYPE, default='State')
    status = models.CharField(max_length=15, choices=VEHICLE_STATUS, default='Active')
    capacity = models.CharField(max_length=15)
    start_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    documents = models.ForeignKey(VehicleDoc, on_delete=models.CASCADE)
    maintainence = models.ForeignKey(VehicleMaintainance, on_delete=models.CASCADE)
    rc_number = models.CharField(max_length=30, default="")
    vehicle_image = models.ImageField(upload_to="vehicles/images", default="")
    def save(self, *args, **kwargs):
        message = "Your vehicle is ready to departure"
        status = "Unseen"
        driverMessage = DriverMsg(message=message, status=status)
        driverMessage.save() 
        super(Vehicle, self).save(*args, **kwargs)
    def __str__(self):
        return self.rc_number+ " - "+ self.status





