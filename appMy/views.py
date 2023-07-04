from django.shortcuts import render ,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def index(request):
    indexparagraf = IndexParagraf.objects.all()

    context={
        "indexparagraf":indexparagraf
    }

    return render(request,'index.html',context)


def ourstory(request): 
    context={
        
    }  
    return render(request,'ourstory.html',context)


def membership(request): 
    context={
        
    }  
    return render(request,'membership.html',context)


def write(request): 
    context={
        
    }  
    return render(request,'write.html',context)

def inpage(request): 
    context={
        
    }  
    return render(request,'inpage.html',context)