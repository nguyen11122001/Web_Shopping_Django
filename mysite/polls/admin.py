from django.contrib import admin
from .models import Category,Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']
    # raw_id_fields = ['user']


admin.site.register(Category)
admin.site.register(Product,ProductAdmin)




