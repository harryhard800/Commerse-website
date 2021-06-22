from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=500)
    product_release = models.DateField()
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=50,default='')
    subcategory = models.CharField(max_length=50,default='')
    image = models.ImageField(upload_to='shop/image', default="")
    
    
    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    Query = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Orders(models.Model):
    """docstring for ClassName"""
    order_id = models.AutoField(primary_key = True)
    ItemJson = models.CharField(max_length=5000,default='')
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=40,default='')
    address = models.CharField(max_length=50,default='')
    address_line_2 = models.CharField(max_length=500,default='')
    state = models.CharField(max_length=500,default= '')
    city = models.CharField(max_length=500,default= '')
    zip_code = models.CharField(max_length=100,default= '')
    phone = models.CharField(max_length=20,default= '')



class Orderupdate(models.Model):
    """docstring fos Orderupdate"models.model def __init__(self, arg):"""
    update_id = models.AutoField(primary_key= True)
    order_id = models.IntegerField(default="")
    upadate_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.upadate_desc+ "...."

        