from django.db import models
from django.utils.html import format_html
from datetime import date
from .choices import DRIVING_TIME, DRIVER_STATUS, DRIVER_EXPERIENCE
from .validations import license, adharCard, name, panCard, phoneNumber, zipCode
import datetime 

current_date = date.today()


# Base Class
class Base(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


# Models for drivers.

class DriverNote(Base):
    id = models.AutoField
    message = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.status+" - " +self.message

class DriverDoc(Base):
    id = models.AutoField
    license_img = models.ImageField(upload_to="driversDocs/images", default="")
    license_no = models.CharField(max_length=15, validators=[license])
    license_exp_date = models.DateField()
    license_status = models.CharField(max_length=15, default="")
    adharCard_img = models.ImageField(upload_to="driversDocs/images", default="")
    adharCard_no = models.CharField(max_length=15, validators=[adharCard])
    panCard_img = models.ImageField(upload_to="driversDocs/images", default="")
    panCard_no = models.CharField(max_length=15, validators=[panCard])
    marritial_status = models.CharField(max_length=20)
    driver_image = models.ImageField(upload_to="drivers/images", default="")


    def license_exp_remaining(self):
        datRem = self.license_exp_date - current_date
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
    def driver_name(self):
        name = Driver.first_name
        return name

    def __str__(self):
        return self.license_no


class Driver(Base):
    id = models.AutoField
    first_name = models.CharField(max_length=15, validators=[name])
    last_name = models.CharField(max_length=15, validators=[name])
    phone1 = models.IntegerField(default=0, validators=[phoneNumber])
    phone2 = models.IntegerField(default=0, validators=[phoneNumber])
    email = models.EmailField(max_length=150, default="")
    branch = models.CharField(max_length=15, default="", validators=[name])
    base_location = models.CharField(max_length=15, default="", validators=[name])
    zip_code = models.IntegerField(default=0, validators=[zipCode])
    address = models.CharField(max_length=200)
    driving_time = models.CharField(max_length=20, choices=DRIVING_TIME, default='day')
    status = models.CharField(max_length=10, choices=DRIVER_STATUS, default='Active')
    experience = models.CharField(max_length=20, choices=DRIVER_EXPERIENCE, default='2 - 4')
    date_of_birth = models.DateField(default=datetime.date.today)
    salary = models.IntegerField(default=0)
    documents = models.ForeignKey(DriverDoc, on_delete=models.CASCADE)
    note = models.ForeignKey(DriverNote, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name +" "+ self.last_name + " - "+ self.status