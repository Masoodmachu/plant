from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from plant.models import Product,homeplants,Categoryplant,fertilizer


# Create your views here.

def home(request):
    return render(request,"home.html")


def registeration(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']

        if cpassword==password:
            user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            return redirect('plant:login')
        else:
            return HttpResponse("Password Does not match")

    return render(request,"register.html")


def login(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('plant:home')
        else:
            return HttpResponse('Invalid username or Password')
    return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return login(request)



def products(request):
    p=Product.objects.all()
    return render(request,"detail.html",{'p':p})


def indoor(request):
    query=Categoryplant.objects.get(id=1)
    p = homeplants.objects.filter(category=query)
    k=Product.objects.filter(category=query)
    return render(request,"indoor.html",{'k':p,'p':k})


def outdoor(request):
    query=Categoryplant.objects.get(id=2)
    p=Product.objects.filter(category=query)
    k=homeplants.objects.filter(category=query)

    return render(request,"outdoor.html",{'p':p,'k':k})



def fertilizers(request):
    query = Categoryplant.objects.get(id=10)
    f = Product.objects.filter(category=query)

    return render(request,"shop.html",{'f':f})



def fertdet(request,pk):
    f=Product.objects.filter(id=pk)
    return render(request,"fertil.html",{'f':f})