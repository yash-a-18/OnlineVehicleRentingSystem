from django.db import models
from Vehicles.models import Vehicle
from CustomerHome.models import Customer
from Owner.models import Owner
from Manager.models import Manager

# Create your models here.
class RentVehicle(models.Model):
    RentVehicle_id = models.AutoField
    RentVehicle_Date_of_Rent = models.DateField()
    RentVehicle_Date_of_Return = models.DateField()
    RentVehicle_Total_amount = models.IntegerField()
    isAvailable = models.BooleanField()
    vehicle_id = models.ForeignKey(Vehicle, default=None, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, default=None, on_delete=models.CASCADE)
    manager_authorized_id = models.ForeignKey(Manager, default=None, on_delete=models.CASCADE)
    owner_authorized_id = models.ForeignKey(Owner, default=None, on_delete=models.CASCADE)