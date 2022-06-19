
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from carts.models import Cart, Order
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

def list(request, category_id=None):
    if (category_id == None):
        products = Product.objects.all()
    else:
        products = Product.objects.filter( category_id =category_id)

    category = Category.objects.all()
    context = {'product': products, 'category': category}
    return render(request, 'products/index.html', context)

@login_required(login_url='login')
def updateProduct(request, pk):
    if request.user.is_staff != 1:
        return redirect('home-product')
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST' :
        form = ProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():   
            form.save()
        # product = form.save(commit=False)
            return redirect('product-details',pk=pk)
    
    categorys = Category.objects.all()
    context = {'form': form, 'categorys': categorys,'product':product}
    return render(request, 'products/product-form.html', context)


@login_required(login_url='login')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.user.is_staff != 1:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'GET':
        product.delete()
        return redirect('home-product')
    return redirect("product-details",pk=pk)    
   


def addImage(request, pk):
    if request.user.is_staff != 1:
        return redirect('home-product')
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

def detailsProduct(request, pk):
    product = Product.objects.get(id=pk)
    images = product.image_set.all()
    if request.method == 'POST':
        if request.user.username:
            user = request.user
            # user = User.objects.get(id=3)
            product = Product.objects.get(id=pk)
            cart = user.cart_set.first()
            print(cart)
            if cart != None :
                cart = cart
            else: 
                Cart.objects.create(user=user)
            # form = OrderForm(request.POST, request.FILES)
           
            order = Order.objects.filter(product=product, cart=cart).first()
            print('order')
            print(cart.id)
            print('order')
            if order != None:
                order.quantity = order.quantity + int(request.POST.get('quantity'))
                order.save()
            else:
                Order.objects.create(
                    cart=cart,
                    product=product,
                    # size=request.POST.get('size'),
                    quantity=request.POST.get('quantity'),
                )
            
            return redirect('cart')
        else:
            return redirect('home-product')
    categorys = Category.objects.all()
    context = {'product': product, 'category': categorys, 'images':images}
    return render(request, 'products/product-details.html', context)

