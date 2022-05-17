from django.shortcuts import render, redirect
from django.http import HttpResponse
from Owner.models import Owner
from Manager.models import Manager
from CustomerHome.models import Customer
from Vehicles.models import Vehicle
from RentVehicle.models import RentVehicle

from datetime import datetime
from datetime import date
import os
from VehicleRentingSystem.settings import MEDIA_ROOT
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('Agg')
import io, base64

# Create your views here.
def index(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    vehicle = Vehicle.objects.all()
    Message="Welcome Aboard!!"
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Owner_index.html',{'vehicle':vehicle,'Message':Message,'owner':owner,'no_of_pending_request':no_of_pending_request})

def Profile(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Owner_Profile.html',{'owner':owner,'no_of_pending_request':no_of_pending_request})

def register_manager(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    no_of_pending_request=count_pending_rent_request()
    return render(request,'register_manager.html',{'owner':owner,'no_of_pending_request':no_of_pending_request})

def ManagerRegistration(request):
    Manager_firstname=request.POST.get('Manager_firstname','')
    Manager_lastname=request.POST.get('Manager_lastname','')
    Manager_dob=request.POST.get('Manager_dob','')
    Manager_gender=request.POST.get('Manager_gender','')
    Manager_mobileno=request.POST.get('Manager_mobileno','')
    Manager_email=request.POST.get('Manager_email','')
    Manager_password=request.POST.get('Manager_password','')
    Manager_address=request.POST.get('Manager_address','')
    Manager_city=request.POST.get('Manager_city','')
    Manager_state=request.POST.get('Manager_state','')
    Manager_country=request.POST.get('Manager_country','')
    Manager_pincode=request.POST.get('Manager_pincode','')
    Manager_license=request.FILES['Manager_license']

    result_customer = Customer.objects.filter(customer_email=Manager_email)
    result_owner = Owner.objects.filter(Owner_email=Manager_email)
    result_manager = Manager.objects.filter(Manager_email=Manager_email)
    if result_customer.exists() or result_owner.exists() or result_manager.exists():
        Message = "This Email address already exist!!"
        return render(request,'register_manager.html',{'Message':Message})
    else:
        manager=Manager(Manager_firstname=Manager_firstname,Manager_lastname=Manager_lastname,
        Manager_dob=Manager_dob,Manager_gender=Manager_gender,Manager_mobileno=Manager_mobileno,
        Manager_email=Manager_email,Manager_password=Manager_password,Manager_address=Manager_address,
        Manager_city=Manager_city,Manager_state=Manager_state,Manager_country=Manager_country,
        Manager_pincode=Manager_pincode,Manager_license=Manager_license)
        
        manager.save()
        return redirect('/Owner/AllManagers')

def AllManagers(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    manager = Manager.objects.all()
    no_of_pending_request=count_pending_rent_request()
    return render(request,"All_Managers.html",{'manager':manager,'owner':owner,'no_of_pending_request':no_of_pending_request})

def AllCustomers(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    customer = Customer.objects.all()
    no_of_pending_request=count_pending_rent_request()
    return render(request,"All_Customers.html",{'customer':customer,'owner':owner,'no_of_pending_request':no_of_pending_request})

def Manager_Profile(request,Manager_email):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    manager = Manager.objects.get(Manager_email=Manager_email)
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Owner_Manager_Profile.html',{'owner':owner,'manager':manager,'no_of_pending_request':no_of_pending_request})

def Customer_Profile(request,customer_email):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    customer = Customer.objects.get(customer_email=customer_email)
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Owner_Customer_Profile.html',{'owner':owner,'customer':customer,'no_of_pending_request':no_of_pending_request})

def upload_Vehicle(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    no_of_pending_request=count_pending_rent_request()
    return render(request,"Owner_Upload_Vehicle.html",{'owner':owner,'no_of_pending_request':no_of_pending_request})

def AllVehicles(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    vehicle = Vehicle.objects.all()
    no_of_pending_request=count_pending_rent_request()
    return render(request,"Owner_all_vehicles.html",{'vehicle':vehicle,'owner':owner,'no_of_pending_request':no_of_pending_request})

def showdetails(request,Vehicle_license_plate):
    if('user_email' not in request.session):
        return redirect('/signin/')
    vehicle = Vehicle.objects.get(Vehicle_license_plate=Vehicle_license_plate)
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Owner_showdetails.html',{'vehicle':vehicle,'owner':owner,'no_of_pending_request':no_of_pending_request})

def CheckAvailability(request,Vehicle_license_plate):
    if('user_email' not in request.session):
        return redirect('/signin/')

    RentVehicle_Date_of_Booking=request.POST.get('RentVehicle_Date_of_Booking','')
    RentVehicle_Date_of_Return=request.POST.get('RentVehicle_Date_of_Return','')
    print(RentVehicle_Date_of_Booking)
    RentVehicle_Date_of_Booking = datetime.strptime(RentVehicle_Date_of_Booking, '%Y-%m-%d').date()
    print(RentVehicle_Date_of_Booking)
    RentVehicle_Date_of_Return = datetime.strptime(RentVehicle_Date_of_Return, '%Y-%m-%d').date()

    rentvehicle = RentVehicle.objects.filter(Vehicle_license_plate=Vehicle_license_plate)
    vehicle = Vehicle.objects.get(Vehicle_license_plate=Vehicle_license_plate)

    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)

    no_of_pending_request=count_pending_rent_request()

    if RentVehicle_Date_of_Booking < date.today():
        Incorrect_dates = "Please give proper dates"
        return render(request,'Owner_showdetails.html',{'Incorrect_dates':Incorrect_dates,'vehicle':vehicle,'owner':owner,'no_of_pending_request':no_of_pending_request})

    if RentVehicle_Date_of_Return < RentVehicle_Date_of_Booking:
        Incorrect_dates = "Please give proper dates"
        return render(request,'Owner_showdetails.html',{'Incorrect_dates':Incorrect_dates,'vehicle':vehicle,'owner':owner,'no_of_pending_request':no_of_pending_request})
    
    days=(RentVehicle_Date_of_Return-RentVehicle_Date_of_Booking).days+1
    total=days*vehicle.Vehicle_price
    
    rent_data = {"RentVehicle_Date_of_Booking":RentVehicle_Date_of_Booking, "RentVehicle_Date_of_Return":RentVehicle_Date_of_Return,"days":days, "total":total}
    
    for rv in rentvehicle:

        # if (RentVehicle_Date_of_Booking < rv.RentVehicle_Date_of_Booking and RentVehicle_Date_of_Return < rv.RentVehicle_Date_of_Booking) or (RentVehicle_Date_of_Booking > rv.RentVehicle_Date_of_Return and RentVehicle_Date_of_Return > rv.RentVehicle_Date_of_Return):
        #     Available = True
        #     return render(request,'Owner_showdetails.html',{'Available':Available,'vehicle':vehicle,'owner':owner,'rent_data':rent_data,'no_of_pending_request':no_of_pending_request})

        if (rv.RentVehicle_Date_of_Booking >= RentVehicle_Date_of_Booking and RentVehicle_Date_of_Return >= rv.RentVehicle_Date_of_Booking) or (RentVehicle_Date_of_Booking >= rv.RentVehicle_Date_of_Booking and RentVehicle_Date_of_Return <= rv.RentVehicle_Date_of_Return) or (RentVehicle_Date_of_Booking <= rv.RentVehicle_Date_of_Return and RentVehicle_Date_of_Return >= rv.RentVehicle_Date_of_Return):
            if rv.isAvailable:
                Available = True
                Message = "Note that somebody has also requested for this vehicle from " + str(rv.RentVehicle_Date_of_Booking) + " to " + str(rv.RentVehicle_Date_of_Return)
                return render(request,'Owner_showdetails.html',{'Message':Message,'Available':Available,'vehicle':vehicle,'owner':owner,'rent_data':rent_data,'no_of_pending_request':no_of_pending_request})

            NotAvailable = True
            return render(request,'Owner_showdetails.html',{'NotAvailable':NotAvailable,'dates':rv,'vehicle':vehicle,'owner':owner,'no_of_pending_request':no_of_pending_request})
    
    Available = True
    return render(request,'Owner_showdetails.html',{'Available':Available,'vehicle':vehicle,'owner':owner,'rent_data':rent_data,'no_of_pending_request':no_of_pending_request})

def RentRequest(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)

    rentvehicle = RentVehicle.objects.all()
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Owner_RentRequest.html',{'owner':owner,'rentvehicle':rentvehicle,'no_of_pending_request':no_of_pending_request})

def SentRequests(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)

    no_of_pending_request=count_pending_rent_request()

    rentvehicle = RentVehicle.objects.filter(customer_email=owner_email)
    if rentvehicle.exists():
        vehicle = Vehicle.objects.all()
        return render(request,'Owner_SentRequests.html',{'owner':owner,'rentvehicle':rentvehicle,'vehicle':vehicle,'no_of_pending_request':no_of_pending_request})
    else:
        Message = "You haven't rented any vehicle yet!!"
        return render(request,'Owner_SentRequests.html',{'owner':owner,'rentvehicle':rentvehicle,'Message':Message,'no_of_pending_request':no_of_pending_request})

def DeleteManager(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    Manager_email = request.GET.get('Manager_email','')
    manager = Manager.objects.get(Manager_email=Manager_email)
    manager.delete()

    return redirect('/Owner/AllManagers/')

def DeleteVehicle(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    Vehicle_license_plate = request.GET.get('Vehicle_license_plate','')
    vehicle = Vehicle.objects.get(Vehicle_license_plate=Vehicle_license_plate)

    path1 = MEDIA_ROOT + str(vehicle.Vehicle_image1)
    path2 = MEDIA_ROOT + str(vehicle.Vehicle_image2)
    path3 = MEDIA_ROOT + str(vehicle.Vehicle_image3)

    os.remove(path1)
    os.remove(path2)
    os.remove(path3)

    vehicle.delete()
    

    return redirect('/Owner/AllVehicles/')

def count_pending_rent_request():
    no_of_pending_request=0
    rentvehicle = RentVehicle.objects.all()
    for rv in rentvehicle:
        if rv.request_status == "Pending":
            no_of_pending_request+=1
    return no_of_pending_request

def customer_gender_chart():
    customer = Customer.objects.all()
    fig = plt.figure(figsize =(10, 7))
    male_counter = 0
    female_counter = 0
    other = 0
    for cust in customer:
        if cust.customer_gender == 'Male':
            male_counter += 1
        elif cust.customer_gender == 'Female':
            female_counter += 1
        else:
            other += 1
    gender = ['Male','Female', 'Other']
    data = [male_counter, female_counter, other]

    plt.pie(data, labels = gender, autopct='%1.1f%%', startangle=90)
    flike = io.BytesIO()
    fig.savefig(flike)
    cust_gender = base64.b64encode(flike.getvalue()).decode()
    return cust_gender

def customer_no_of_rent_request():
    cust_dict = {}
    rentvehicle = RentVehicle.objects.all()
    for rv in rentvehicle:
        if rv.customer_email not in cust_dict.keys():
            cust_dict[rv.customer_email] = 1
        else:
            cust_dict[rv.customer_email] += 1
    cust_email = list(cust_dict.keys())
    cust_no_of_rent_request = list(cust_dict.values())
    fig = plt.figure(figsize = (12, 6))
 
    # creating the bar plot
    plt.bar(cust_email, cust_no_of_rent_request, color ='green',
            width = 0.4)
    plt.xticks(cust_email, cust_email, rotation=10, horizontalalignment='right')
    plt.xlabel("Customer Email")
    plt.ylabel("No. of Rent Requests")
    plt.show()
    flike = io.BytesIO()
    fig.savefig(flike)
    cust_no_of_rent_request = base64.b64encode(flike.getvalue()).decode()
    return cust_no_of_rent_request

def Vehicle_type_chart():
    vehicle = Vehicle.objects.all()
    fig = plt.figure(figsize =(10, 7))
    bicycle, bike, bus, car, scooter, tourist_van, truck, other = 0, 0, 0, 0, 0, 0, 0, 0
    for v in vehicle:
        if v.Vehicle_type == 'Bicycle':
            bicycle += 1
        elif v.Vehicle_type == 'Bike':
            bike += 1
        elif v.Vehicle_type == 'Bus':
            bus += 1
        elif v.Vehicle_type == 'Car':
            car += 1
        elif v.Vehicle_type == 'Scooter':
            scooter += 1
        elif v.Vehicle_type == 'Tourist Van':
            tourist_van += 1
        elif v.Vehicle_type == 'Truck':
            truck += 1
        else:
            other += 1
    type = ['Bicycle','Bike', 'Bus', 'Car', 'Scooter', 'Tourist Van', 'Truck', 'Other']
    data = [bicycle, bike, bus, car, scooter, tourist_van, truck, other]

    plt.pie(data, labels = type, autopct='%1.1f%%', startangle=90)
    flike = io.BytesIO()
    fig.savefig(flike)
    v_type = base64.b64encode(flike.getvalue()).decode()
    return v_type

def Vehicle_no_of_rent_request():
    veh_dict = {}
    rentvehicle = RentVehicle.objects.all()
    for rv in rentvehicle:
        if rv.Vehicle_license_plate not in veh_dict.keys():
            veh_dict[rv.Vehicle_license_plate] = 1
        else:
            veh_dict[rv.Vehicle_license_plate] += 1
    v_license_plate = list(veh_dict.keys())
    v_no_of_rent_request = list(veh_dict.values())
    fig = plt.figure(figsize = (12, 6))
 
    # creating the bar plot
    plt.bar(v_license_plate, v_no_of_rent_request, color ='maroon',
            width = 0.4)
    plt.xticks(v_license_plate, v_license_plate, rotation=10, horizontalalignment='right')
    plt.xlabel("Vehicle License Plate")
    plt.ylabel("No. of Rent Requests")
    plt.show()
    flike = io.BytesIO()
    fig.savefig(flike)
    v_no_of_rent_request = base64.b64encode(flike.getvalue()).decode()
    return v_no_of_rent_request

def ViewAnalysis(request):
    if('user_email' not in request.session):
        return redirect('/signin/')

    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)

    no_of_pending_request=count_pending_rent_request()
    cust_gender = customer_gender_chart()
    cust_no_of_rent_request = customer_no_of_rent_request()
    v_type = Vehicle_type_chart
    v_no_of_rent_request = Vehicle_no_of_rent_request()
    
    return render(request, 'Analysis.html', {'owner':owner, 'no_of_pending_request':no_of_pending_request,'cust_gender':cust_gender, 'cust_rent_request':cust_no_of_rent_request, 'v_type':v_type, 'v_rent_request':v_no_of_rent_request})