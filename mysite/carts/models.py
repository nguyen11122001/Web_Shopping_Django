from django.db import models
from django.db import models
from accounts.models import User
from products.models import Product
# Create your models here.

class Cart(models.Model):
    # user = models.OneToOneField(
    #     User,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    # )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.name
    

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=10)
    quantity =models.IntegerField()
    class Meta:
        ordering = ['-updated', '-created']

    # def __str__(self):
    #     return self.name
    
    @property
    def total(self):
        return self.quantity * self.product.price
    def __str__(self):
        return (self.cart.user.name + " => " +self.product.name)
    
    
