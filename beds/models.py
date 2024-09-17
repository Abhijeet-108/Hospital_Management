from django.db import models
from django.contrib.auth.models import User 
# Create your models here


class hosp(models.Model):
    
    host = models.ForeignKey(User , on_delete = models.SET_NULL , null = True)
    name = models.CharField(max_length=50)
    email = models.EmailField(null=False)
    phone = models.BigIntegerField(null=False)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    pin = models.IntegerField(null=False)
    description = models.TextField(null = True , blank = True)
 #   p_img = models.ImageField()
  #  c_img = models.ImageField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name
    
class inventory(models.Model):
    host = models.ForeignKey(User , on_delete=models.SET_NULL , null = True)
    item = models.CharField(max_length=30 , null = False)
    quantity = models.IntegerField(null = True , blank=True)
    avail = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item
    

class blood(models.Model):
    host = models.ForeignKey(User , on_delete=models.SET_NULL , null = True)
    btype = models.CharField(max_length=5 , blank =False , null = False)
    avail = models.BooleanField(default=False)
    unit = models.IntegerField(null = True , blank = True)

    def __str__(self):
        return self.btype