from django.shortcuts import render, redirect
from django.http import HttpResponse
from Owner.models import Owner
from Manager.models import Manager
from CustomerHome.models import Customer

# Create your views here.
def index(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    index=[1,2,3,4,5,6]
    Message="Welcome Aboard!!"
    return render(request,'Owner_index.html',{'p':index,'Message':Message,'owner':owner})

def Profile(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    return render(request,'Owner_Profile.html',{'owner':owner})

def register_manager(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    return render(request,'register_manager.html',{'owner':owner})

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
    return render(request,"All_Managers.html",{'manager':manager,'owner':owner})

def AllCustomers(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    customer = Customer.objects.all()
    return render(request,"All_Customers.html",{'customer':customer,'owner':owner})

def Vehicle(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    return render(request,"Owner_Upload_Vehicle.html",{'owner':owner})

def Manager_Profile(request,Manager_email):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    manager = Manager.objects.get(Manager_email=Manager_email)
    return render(request,'Owner_Manager_Profile.html',{'owner':owner,'manager':manager})

def Customer_Profile(request,customer_email):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    customer = Customer.objects.get(customer_email=customer_email)
    return render(request,'Owner_Customer_Profile.html',{'owner':owner,'customer':customer})