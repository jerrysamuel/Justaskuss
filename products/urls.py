from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('productss/', views.productss, name='productss'),
] 