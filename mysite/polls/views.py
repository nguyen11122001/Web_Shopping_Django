

from django.shortcuts import render, get_object_or_404, get_list_or_404


from .models import Category, Product



def index(request,category_id=None):
    if (category_id == None):
        product = get_list_or_404(Product)
    else:
        product = get_list_or_404(Product, category_id=category_id)

    category = get_list_or_404(Category)
    return render(request, 'polls/index.html', {'product': product, 'category':category})



def checkout(request):
    return render(request, 'polls/checkout.html')

def contact_us(request):
    return render(request, 'polls/contact-us.html')

def login(request):
    return render(request, 'polls/login.html')

def product_details(request):
    
    return render(request, 'polls/product-details.html')




