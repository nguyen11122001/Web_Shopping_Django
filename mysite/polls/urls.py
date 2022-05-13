

from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('category/<int:category_id>/', views.index, name='index'),
    path('', views.index, name='index'),

    path('checkout/', views.checkout, name='checkout'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('login/', views.login, name='login'),
    path('product_details/', views.product_details, name='product_details'),


    
    
    
    


   
]