from django.forms import ModelForm

from .models import Product, Image


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['discount', 'updated', 'created', 'size']
        
class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        exclude = ['product', 'updated', 'created']
        
