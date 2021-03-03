from django.shortcuts import render, redirect
from django.http import HttpResponse
from Vehicles.models import Vehicle
from Owner.models import Owner
from Manager.models import Manager
from django.shortcuts import get_object_or_404

# Create your views here.
def owner_upload_vehicle(request):
    Vehicle_name=request.POST.get('Vehicle_name','')
    Vehicle_company=request.POST.get('Vehicle_company','')
    Vehicle_model=request.POST.get('Vehicle_model','')
    Vehicle_type=request.POST.get('Vehicle_type','')
    Vehicle_fuel=request.POST.get('Vehicle_fuel','')
    Vehicle_No_of_Seats=request.POST.get('Vehicle_No_of_Seats','')
    Vehicle_color=request.POST.get('Vehicle_color','')
    Vehicle_license_plate=request.POST.get('Vehicle_license_plate','')
    
    Vehicle_uploaded_by=request.session.get('user_email')

    isGeared=request.POST.get('isGeared','')
    Vehicle_description=request.POST.get('Vehicle_description','')
    Vehicle_price=request.POST.get('Vehicle_price','')
    Vehicle_image1=request.FILES['Vehicle_image1']
    Vehicle_image2=request.FILES['Vehicle_image2']
    Vehicle_image3=request.FILES['Vehicle_image3']

    result_vehicle = Vehicle.objects.filter(Vehicle_license_plate=Vehicle_license_plate)

    if result_vehicle.exists():
        Message = "This Vehicle already exist!!"
        return render(request,'Owner_Upload_Vehicle.html',{'Message':Message})
    else:
        vehicle=Vehicle(Vehicle_name=Vehicle_name,Vehicle_company=Vehicle_company,
        Vehicle_model=Vehicle_model,Vehicle_type=Vehicle_type,Vehicle_fuel=Vehicle_fuel,
        Vehicle_No_of_Seats=Vehicle_No_of_Seats,Vehicle_color=Vehicle_color,
        Vehicle_license_plate=Vehicle_license_plate,
        Vehicle_uploaded_by=Vehicle_uploaded_by,isGeared=isGeared,Vehicle_description=Vehicle_description,
        Vehicle_price=Vehicle_price,Vehicle_image1=Vehicle_image1,Vehicle_image2=Vehicle_image2,
        Vehicle_image3=Vehicle_image3)
        
        vehicle.save()
        return redirect('/Owner/')