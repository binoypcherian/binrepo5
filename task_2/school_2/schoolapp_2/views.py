from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.urls import reverse_lazy
from .models import Request, Course
from .forms import RequestForm
from django.shortcuts import render

class StudentListView(ListView):
    model = Request
    form_class = RequestForm
    context_object_name = 'requests'

class StudentCreateView(CreateView):
    model = Request
    form_class = RequestForm
    success_url = reverse_lazy('request_list')

class StudentUpdateView(UpdateView):
    model = Request
    form_class = RequestForm
    success_url = reverse_lazy('request_list')

def load_courses(request):
    dept_id = request.GET.get('rdept')
    courses = Course.objects.filter(deptid=dept_id).order_by('cname')
    return render(request, 'schoolapp_2/course_dropdown_list_options.html', {'courses': courses})

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
                return redirect('student_list')
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
            return redirect ('request_add')
        else:
            messages.info(request, "Invalid Login Credentials")
            return redirect('fun3')
    return render(request, 'login.html')

def fun4(request):
    auth.logout(request)
    return redirect ('/')
