from django.contrib import admin
from .models import Travel, Routes

# Register your models here.


class TravelAdmin(admin.ModelAdmin):
    list_display = ("manifest", "vehicle", "driver", "updated_at" ,"departure_loc", "destination", "status")

admin.site.register(Travel, TravelAdmin)
admin.site.register(Routes)