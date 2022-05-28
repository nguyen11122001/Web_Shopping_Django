from django.shortcuts import get_object_or_404, redirect, render

from products.models import Product

from .forms import OderForm

from .models import Cart, Oder

# Create your views here.


def addProductToCart(request,pk):
    user = request.user
    product = Product.objects.get(id=pk)
    cart = get_object_or_404(Cart, User=user)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True)
    # size = models.CharField(max_length=10)
    # quantity =models.IntegerField()

    if request.method == 'POST':
        form = OderForm(request.POST, request.FILES)
        Oder.objects.create(
            cart=cart,
            product=product,
            size=request.POST.get('size'),
            quantity=request.POST.get('quantity'),
        )
        
        return redirect('home-Oder')
    
    
    return render(request, 'products/product-form.html')

def listOders(request):
    user = request.user
    cart = get_object_or_404(Cart, User=user)
    oders = Oder.objects.filter(cart=cart)
    return render(request, 'oders/oders.html', {'oders': oders})