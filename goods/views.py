from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

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