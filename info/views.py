from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from . import  views

def index(request):
    content = {}
    return render(request,'info/index.html',content)

def contact_us(request):
    content = {}
    return render(request,'info/contact_us.html',content)