from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from Owner.models import Owner
from Manager.models import Manager
from CustomerHome.models import Customer
from Vehicles.models import Vehicle
from RentVehicle.models import RentVehicle

from datetime import datetime

# Create your views here.
def index(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    manager_email = request.session.get('user_email')
    manager = Manager.objects.get(Manager_email=manager_email)
    vehicle = Vehicle.objects.all()
    Message="Welcome Aboard!!"
    return render(request,'Manager_index.html',{'vehicle':vehicle,'Message':Message,'manager':manager})

def Profile(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    manager_email = request.session.get('user_email')
    manager = Manager.objects.get(Manager_email=manager_email)
    return render(request,'Manager_Profile.html',{'manager':manager})

def AllCustomers(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    manager_email = request.session.get('user_email')
    manager = Manager.objects.get(Manager_email=manager_email)
    customer = Customer.objects.all()
    return render(request,"Manager_All_Customers.html",{'customer':customer,'manager':manager})

def Customer_Profile(request,customer_email):
    if('user_email' not in request.session):
        return redirect('/signin/')
    manager_email = request.session.get('user_email')
    manager = Manager.objects.get(Manager_email=manager_email)
    customer = Customer.objects.get(customer_email=customer_email)
    return render(request,'Manager_Customer_Profile.html',{'manager':manager,'customer':customer})

def upload_Vehicle(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    manager_email = request.session.get('user_email')
    manager = Manager.objects.get(Manager_email=manager_email)
    return render(request,"Manager_Upload_Vehicle.html",{'manager':manager})

def AllVehicles(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    manager_email = request.session.get('user_email')
    manager = Manager.objects.get(Manager_email=manager_email)
    vehicle = Vehicle.objects.all()
    return render(request,"Manager_all_vehicles.html",{'vehicle':vehicle,'manager':manager})

def showdetails(request,Vehicle_license_plate):
    if('user_email' not in request.session):
        return redirect('/signin/')
    vehicle = Vehicle.objects.get(Vehicle_license_plate=Vehicle_license_plate)
    manager_email = request.session.get('user_email')
    manager = Manager.objects.get(Manager_email=manager_email)
    return render(request,'Manager_showdetails.html',{'vehicle':vehicle,'manager':manager})

def CheckAvailability(request,Vehicle_license_plate):
    if('user_email' not in request.session):
        return redirect('/signin/')

    RentVehicle_Date_of_Booking=request.POST.get('RentVehicle_Date_of_Booking','')
    RentVehicle_Date_of_Return=request.POST.get('RentVehicle_Date_of_Return','')

    RentVehicle_Date_of_Booking = datetime.strptime(RentVehicle_Date_of_Booking, '%Y-%m-%d').date()
    RentVehicle_Date_of_Return = datetime.strptime(RentVehicle_Date_of_Return, '%Y-%m-%d').date()

    rentvehicle = RentVehicle.objects.filter(Vehicle_license_plate=Vehicle_license_plate)
    vehicle = Vehicle.objects.get(Vehicle_license_plate=Vehicle_license_plate)

    manager_email = request.session.get('user_email')
    manager = Manager.objects.get(Manager_email=manager_email)
    
    for rv in rentvehicle:
        if rv.RentVehicle_Date_of_Booking <= RentVehicle_Date_of_Booking and RentVehicle_Date_of_Booking <= rv.RentVehicle_Date_of_Return:
            if rv.isAvailable:
                Available = True
                Message = "Note that somebody has also requested for this vehicle from " + str(rv.RentVehicle_Date_of_Booking) + " to " + str(rv.RentVehicle_Date_of_Return)
                return render(request,'Manager_showdetails.html',{'Message':Message,'Available':Available,'vehicle':vehicle,'manager':manager})

            NotAvailable = True
            return render(request,'Manager_showdetails.html',{'NotAvailable':NotAvailable,'dates':rv,'vehicle':vehicle,'manager':manager})
    
    Available = True
    return render(request,'Manager_showdetails.html',{'Available':Available,'vehicle':vehicle,'manager':manager})
