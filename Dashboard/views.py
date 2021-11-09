from django.http.response import HttpResponse
from django.shortcuts import render
from Travels.models import Travel
from Vehicle.models import Vehicle
from Vehicle.models import Driver
import json
from django.http import JsonResponse

# Create your views here.

def master_dashboard(request):
    active = 'Active'
    travels = Travel.objects.filter(status=active)
    vehicle = Vehicle.objects.filter(status=active)
    driver = Driver.objects.filter(status=active)
    print(travels.count())
    print(vehicle)
    print(driver)
    return json(
        {
        'travel_count': '45',
        })