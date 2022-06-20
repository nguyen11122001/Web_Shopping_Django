
from django.urls import path
from . import views

urlpatterns = [

    path('create-product/', views.createProduct, name="create-product"),
    path('', views.list, name="home-product"),
    path('product-details/<str:pk>/', views.detailsProduct, name="product-details"),
    path('update-product/<str:pk>/', views.updateProduct, name="update-product"),
    path('delete-product/<str:pk>/', views.deleteProduct, name="delete-product"),
    
    
    path('delete-image/<str:pk>/', views.delImage, name="delete-image"),
    path('product-images/<str:pk>/', views.listImage, name="product-images"),
    path('add-product-images/<str:pk>/', views.addImage, name="add-product-images"),
    path('category/<int:category_id>/', views.list, name='home-product'),
]
