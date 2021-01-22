from django.db import models

# Create your models here.
class Manager(models.Model):
    Manager_id = models.AutoField
    Manager_firstname = models.CharField(max_length=60)
    Manager_lastname = models.CharField(max_length=60)
    Manager_address = models.CharField(max_length=600)
    Manager_email = models.CharField(max_length=100)
    Manager_password = models.CharField(max_length=32)
    Manager_dob = models.DateField()
    Manager_mobileno = models.CharField(max_length=10)
    Manager_age = models.IntegerField()
    Manager_license = models.CharField(max_length=600)
    Manager_agency = models.CharField(max_length=100)
    Manager_city = models.CharField(max_length=30)
    Manager_state = models.CharField(max_length=30)
    Manager_country = models.CharField(max_length=30)
    Manager_pincode = models.IntegerField()
    isManager = models.BooleanField(default=True)