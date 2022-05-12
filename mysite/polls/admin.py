from django.contrib import admin
from .models import Category, Cart,User,Product,Oder


admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Oder)
admin.site.register(Product)
admin.site.register(User)



