from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    index=[1,2,3,4,5,6];
    return render(request,'index.html',{'p':index})

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
