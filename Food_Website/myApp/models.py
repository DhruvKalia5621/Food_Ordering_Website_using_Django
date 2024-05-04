from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Member(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=20)
    contact = models.IntegerField()

    def __str__(self):
        return self.username
    
class Profile2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.IntegerField( blank=True, null=True)

    # Add any other additional fields you want for the profile
    
        
class profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=20)
    contact = models.IntegerField()
    image_field = models.FileField(upload_to="images/",max_length=250,null=True,default=None)


class Complaints(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Phone = models.IntegerField()
    CompanyName = models.CharField(max_length=255)
    Message = models.TextField()

    def __str__(self):
        return self.Name

class CustomerOrders(models.Model):
    CustomerName = models.CharField(max_length=255)
    OrderID = models.IntegerField()
    OrderedItems = models.CharField(max_length=255)
    Quantity = models.IntegerField()
    TotalAmout = models.IntegerField()
