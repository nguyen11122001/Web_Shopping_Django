from django.db import models

# Create your models here.
class Category(models.Model):
    name =models.CharField(max_length=30)

class Product(models.Model):
    url =models.CharField(max_length=200)
    name =models.CharField(max_length=50)
    discription =models.TextField(max_length=1000)
    price =models.FloatField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    size = models.CharField(max_length=100, null=True)
    
# class Cart(models.Model):
#     user =models.ForeignKey(User,on_delete=models.CASCADE)

# class Oder(models.Model):
#     product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     size = models.CharField(max_length=10)
#     quantity =models.IntegerField()
#     cart =models.ForeignKey(Cart,on_delete=models.CASCADE)
