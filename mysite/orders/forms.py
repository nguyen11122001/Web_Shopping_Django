from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Order



        
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields =["size", "quantity"]