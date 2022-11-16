from django.shortcuts import render
from .models import Product, Company
from django.db.models import Q

def index(request):
    categories = Company.objects.all()
    phones = Product.objects.all()

    context = {
        'categories': categories,
        'phones': phones
    }
    return render(request, 'products/index.html')

def productss(request):
    categories = Company.objects.all()
    phones = Product.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        phones = phones.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        phones = phones.filter(Q(name__icontains=query))

    context = {
        'categories': categories,
        'phones': phones
        'active_category': active_category
    }
    return render(request, 'products/productss.html', context)