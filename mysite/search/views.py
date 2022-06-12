from django.shortcuts import render
from products.models import Product,Category,Image
from django.db.models import Q


# Create your views here.
def search(request):
    query = request.GET.get('q')
    if (query == None):
        products = Product.objects.all()
    else:
        products = Product.objects.filter( name__icontains=query)  

    category = Category.objects.all()
    print(products)
    context = {'product': products, 'category': category}
    return render(request, 'products/index.html', context)
