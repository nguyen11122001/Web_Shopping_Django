from django.shortcuts import get_object_or_404, redirect, render

from products.models import Product
from accounts.models import User
from .forms import OrderForm

from .models import Cart, Order

# Create your views here.


def order(request,pk):
    # user = request.user
    user = User.objects.get(id=3)
    product = Product.objects.get(id=pk)
    cart = user.cart_set.first()
    print(cart)
    if cart != None :
        cart = cart
    else:
        Cart.objects.create(user=user)
    form = OrderForm(request.POST, request.FILES)
    if request.method == 'POST':
        
        Order.objects.create(
            cart=cart,
            product=product,
            size=request.POST.get('size'),
            quantity=request.POST.get('quantity'),
        )
        
        return redirect('cart')
    
    context = {'form': form, 'product': product}
    return render(request, 'orders/order-form.html', context)
    

def listOrders(request,pk):
    # user = request.user
    user = User.objects.get(id=pk)
    cart = user.cart_set.first()
    
    orders = cart.order_set.all()
    return render(request, 'orders/orders.html', {'orders': orders})