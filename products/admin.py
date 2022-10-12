from django.contrib import admin
from .models import Company
from .models import Product

admin.site.register(Company)
admin.site.register(Product)

