from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    records = Record.objects.all()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,"You have been logged in")
            return redirect('home')
        messages.success(request,"There Was An Error Logging In. Please Try again")
        return redirect('home')
    
    return render(request,'home.html',{'records':records})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully registered!")
            return redirect('home')
        
        return render(request,'register.html',{'form':form})

    form = SignUpForm()
    return render(request,'register.html',{'form':form})