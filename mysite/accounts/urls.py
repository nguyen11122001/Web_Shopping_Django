
from django.urls import path
from . import views

urlpatterns = [
    # path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('home/', views.home, name="home"),
    path('', views.loginUser, name="login"),
    path('edit/', views.updateUser, name="edit-profile"),
    path('profile/', views.userProfile, name="user-profile"),
]
