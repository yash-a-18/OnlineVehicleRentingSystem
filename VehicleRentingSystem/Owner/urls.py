from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from CustomerHome import views as cust_views
from Vehicles import views as veh_views

urlpatterns = [
    path('', views.index, name="Owner"),
    path('signin/',cust_views.signin, name="SignIn"),
    path('Logout/',cust_views.Logout, name="Logout"),
    path('Profile/',views.Profile, name="Profile"),
    path('UploadVehicle/',views.upload_Vehicle, name="UploadVehicle"),
    path('RegisterManager/',views.register_manager, name="RegisterManager"),
    path('ManagerRegistration/',views.ManagerRegistration, name="ManagerRegistration"),
    path('AllManagers/',views.AllManagers, name="AllManagers"),
    path('AllCustomers/',views.AllCustomers, name="AllCustomers"),
    path('AllVehicles/',views.AllVehicles, name="AllVehicles"),
    path('VehicleDetails/<str:Vehicle_license_plate>/',views.showdetails,name="OwnerVehicleDetails"),
    path('CheckAvailability/<str:Vehicle_license_plate>/',views.CheckAvailability,name="OwnerCheckAvailability"),
    path('RentRequest/',views.RentRequest,name="RentRequest"),
    path('SentRequests/',views.SentRequests,name="SentRequests"),
    path('DeleteManager/',views.DeleteManager,name="DeleteManager"),
    path('DeleteVehicle/',views.DeleteVehicle,name="DeleteVehicle"),
    path('ManagerProfile/<str:Manager_email>/',views.Manager_Profile,name="ManagerProfile"),
    path('CustomerProfile/<str:customer_email>/',views.Customer_Profile,name="CustomerProfile"),
    path('Vehicle/UploadVehicle',veh_views.upload_vehicle,name="UploadVehicle"),
    path('ViewAnalysis/',views.ViewAnalysis, name="ViewAnalysis"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)