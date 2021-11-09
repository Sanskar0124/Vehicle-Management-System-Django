from django.contrib import admin
from .models import Driver, DriverMsg, DriverDoc


class DriverAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone1","status","driving_time", "salary", "documents")

# Register your models here.
admin.site.register(Driver, DriverAdmin)
admin.site.register(DriverMsg)
admin.site.register(DriverDoc)