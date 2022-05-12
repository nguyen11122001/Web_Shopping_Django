

from unicodedata import category
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, get_list_or_404


from .models import Category, Product



def index(request):
    product = get_list_or_404(Product)
    category = get_list_or_404(Category)


    return render(request, 'polls/index.html', {'product': product, 'category':category})

def blog(request):
    return render(request, 'polls/blog.html')

def blog_single(request):
    return render(request, 'polls/blog-single.html')

def cart(request):
    return render(request, 'polls/cart.html')

def checkout(request):
    return render(request, 'polls/checkout.html')

def contact_us(request):
    return render(request, 'polls/contact-us.html')

def login(request):
    return render(request, 'polls/login.html')

def product_details(request):
    
    return render(request, 'polls/product-details.html')

def shop(request):
    return render(request, 'polls/shop.html')



def home(request):
    product = get_list_or_404(Product)
    category = get_list_or_404(Category)

    return render(request, 'polls/homedemo.html', {'product': product, 'category':category})