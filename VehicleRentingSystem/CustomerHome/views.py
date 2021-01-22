from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'Customer/index.html')

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
