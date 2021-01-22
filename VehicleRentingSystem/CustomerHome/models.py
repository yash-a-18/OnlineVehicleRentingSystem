from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField
    customer_firstname = models.CharField(max_length=60)
    customer_lastname = models.CharField(max_length=60)
    customer_address = models.CharField(max_length=600)
    customer_email = models.CharField(max_length=100)
    customer_password = models.CharField(max_length=32)
    customer_dob = models.DateField()
    customer_mobileno = models.CharField(max_length=10)
    customer_gender = models.CharField(max_length=10)
    customer_age = models.IntegerField()
    customer_license = models.CharField(max_length=600)
    customer_city = models.CharField(max_length=30)
    customer_state = models.CharField(max_length=30)
    customer_country = models.CharField(max_length=30)
    customer_pincode = models.IntegerField()