from django.contrib import admin
from .models import VehicleDoc,Vehicle, VehicleMaintainance
# Register your models here.


class VehicleAdmin(admin.ModelAdmin):
    list_display = ("model", "ownerShip","rc_number","capacity", "vehicle_type", "fuel_type", "permit_type", "status")

class VehicleMaintainanceAdmin(admin.ModelAdmin):
    list_display = ("last_service", "insurance_exp","insurance_status","puc_exp", "puc_status", "updated_at")

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleDoc)
admin.site.register(VehicleMaintainance, VehicleMaintainanceAdmin)
