from django.contrib import admin
from .models import VehicleDoc,Vehicle, VehicleMaintainance
# Register your models here.


class VehicleAdmin(admin.ModelAdmin):
    list_display = ("model", "ownerShip","carrying_space","carrying_capacity","volume", "vehicle_type", "fuel_type", "permit_type", "status", "Vehicles_Image")

class VehicleMaintainanceAdmin(admin.ModelAdmin):
    list_display = ("last_service", "servicing_days_remaining", "insurance_exp_remaining","insurance_status","puc_exp","puc_exp_remaining", "puc_status", "updated_at")

class VehicleDocAdmin(admin.ModelAdmin):
    list_display = ("owner_name", "owner_phone", "rc_number")

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleDoc, VehicleDocAdmin)
admin.site.register(VehicleMaintainance, VehicleMaintainanceAdmin)
