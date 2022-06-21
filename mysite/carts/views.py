from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from products.models import Product
from accounts.models import User
from .forms import OrderForm


from .models import Cart, Order

# Create your views here.

def test(request):
    user = request.user
    # user = User.objects.get(id=3)
    print(user.username)
    cart = user.cart_set.first()
    # print(cart)
    return redirect("home")

@login_required(login_url='login')
def order(request,pk):
    if request.user.username:
        user = request.user
        # user = User.objects.get(id=3)
        product = Product.objects.get(id=pk)
        cart = user.cart_set.first()
        # print(cart)
        if cart != None :
            cart = cart
        else: 
            Cart.objects.create(user=user)
        # form = OrderForm(request.POST, request.FILES)
        if request.method == 'POST':
            
            Order.objects.create(
                cart=cart,
                product=product,
                # size=request.POST.get('size'),
                quantity=request.POST.get('quantity'),
            )
            
            return redirect('cart')
        
        context = { 'product': product}
        return render(request, 'orders/order-form.html', context)
    else:
        return redirect('home-product')
    
@login_required(login_url='login')
def listOrders(request):
    if request.user.username:
        user = request.user
        cart = user.cart_set.first()
        # print(cart)
        if cart != None :
            cart = cart
        else: 
            Cart.objects.create(user=user)
        # user = User.objects.get(id=pk)
        cart = user.cart_set.first()
        
        orders = cart.order_set.all()
        return render(request, 'orders/orders.html', {'orders': orders})
    else:
        return redirect('home-product')
    
    
@login_required(login_url='login')
def deleteOrder(request,pk):
    
    user = request.user
    product = Product.objects.get(id=pk)
    cart = user.cart_set.first()
    print(cart)
    if cart != None :
        cart = cart
    else: 
        Cart.objects.create(user=user)
    
    order = Order.objects.filter(product=product, cart=cart).first()

    if order != None:
        order.delete() 
    
    return redirect('cart')
