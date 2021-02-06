from django.urls import path
from . import views
from django.conf.urls import url
from CustomerHome.views import RegisterCustomer

urlpatterns = [
    path('', views.index, name="Home"),
    path('Home/', views.Home, name="LoggedinHome"),
    path('signin/',views.signin,name="SignIn"),
    path('Logout/',views.Logout,name="Logout"),    
    path('register/',views.register,name="Register"),
    path('Profile/',views.Profile,name="Profile"),
    path('about/', views.about_us, name="AboutUs"),
    path('contact/', views.contact_us, name="ContactUs"),
    path('search/', views.search, name="Search"),
    path('vehicleview/',views.vehicle_view,name="VehicleView"),
    path('rentvehicle/',views.rent_vehicle,name="RentVehicle"),
    path('LoginAuthentication/',views.LoginAuthentication,name="LoginAuthentication"),
    path('RegisterCustomer/',views.RegisterCustomer,name="RegisterCustomer"),
    # url(r'^RegisterCustomer/',RegisterCustomer),
]