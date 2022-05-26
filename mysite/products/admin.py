from django.contrib import admin

# Register your models here.
from .models import Product, Category,Image

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Image)