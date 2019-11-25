from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib import messages

def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    elif request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password2==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists!')
                return redirect('accounts-register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password =password1)
                user.save();
                messages.info(request, 'Well done! Now you can login.')
                return render(request, 'login.html')
        else:
            messages.success(request, 'Passwords are not matching!')
            return redirect('accounts-register')

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/index', request.path)
        else:
            messages.info(request, 'Incorrect credentials!')
            return redirect('accounts-login')

def logout(request):
    auth.logout(request)
    messages.info(request, 'You are logged out. Please login again.')
    return redirect('accounts-login')

def profile(request):
    return render(request, 'profile.html')
