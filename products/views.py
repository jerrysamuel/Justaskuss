from django.shortcuts import render
from .models import Product

def index(request):
    phones =Product.objects.all()
    return render(request, 'index.html',{"phones":phones})

def productss(request):
    phones =Product.objects.all()
    return render(request, 'productss.html',{"phones":phones})