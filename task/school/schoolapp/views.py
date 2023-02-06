from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import Req,Dep,Course
from .forms import ReqForm

# Create your views here.
def fun1(request):
    return render(request, 'home.html')

def fun2(request):
    if request.method == 'POST':
        username1 = request.POST['user_signup']
        password11 = request.POST['password_signup']
        password12 = request.POST['password_confirm']
        if password11 == password12:
            if User.objects.filter(username=username1).exists():
                messages.info(request, "Username Already Taken")
                return redirect('fun2')
            else:
                user1=User.objects.create_user(username=username1, password=password11)
                user1.save()
                return redirect('fun1')
        else:
            messages.info(request,"Passwords not Matching")
            return redirect('fun2')
    return render(request, 'register.html')

def fun3(request):
    if request.method=='POST':
        username01 = request.POST['user_login']
        password01 = request.POST['password_login']
        user2=auth.authenticate(username=username01,password=password01)
        if user2 is not None:
            auth.login(request,user2)
            return redirect ('fun5')
        else:
            messages.info(request, "Invalid Login Credentials")
            return redirect('fun3')
    return render(request, 'login.html')

def fun4(request):
    auth.logout(request)
    return redirect ('/')

def fun5(request):
    if request.method == 'POST':
        form=ReqForm(request.POST)
        if form.is_valid():
            reqnew=form.save()
            reqnew.save()
            messages.success(request, 'Request Submission Successful')
        else:
            messages.error(request, 'Request Submission Failed')
            return render(request,'request.html',{'form':form})
    else:
        form=ReqForm(None)
        return render(request, 'request.html',{'form':form})

