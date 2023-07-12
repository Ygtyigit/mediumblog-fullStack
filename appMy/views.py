from django.shortcuts import render ,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import PostForm

# Create your views here.


def index(request):
    indexparagraf = IndexParagraf.objects.all()
    
    context={
        "indexparagraf":indexparagraf
    }
    if request.POST.get('submit') == 'register':
        if request.method == 'POST':
                name = request.POST["name"]
                email = request.POST["email"]
                password1 = request.POST["password1"]
                password2 = request.POST["password2"]
                
                if password1 == password2:
                    if not User.objects.filter(username = email).exists():
                        if not User.objects.filter(email=email).exists():               
                            user = User.objects.create_user(username = email ,first_name=name,email=email,password=password1)
                            user.save()
                            userinfo = UserInfo(user = user , password = password1)
                            userinfo.save()
                            messages.success(request,'Kayıt Olma Başarılı!')
                            return redirect('index')
                        else:
                            messages.warning(request,'Bu mail üzerine daha önceden bir kullanıcı oluşturulmuş.')
                            return redirect('index')
                    else:
                        messages.warning(request,'Bu kullanıcı adı üzerine daha önceden bir kullanıcı oluşturulmuş!.')
                        return redirect('index')
                else:
                    messages.warning(request,'Şifreyi doğru girdiğinden emin ol!.')
                    return redirect('index')
            
        if request.POST.get('submit') == 'login':
                

            if request.method == "POST":
                username = request.POST["email"]
                password = request.POST["password"]
                
                user = authenticate(request, username = username , password = password)
                
                if User is not None:
                    login(request,user)
                    messages.success(request,"Giriş Yapıldı")
                    return redirect('inpage')
                else:
                    messages.warning(request,"Kullanıcı adı veya Şifre hatalı")
                    return redirect('index')


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



def cardpost(request):
    context={
              
    }
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postlist')
    else:
        form= PostForm()
    
    return render(request,'cardpost.html',{'form':form})


    
       


