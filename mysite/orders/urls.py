
from django.urls import path
from . import views

urlpatterns = [

    path('oder/', views.createProduct, name="oder"),

]
