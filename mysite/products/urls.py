
from django.urls import path
from . import views

urlpatterns = [

    path('create-product/', views.createProduct, name="create-product"),
    path('', views.list, name="home-product"),
    path('update-product/<str:pk>/', views.updateProduct, name="update-product"),
]
