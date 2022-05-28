from unicodedata import category
from django.shortcuts import redirect, render

from .forms import ProductForm
from .models import Product,Category
# Create your views here.
def createProduct(request):
    categorys = Category.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('home-product')
    else:
        form = ProductForm()
    context = {'form': form, 'categorys': categorys}
    return render(request, 'products/product-form.html', context)

def list(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context = {'product': products, 'category': category}
    return render(request, 'products/index.html', context)

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST' :
        print(1)
        form = ProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
            print(1)
            
            form.save()
        # product = form.save(commit=False)
            return redirect('home-product')
    
    categorys = Category.objects.all()
    context = {'form': form, 'categorys': categorys}
    return render(request, 'products/product-form.html', context)

