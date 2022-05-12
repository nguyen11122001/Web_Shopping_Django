
from operator import mod
from django.db import models

class User(models.Model):
    userName=models.CharField(max_length=30)
    storeName=models.CharField(max_length=30)
    password =models.CharField(max_length=20)
    phone =models.CharField(max_length=10)
    email =models.EmailField(max_length=20)
    address =models.CharField(max_length=50)

class Category(models.Model):
    name =models.CharField(max_length=30)

class Product(models.Model):
  
    url =models.CharField(max_length=200)
    name =models.CharField(max_length=50)
    discription =models.TextField(max_length=1000)
    price =models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    store = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity =models.IntegerField()
    

class Cart(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)

class Oder(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity =models.IntegerField()
    cart =models.ForeignKey(Cart,on_delete=models.CASCADE)



