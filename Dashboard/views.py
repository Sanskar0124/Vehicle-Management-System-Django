from django.http.response import HttpResponse
from django.shortcuts import render
from Driver.models import DriverDoc
from Travels.models import Travel
from Vehicle.models import Vehicle, VehicleMaintainance
from Vehicle.models import Driver
from django.http import JsonResponse
from datetime import date

# Create your views here.

current_date = date.today()

def master_dashboard(request):
    # Cards Count
    active = 'Active'
    travels = Travel.objects.filter(status=active)
    vehicle = Vehicle.objects.filter(status=active)
    driver = Driver.objects.filter(status=active)
    # print(travels.count())
    # print(vehicle.count())
    # print(driver.count())

    # Arrays For Counting
    insuranceExpiry = []
    pucExpiry = []
    needServicing = []
    licenseExpiry = []

    # Vehicle Maintainance
    vehicleMaintainance = VehicleMaintainance.objects.all()

    # Insurance Expiry
    for i in vehicleMaintainance:
        # Insurance Expiry
        insDate = i.insurance_exp
        insRemainingDays =  insDate - current_date
        # print(remainingDays)
        strDate = str(insRemainingDays).split()
        intDate = int(strDate[0])
        if(intDate < 30):
            insuranceExpiry.append(insDate)
            print("red")
        elif(intDate < 60):
            insuranceExpiry.append(insDate)
            print("orange")
    # print(len(insuranceExpiry))

    # Puc Expiry
    for i in vehicleMaintainance:
        pucDate = i.puc_exp
        pucRemainingDays =  pucDate - current_date
        # print(pucRemainingDays)
        strDate = str(pucRemainingDays).split()
        intDate = int(strDate[0])
        if(intDate < 30):
            pucExpiry.append(pucDate)
            print("pucRed")
        elif(intDate < 60):
            pucExpiry.append(pucDate)
            print("pucOrange")

    # Servicing
    for i in vehicleMaintainance:
        serviceDate = i.last_service
        serviceRemainingDays = serviceDate  - current_date
        # print(serviceRemainingDays)
        strDate = str(serviceRemainingDays).split()
        intDate = int(strDate[0])
        if(intDate < 90):
            needServicing.append(serviceDate)
            print("Need Servicing")

    # License Expiry
    driverDocs = DriverDoc.objects.all()
    for i in driverDocs:
        licDate = i.license_exp_date
        licRemainingDays =  licDate - current_date
        # print(pucRemainingDays)
        strDate = str(licRemainingDays).split()
        intDate = int(strDate[0])
        if(intDate < 30):
            licenseExpiry.append(licDate)
            print("licRed")
        elif(intDate < 60):
            licenseExpiry.append(licDate)
            print("licOrange")
            
    # print(len(pucExpiry))
    return JsonResponse({'data': {
        "active_travels" : travels.count(),
        "active_vehicles" : vehicle.count(),
        "active_drivers" : driver.count(),
        "insurance_exp" : len(insuranceExpiry),
        "puc_exp" : len(pucExpiry),
        "need_servicing" : len(needServicing),
        "license_exp" : len(licenseExpiry),
    }})