from django.contrib import admin
from .models import Driver, DriverNote, DriverDoc


class DriverAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone1","status","driving_time", "salary", "documents")

class DriverDocAdmin(admin.ModelAdmin):
    list_display = ( "license_no", "license_exp_date", "license_exp_remaining", "license_status","drivers_image")
    readonly_fields = ('drivers_image',)

# Register your models here.
admin.site.register(Driver, DriverAdmin)
admin.site.register(DriverNote)
admin.site.register(DriverDoc, DriverDocAdmin)