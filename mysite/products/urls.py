
from django.urls import path
from . import views

urlpatterns = [

    path('create-product/', views.createProduct, name="create-product"),
    path('', views.list, name="home-product"),
    path('update-product/<str:pk>/', views.updateProduct, name="update-product"),
    path('product-images/<str:pk>/', views.listImage, name="product-images"),
    path('add-product-images/<str:pk>/', views.addImage, name="add-product-images"),
    path('category/<int:category_id>/', views.list, name='home-product'),
]
