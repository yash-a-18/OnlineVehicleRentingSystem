from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('about/', views.about_us, name="AboutUs"),
    path('contact/', views.contact_us, name="ContactUs"),
    path('search/', views.search, name="Search"),
    path('vehicleview/',views.vehicle_view,name="VehicleView"),
    path('rentvehicle/',views.rent_vehicle,name="RentVehicle"),
]