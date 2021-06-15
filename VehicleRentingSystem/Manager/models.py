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
    Manager_gender = models.CharField(max_length=15)
    Manager_license = models.ImageField(upload_to='img/Manager_License/')
    Manager_agency = models.CharField(max_length=100,default="Fast Rentals")
    Manager_city = models.CharField(max_length=30)
    Manager_state = models.CharField(max_length=30)
    Manager_country = models.CharField(max_length=30)
    Manager_pincode = models.IntegerField()
    isOwner = models.BooleanField(default=False)

    def __str__(self):
        return self.Manager_email + ": " + str(self.Manager_license)