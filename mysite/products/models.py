from django.db import models
from accounts.models import User
# Create your models here.


class Category(models.Model):
    name =models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    img = models.ImageField(null=True, default="avatar.svg")
    name =models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True,max_length=1000)
    
    price =models.FloatField()
    quantity =models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount =models.IntegerField(null=True, default=0)
    size = models.CharField(max_length=100, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Image(models.Model):
    description = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(null=True, default="product.svg")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name