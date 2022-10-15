from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('productss/', views.productss, name='productss'),
    path('product_details/', views.product_details, name='product_details'),
    path('search_results/', views.search_results, name='search_results'),
    path('problem_solutions/', views.problem_solutions, name='problem_solutions'),
] 