from django.contrib import admin
from .models import VehicleDoc,Vehicle, VehicleMaintainance
# Register your models here.


class VehicleAdmin(admin.ModelAdmin):
    list_display = ("model", "ownerShip","rc_number","carrying_space", "vehicle_type", "fuel_type", "permit_type", "status")
#     {
# 'fields': (('first_name', 'last_name'), 'address', 'city', 'state'),
# }

class VehicleMaintainanceAdmin(admin.ModelAdmin):
    list_display = ("last_service", "servicing_days_remaining", "insurance_exp_remaining","insurance_status","puc_exp","puc_exp_remaining", "puc_status", "updated_at")
    # def highlight_expirydate(self, obj):
    #     print(self.insurance_exp_remaining)
    #     print("Helllooooooooooooooooo")
    #     if(self.insurance_exp_remaining < 60):
    #         return "<span style='color:red'>obj.insurance_exp_remaining</span>"

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleDoc)
admin.site.register(VehicleMaintainance, VehicleMaintainanceAdmin)
