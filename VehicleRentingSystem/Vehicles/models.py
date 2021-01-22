from django.db import models

# Create your models here.
class Vehicle(models.Model):
    Vehicle_id = models.AutoField
    Vehicle_name = models.CharField(max_length=60)
    Vehicle_company = models.CharField(max_length=60)
    Vehicle_model = models.CharField(max_length=60)
    Vehicle_type = models.CharField(max_length=20)
    Vehicle_fuel = models.CharField(max_length=10)
    Vehicle_No_of_Seats = models.IntegerField()
    Vehicle_color = models.CharField(max_length=20)
    Vehicle_license_plate = models.CharField(max_length=30)
    Vehicle_uploaded_by = models.CharField(max_length=100)
    Vehicle_image1 = models.CharField(max_length=100)
    Vehicle_image2 = models.CharField(max_length=100)
    Vehicle_image3 = models.CharField(max_length=100)
    isGeared = models.BooleanField()
    Vehicle_description = models.CharField(max_length=500)
    Vehicle_No_of_Occupied_days = models.IntegerField()
    Vehicle_price = models.IntegerField()