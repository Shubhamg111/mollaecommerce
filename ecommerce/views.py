from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    data={
        'bannerData': Banner.objects.filter(is_active=True)
    }
    return render(request,"frontend/pages/index.html",data)

def contact(request):
    return render(request,"frontend/pages/contact.html")