from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"home.html",{})

def about(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"about.html",{})

def gallery(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"gallery.html",{})

def login(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"login.html",{})

def signup(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"signup.html",{})




