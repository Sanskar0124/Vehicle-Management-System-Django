from django.db import models
from django.db.models.fields import AutoField, DateTimeField, TimeField
from Driver.models import DriverNote, Driver, Base
from Orders.models import Manifest
from django.utils.html import format_html

from validation import name, phoneNumber, policyNumber, pucNumber
from .choices import OWNER_SHIP, VEHICLE_TYPE, FUEL_TYPE, PERMIT_TYPE, VEHICLE_STATUS
from datetime import date

current_date = date.today()


# Create your models here.

class VehicleDoc(Base):
    id = models.AutoField
    owner_name = models.CharField(max_length=15, default="", validators=[name])
    owner_phone = models.IntegerField(default=0, validators=[phoneNumber])
    rc_book = models.ImageField(upload_to="vehiclesDocs/images", default="")
    papers_img = models.ImageField(upload_to="vehiclesDocs/images", default="") 
    permit = models.ImageField(upload_to="vehiclesDocs/images", default="")

    def __str__(self):
        return self.owner_name

class VehicleMaintainance(Base):
    id = models.AutoField
    last_service = models.DateField()
    insurance_policy_no = models.CharField(max_length=12, validators=[policyNumber])
    insurance_exp = models.DateField()
    insurance_status = models.CharField(max_length=15, default="")
    puc_no = models.CharField(max_length=12, validators=[pucNumber])
    puc_exp = models.DateField()
    puc_status = models.CharField(max_length=15, default="")

    def insurance_exp_remaining(self):
        datRem = self.insurance_exp - current_date
        strDate = str(datRem).split()
        intDate = int(strDate[0])
        if(intDate < 30):
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                str(intDate) + " Days remaining",
                )
        if(intDate < 60):
            return format_html(
                '<span style="color: {};">{}</span>',
                "orange",
                str(intDate) + " Days remaining",
                )

    # def servicing_days_remaining(self):
    #     datRem = self.last_service - current_date
    #     strDate = str(datRem).split()
    #     intDate = int(strDate[0])
    #     return format_html(
    #         '<span style="color: {};">{}</span>',
    #         "red",
    #         str(intDate) + " Days remaining",
    #         )


    def puc_exp_remaining(self):
        datRem = self.puc_exp - current_date
        strDate = str(datRem).split()
        intDate = int(strDate[0])
        if(intDate < 30):
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                str(intDate) + " Days remaining",
                )
        if(intDate < 60):
            return format_html(
                '<span style="color: {};">{}</span>',
                "orange",
                str(intDate) + " Days remaining",
                )



    @property
    def servicing_days_remaining(self):
        datRem = self.last_service - current_date
        return datRem



class Vehicle(Base):
    id = models.AutoField
    model = models.CharField(max_length=30)
    ownerShip = models.CharField(max_length=30, choices=OWNER_SHIP, default='Company')
    vehicle_type = models.CharField(max_length=15, choices=VEHICLE_TYPE)
    fuel_type = models.CharField(max_length=15, choices=FUEL_TYPE, default='Diesel')
    permit_type = models.CharField(max_length=15, choices=PERMIT_TYPE, default='State')
    status = models.CharField(max_length=15, choices=VEHICLE_STATUS, default='Active')
    carrying_capacity = models.CharField(max_length=15, default="")
    carrying_space = models.CharField(max_length=15, default="")
    length = models.FloatField(default=0)
    breadth = models.FloatField(default=0)
    height = models.FloatField(default=0)
    volume = models.FloatField(default=0)
    documents = models.ForeignKey(VehicleDoc, on_delete=models.CASCADE)
    maintainence = models.ForeignKey(VehicleMaintainance, on_delete=models.CASCADE)
    rc_number = models.CharField(max_length=30, default="")
    vehicle_image = models.ImageField(upload_to="vehicles/images", default="")
    def save(self, *args, **kwargs):
        message = "Your vehicle is ready to departure"
        status = "Unseen"
        driverMessage = DriverNote(message=message, status=status)
        driverMessage.save() 
        super(Vehicle, self).save(*args, **kwargs)
    def __str__(self):
        return self.rc_number+ " - "+ self.status





