from typing import Any
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Product(models.Model):
    image = models.ImageField(upload_to='images')
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    delivery_charge = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=100)



    def __str__(self):
        return self.product_name
    
class Customer(models.Model):
    username = models.CharField(max_length=100)
    email= models.EmailField()
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username
    
class CustomerOrder(models.Model):
    customerName = models.CharField(max_length=150)
    phoneNumber = models.IntegerField()
    email = models.EmailField()
    city = models.TextField(blank=True)
    region = models.TextField(blank=True)
    street_address = models.TextField(blank=True)
    zip_code = models.TextField(blank=True)
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField()
    total = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)

    def __str__(self):
        return self.customerName
    
class Feedback(models.Model):
    fullname =models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.fullname
    

    

    