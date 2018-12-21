from django.shortcuts import render
from .models import Goods
# Create your views here.


def index(request):
    catalog_list = []
    all_catalog= Goods.objects.values('gmain_catalog').distinct()
    for item in all_catalog:
        catalog_list.append(item['gmain_catalog'])
    context = {
    'catalog':set(catalog_list)
    }
    return render(request, 'index.html', context)


def contact_us(request,):
    context = {
        'name':'Vivi',
        'tel':'18888888888'
    }
    return render(request,'contact.html',context)


def about_us(request,):
    context = {

    }
    return render(request,'about-us.html',context)

def goods_show(request,catalog):
    print(catalog)
    result = Goods.objects.filter(gmain_catalog=catalog).values()
    context={
        'result': result
    }
    return render(request,'goods_show.html',context)

def shop(request,):
    context = {

    }
    return render(request,'shop-left-sidebar.html',context)