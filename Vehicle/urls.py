from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="VehicleHome"),
    # path('orders/', views.orders, name="Orders"),
    # path('ordersInVehicle/', views.ordersInVehicle, name="OrdersInVehicle"),
    # path('dashboard/', views.dashboard, name="Orders"),
]