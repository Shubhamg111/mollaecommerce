from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    data={
        'bannerData': Banner.objects.filter(is_active=True),
        'productData': Product.objects.order_by('-id'),

    }
    return render(request,"frontend/pages/index.html",data)

def contact(request):
    return render(request,"frontend/pages/contact.html")

def productview(request,slug):
    productdata=Product.objects.get(slug=slug)
    category_id=productdata.category.id
    relatedproducts = Product.objects.filter(category_id=category_id)
    data={
        'productdata':  productdata,
        'relatedproducts': relatedproducts 
    }
    return render(request,'frontend/pages/productview.html',data)

def product_category(request,slug):
    categoryData = Category.objects.get(slug = slug)
    productsData = Product.objects.filter(category_id=categoryData.id)
    data={
        'productsdata': productsData,
        
    }
    return render(request,'frontend/pages/product_category.html',data)