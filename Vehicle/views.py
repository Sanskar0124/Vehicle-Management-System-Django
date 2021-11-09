from django.http.response import HttpResponse
from django.shortcuts import render
# from .models import Order, Vehicle

# Create your views here.
def index(request):
    return render(request,'vehicle/home.html')

# def orders(request):
#     allOrders = []
#     stateOrder = Order.objects.values('state', 'id')
#     # print(stateOrder)
#     states = {item['state'] for item in stateOrder}
#     # print(states)
#     for sta in states:
#         ord = Order.objects.filter(state=sta)
#         # print(ord)
#         allOrders.append(ord)
#         print(type(ord))
#         # print(allOrders)
#     params = {'allOrders' : allOrders}
#     return render(request,'vehicle/orders.html', params)

# def ordersInVehicle(request):
#     allVehicles = []
#     statVehicle = Vehicle.objects.values('vehicle_status', 'id')
#     # print(statVehicle)
#     statuses = {item['vehicle_status'] for item in statVehicle}
#     # print(statuses)
#     for sta in statuses:
#         veh = Vehicle.objects.filter(vehicle_status=sta)
#         # print(veh)
#         allVehicles.append(veh)
#         # print(allVehicles)
#     params = {'allVehicles' : allVehicles}
#     return render(request,'vehicle/ordersInVehicle.html', params)


# def dashboard(request):
#     return render(request,'vehicle/dashboard.html')