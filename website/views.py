from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout 
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.
def home(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'logged in successfully')
            return redirect('home')
        else:
            messages.success(request,'username or password is incorrect')
            return redirect('home')
    return render(request,'home.html')

def logout_user(request):
    logout(request)
    messages.success(request,'logged out successfully')
    return redirect('home')
def register_user(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form .is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,'Account created successfully')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})
