from django.shortcuts import render
from .models import *
from django.template import loader
from django.http import HttpResponse
import requests



# def list(request):
#  return render(request,'home.html',{'pro':products})

def list(request):
 response=requests.get('https://fakestoreapi.com/products')

 products=response.json()

 return render(request,'home.html',{'pro':products})




def det(request,id):
 det=Product.objects.get(id=id)
 return render(request,'det.html',{'det':det})

def men(request):
 men=Product.objects.filter(category="men's clothing")
 return render(request,'category.html',{'men':men})

def women(request):
 women=Product.objects.filter(category="women's clothing")
 return render(request,'category1.html',{'women':women})

def jewelery(request):
 jewelery=Product.objects.filter(category="jewelery")
 return render(request,'category2.html',{'jewelery':jewelery})

def electronics(request):
 electronics=Product.objects.filter(category="electronics")
 return render(request,'category3.html',{'electronics':electronics})



