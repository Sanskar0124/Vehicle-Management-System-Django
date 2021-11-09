from django.db import models

# choices
DRIVING_TIME = (
    ('Day', 'DAY'),
    ('Night', 'NIGHT'),
    ('Custom', 'CUSTOM'),
)

DRIVER_STATUS = (
    ('Active', 'ACTIVE'),
    ('Engage', 'ENGAGE'),
    ('InActive', 'INACTIVE'),
)

DRIVER_EXPERIENCE = (
    ( '1', 'Less then 1 year'),
    ( '2 - 4', 'Between 2 - 4 Years'),
    ('4 - 6', 'Between 4 - 6 Years'),
    ( '6+','More than 6+ Years'),
)


# Create your models here.
class DriverMsg(models.Model):
    id = models.AutoField
    message = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    time_stamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.status+" - " +self.message

class DriverDoc(models.Model):
    id = models.AutoField
    license_img = models.ImageField(upload_to="driversDocs/images", default="")
    license_no = models.CharField(max_length=15)
    license_exp_date = models.DateField()
    license_status = models.CharField(max_length=15, default="")
    adharCard_img = models.ImageField(upload_to="driversDocs/images", default="")
    adharCard_no = models.CharField(max_length=15)
    panCard_img = models.ImageField(upload_to="driversDocs/images", default="")
    panCard_no = models.CharField(max_length=15)
    marritial_status = models.CharField(max_length=20)
    driver_image = models.ImageField(upload_to="drivers/images", default="")
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.license_no

class Driver(models.Model):
    id = models.AutoField
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone1 = models.IntegerField(default=0)
    phone2 = models.IntegerField(default=0)
    zip_code = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    driving_time = models.CharField(max_length=10, choices=DRIVING_TIME, default='day')
    status = models.CharField(max_length=10, choices=DRIVER_STATUS, default='Active')
    experience = models.CharField(max_length=20, choices=DRIVER_EXPERIENCE, default='2 - 4')
    age = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    start_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    documents = models.ForeignKey(DriverDoc, on_delete=models.CASCADE)
    message = models.ForeignKey(DriverMsg, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name +" "+ self.last_name + " - "+ self.status