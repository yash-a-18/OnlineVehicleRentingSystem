from django.shortcuts import render, redirect
from django.http import HttpResponse
from CustomerHome.models import Customer
from RentVehicle.models import RentVehicle
from Owner.models import Owner
from Manager.models import Manager

from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'RentVehicle/index.html')

def SendRequest_toOwner(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    user_email = request.session.get('user_email')

    RentVehicle_Date_of_Booking=request.POST.get('RentVehicle_Date_of_Booking','')
    RentVehicle_Date_of_Return=request.POST.get('RentVehicle_Date_of_Return','')
    Total_days=request.POST.get('Total_days','')
    RentVehicle_Total_amount=request.POST.get('RentVehicle_Total_amount','')
    Vehicle_license_plate=request.POST.get('Vehicle_license_plate','')
    RentVehicle_Date_of_Booking=request.POST.get('RentVehicle_Date_of_Booking','')

    RentVehicle_Date_of_Booking = datetime.strptime(RentVehicle_Date_of_Booking, '%B %d, %Y').date()
    RentVehicle_Date_of_Return = datetime.strptime(RentVehicle_Date_of_Return, '%B %d, %Y').date()
    
    rentvehicle = RentVehicle(RentVehicle_Date_of_Booking=RentVehicle_Date_of_Booking,
    RentVehicle_Date_of_Return=RentVehicle_Date_of_Return,
    Total_days=Total_days,RentVehicle_Total_amount=RentVehicle_Total_amount,
    Vehicle_license_plate=Vehicle_license_plate,customer_email=user_email)

    rentvehicle.save()

    customer = Customer.objects.filter(customer_email=user_email)
    if customer.exists():
        return redirect("/SentRequests/")

    manager = Manager.objects.filter(Manager_email=user_email)
    if manager.exists():
        return redirect("/Manager/SentRequests/")

    owner = Owner.objects.filter(Owner_email=user_email)
    if owner.exists():
        return redirect("/Owner/SentRequests/")

def AcceptRequest(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    user_email = request.session.get('user_email')
    id = request.GET.get('id','')
    rentvehicle = RentVehicle.objects.get(id=id)
    rentvehicle.isAvailable= False
    rentvehicle.request_responded_by = user_email
    rentvehicle.request_status = "Accepted"
    rentvehicle.save()

    manager = Manager.objects.filter(Manager_email=user_email)
    if manager.exists():
        return redirect("/Manager/RentRequest/")
    
    owner = Owner.objects.filter(Owner_email=user_email)
    if owner.exists():
        return redirect("/Owner/RentRequest/")

def DeclineRequest(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    user_email = request.session.get('user_email')
    id = request.GET.get('id','')
    rentvehicle = RentVehicle.objects.get(id=id)
    rentvehicle.isAvailable= True
    rentvehicle.request_responded_by = user_email
    rentvehicle.request_status = "Declined"
    rentvehicle.save()
    
    manager = Manager.objects.filter(Manager_email=user_email)
    if manager.exists():
        return redirect("/Manager/RentRequest/")
    
    owner = Owner.objects.filter(Owner_email=user_email)
    if owner.exists():
        return redirect("/Owner/RentRequest/")

def CancelRequest(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    user_email = request.session.get('user_email')
    id = request.GET.get('id','')
    rentvehicle = RentVehicle.objects.get(id=id)
    rentvehicle.delete()

    customer = Customer.objects.filter(customer_email=user_email)
    if customer.exists():
        return redirect("/SentRequests/")

    manager = Manager.objects.filter(Manager_email=user_email)
    if manager.exists():
        return redirect("/Manager/SentRequests/")

    owner = Owner.objects.filter(Owner_email=user_email)
    if owner.exists():
        return redirect("/Owner/SentRequests/")