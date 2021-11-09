from django.contrib import admin
from .models import VehicleDoc,Vehicle, VehicleMaintainance
# Register your models here.


class VehicleAdmin(admin.ModelAdmin):
    list_display = ("model", "ownerShip","rc_number","capacity", "vehicle_type", "fuel_type", "permit_type", "status")

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleDoc)
admin.site.register(VehicleMaintainance)
