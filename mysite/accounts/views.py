from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import  MyUserCreationForm,UserForm
from .models import User
from orders.models import Cart, Order
# Create your views here.
def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        
        form = MyUserCreationForm(request.POST)
        
        
        if form.is_valid():

            user = form.save(commit=False)
            

            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'accounts/login_register.html', {'form': form})

def home(request):
    request.session['user'] = request.user.id
    return render(request, 'accounts/hello.html')



def logoutUser(request):
    logout(request)
    return redirect('home')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'accounts/login_register.html')

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'accounts/update-user.html', {'form': form})

@login_required(login_url='login')
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    cart = Cart.objects.filter(user=user)
    

    context = {'user': user, 'cart': cart}
    return render(request, 'accounts/profile.html', context)