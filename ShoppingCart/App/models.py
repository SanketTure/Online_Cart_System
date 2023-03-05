from django.db import models

# Create your models here.

    
class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField()
    
    def __str__(self):
        return self.title
    
class CartModel(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField()
    
    def __str__(self):
        return self.title
    
class CustomerModel(models.Model):
    name = models.CharField(max_length=100)
    phoneNo = models.BigIntegerField()
    address = models.TextField()
    
    def __str__(self):
        return self.name
    
class OrderHistoryModel(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField()
    dateAndTime = models.DateTimeField()
    
    def __str__(self):
        return self.name
    

    
