from django.shortcuts import render
from .models import Goods
# Create your views here.

def index(request):
    goods = Goods()
    catalog1 = Goods.objects.values('gmain_catalog').distinct()
    context = {
    'catalog':catalog1
    }
    return render(request,'index.html',context)

def contact_us(request,):
    context = {
        'name':'Vivi',
        'tel':'18888888888'
    }
    return render(request,'contact_us.html',context)

def about_us(request,):
    context = {

    }
    return render(request,'about_us.html',context)