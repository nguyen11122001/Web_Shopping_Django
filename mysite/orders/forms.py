from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Oder



        
class OderForm(ModelForm):
    class Meta:
        model = Oder
        fields =["size", "quantity"]