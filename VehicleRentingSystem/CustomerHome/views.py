from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from CustomerHome.models import Customer
from Owner.models import Owner
from Manager.models import Manager

isLogin = False

# Create your views here.
def index(request):
    global isLogin

    if('user_email' in request.session):
        email = request.session.get('user_email')

        result_customer = Customer.objects.filter(customer_email=email)
        result_owner = Owner.objects.filter(Owner_email=email)
        result_manager = Manager.objects.filter(Manager_email=email)

        if result_customer.exists():
            request.session['user_email'] = email
            isLogin = True
            return redirect('/Home/')
        elif result_owner.exists():
            request.session['user_email'] = email
            return redirect('/Owner/')
        elif result_manager.exists():
            request.session['user_email'] = email
            return redirect('/Manager/')
        return redirect('/Home/')

    index=[1,2,3,4,5,6]
    if('user_email' not in request.session and isLogin):
        isLogin = False
        Message = "Successfully Logged Out!!"
        return render(request,'index.html',{'Message':Message,'p':index})
    return render(request,'index.html',{'p':index})

def signin(request):
    return render(request,'SignIn.html')

def register(request):
    return render(request,'register.html')

def LoginAuthentication(request):
    global isLogin
    login_email=request.POST.get('login_email','')
    login_password=request.POST.get('login_password','')
    # customer = Customer.objects.all()

    result_customer = Customer.objects.filter(customer_email=login_email,customer_password=login_password)
    result_owner = Owner.objects.filter(Owner_email=login_email,Owner_password=login_password)
    result_manager = Manager.objects.filter(Manager_email=login_email,Manager_password=login_password)

    if result_customer.exists():
        request.session['user_email'] = login_email
        isLogin = True
        return redirect('/Home/')
    elif result_owner.exists():
        request.session['user_email'] = login_email
        return redirect('/Owner/')
    elif result_manager.exists():
        request.session['user_email'] = login_email
        return redirect('/Manager/')
    else:
        Message = "Invalid Email or password!!"
        return render(request,'SignIn.html',{'p':index,'Message':Message})

def RegisterCustomer(request):
    global isLogin

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

    result_customer = Customer.objects.filter(customer_email=customer_email)
    result_owner = Owner.objects.filter(Owner_email=customer_email)
    result_manager = Manager.objects.filter(Manager_email=customer_email)

    if result_customer.exists() or result_owner.exists() or result_manager.exists():
        Message = "This Email address already exist!!"
        return render(request,'register.html',{'Message':Message})
    else:
        customer=Customer(customer_firstname=customer_firstname,customer_lastname=customer_lastname,
        customer_dob=customer_dob,customer_gender=customer_gender,customer_mobileno=customer_mobileno,
        customer_email=customer_email,customer_password=customer_password,customer_address=customer_address,
        customer_city=customer_city,customer_state=customer_state,customer_country=customer_country,
        customer_pincode=customer_pincode,customer_license=customer_license)
        
        customer.save()
        request.session['user_email'] = customer_email
        isLogin = True
        return redirect('/Home/')

def Logout(request):
    del request.session['user_email']
    Message = "Successfully Logged Out!!"
    index=[1,2,3,4,5,6]
    return redirect('/')

def Home(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    customer_email = request.session.get('user_email')
    customer = Customer.objects.get(customer_email=customer_email)
    index=[1,2,3,4,5,6]
    Message="Welcome Aboard!!"
    return render(request,'Home.html',{'p':index,'Message':Message,'customer':customer})

def Profile(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    customer_email = request.session.get('user_email')
    customer = Customer.objects.get(customer_email=customer_email)
    return render(request,'Profile.html',{'customer':customer})

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
