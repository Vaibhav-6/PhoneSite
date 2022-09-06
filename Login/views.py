from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from .models import *
from .forms import SignUpForm, LogInForm


def signup(request):
    if request.method == 'POST': #getting the POST request and checking if form is valid 
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save() #saving it in db
            login(request, user)
            return redirect('/users/products/') #redirecting to prduct page
    else:
        form = SignUpForm()   #intitally sending form for user to fill 
    return render(request, 'users/signup.html', {'form': form})


def log_in(request):
    error = False
    if request.user.is_authenticated: #checking if user is already authenticated and redirecting to product page
        return redirect('/users/products/')
    if request.method == "POST": #getting Post request and checking is form is valid
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password) #authenticating the user 
            if user:
                login(request, user)  #login and redirect user to product pages
                return redirect('/users/products/')
            else:
                error = True #else error would be shown
    else:
        form = LogInForm()

    return render(request, 'users/login.html', {'form': form, 'error': error})


def log_out(request):
    logout(request)
    return redirect(reverse('users:login')) #using reverse func to logout

def products(request):
    products=Product.objects.all() #Sending Product object to product.html
    return render(request,'product.html',{'products':products})