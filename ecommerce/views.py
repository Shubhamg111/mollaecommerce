from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.

def home(request):
    data={
        'bannerData': Banner.objects.filter(is_active=True),
        'productData': Product.objects.order_by('-id'),

    }
    return render(request,"frontend/pages/index.html",data)

def contact(request):
    return render(request,"frontend/pages/contact.html")

def product_list(request):
    data={
        'products':Product.objects.order_by('category'),
    }
    return render(request,'frontend/pages/productList.html',data)

def productview(request,slug):
    productData=Product.objects.get(slug=slug)
    categoryId=productData.category_id
    relatedData = Product.objects.filter(category_id=categoryId)
    data={
        'productData':  productData,
        'relatedData': relatedData 
    }
    return render(request,'frontend/pages/productview.html',data) 

def productcategory(request,slug):
    categoryData = Category.objects.get(slug = slug)
    productsData = Product.objects.filter(category_id=categoryData.id)
    data={
        'productsData': productsData,
        
    }
    return render(request,'frontend/pages/product_category.html',data)

def productsearch(request):
    if request.method=="POST":
        criteria = request.POST['criteria']
        productsData = Product.objects.filter(Q(name__icontains=criteria) | Q(description__icontains=criteria))
        data ={
            'productsData': productsData
        }
        return render(request,'frontend/pages/productList.html',data)
    else:
        return redirect('productlist') 