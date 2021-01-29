from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from CustomerHome.models import Customer

# Create your views here.
def index(request):
    index=[1,2,3,4,5,6];
    return render(request,'index.html',{'p':index})

def signin(request):
    return render(request,'SignIn.html')

def register(request):
    return render(request,'register.html')

def RegisterCustomer(request):
    customer_firstname=request.POST.get('customer_firstname','')
    customer_lastname=request.POST.get('customer_lastname','')
    customer_dob=request.POST.get('customer_dob','')
    customer_gender=request.POST.get('customer_gender','')
    customer_mobileno=request.POST.get('customer_mobileno','')
    customer_email=request.POST.get('customer_email','')
    customer_password=request.POST.get('customer_password','')
    customer_address=request.POST.get('customer_address','')
    customer_city=request.POST.get('customer_city','')
    customer_state=request.POST.get('customer_state','')
    customer_country=request.POST.get('customer_country','')
    customer_pincode=request.POST.get('customer_pincode','')
    customer_license=request.FILES['customer_license']
    
    customer=Customer(customer_firstname=customer_firstname,customer_lastname=customer_lastname,
    customer_dob=customer_dob,customer_gender=customer_gender,customer_mobileno=customer_mobileno,
    customer_email=customer_email,customer_password=customer_password,customer_address=customer_address,
    customer_city=customer_city,customer_state=customer_state,customer_country=customer_country,
    customer_pincode=customer_pincode,customer_license=customer_license)
    
    customer.save()
    Message = "Successfully Registered"
    index=[1,2,3,4,5,6];
    return render(request,'Home.html',{'p':index,'Message':Message,'customer':customer,'customer_license':customer.customer_license})

def Home(request):
    index=[1,2,3,4,5,6];
    return render(request,'Home.html',{'p':index})

def about_us(request):
    return HttpResponse('About Us')
    
def contact_us(request):
    return HttpResponse('Contact Us')

def search(request):
    return HttpResponse('search')

def vehicle_view(request):
    return HttpResponse('vehicle view')

def rent_vehicle(request):
    return HttpResponse('rent vehicle')
