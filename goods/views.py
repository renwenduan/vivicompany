import os

from django.shortcuts import render
from .models import Goods
# Create your views here.
from vivicompany.settings import *

catalog_list = []
all_catalog = Goods.objects.values('gcatalog').distinct()
for item in all_catalog:
    catalog_list.append(item['gcatalog'])
catalog_list= set(catalog_list)

def index(request):

    context = {
    'catalog':catalog_list
    }
    return render(request, 'index.html', context)


def contact_us(request,):
    context = {
        'name':'Vivi',
        'tel':'18888888888',
        'catalog':catalog_list
    }
    return render(request,'contact.html',context)


def about_us(request,):
    context = {
        'catalog': catalog_list
    }
    return render(request,'about-us.html',context)

#

def shop(request,):
    goods_list = Goods.objects.all()
    context = {
        'goods_list':goods_list,
        'catalog': catalog_list
    }
    return render(request,'shop-left-sidebar.html',context)


def details(request,id_get):
    file_list = []
    goods = Goods.objects.filter(id=id_get)[0]
    file_path = os.listdir(os.path.join(BASE_DIR,'static','goods','img','product','thumbnail-size'))
    for name in file_path:
        if name.startswith(goods.gname):
            file_list.append(name)
    context = {
        'goods':goods,
        'file_list':file_list,
        'catalog': catalog_list
    }
    return render(request,'product-details.html',context)