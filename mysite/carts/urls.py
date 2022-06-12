
from django.urls import path
from . import views

urlpatterns = [

    path('order/<str:pk>/', views.order, name="order"),
    path('cart/', views.listOrders, name="cart"),
    path('test/', views.test, name="test"),

]
