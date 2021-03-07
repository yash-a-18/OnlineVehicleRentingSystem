from django.db import models
from Vehicles.models import Vehicle
from CustomerHome.models import Customer
from Owner.models import Owner
from Manager.models import Manager

# Create your models here.
class RentVehicle(models.Model):
    RentVehicle_id = models.AutoField
    RentVehicle_Date_of_Booking = models.DateField(blank=True,null=True)
    RentVehicle_Date_of_Return = models.DateField(blank=True,null=True)
    RentVehicle_Total_amount = models.IntegerField()
    isAvailable = models.BooleanField(default=True)
    isBillPaid = models.BooleanField(default=False)
    Vehicle_license_plate = models.CharField(max_length=30)
    customer_email = models.CharField(max_length=100)
    request_accepted_by = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.customer_email + ": " + str(self.Vehicle_license_plate)