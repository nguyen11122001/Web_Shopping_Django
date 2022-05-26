from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import  MyUserCreationForm
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