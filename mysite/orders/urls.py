
from django.urls import path
from . import views

urlpatterns = [

    path('order/<str:pk>/', views.order, name="order"),
    path('cart/<str:pk>/', views.listOrders, name="cart"),

]
