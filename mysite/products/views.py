
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import ImageForm, ProductForm
from .models import Product,Category,Image
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


@login_required(login_url='login')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.user.staff != 1:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        product.delete()
        return redirect('home-product')
    return render(request, 'base/delete.html', {'obj': product})


def addImage(request, pk):
    product = Product.objects.get(id=pk)
    form = ImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            Image.objects.create(
            product=product,
            img=request.FILES.get('img'),
            description=request.POST.get('description'), 
            )
            return redirect('product-images', pk=pk)
    return render(request, 'products/image-form.html', {'form': form})

def listImage(request, pk):
    product = Product.objects.get(id=pk)
    images = product.image_set.all()
    
    if images.count()>0:
        count=True
    else:
        count = False
    print(count)
    # images = Image.objects.all()
    # images = Image.objects.filter(product=product)
    # images = Image.objects.get(product=product)
    context = {'product': product, 'images': images,'count':count}
    return render(request, 'products/images.html', context)

