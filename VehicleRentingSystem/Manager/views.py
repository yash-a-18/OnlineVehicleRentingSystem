from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from Owner.models import Owner
from Manager.models import Manager
from CustomerHome.models import Customer
from Vehicles.models import Vehicle

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