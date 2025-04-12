from django.shortcuts import render

# Create your views here.

from coursehub import views
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login_view(request):
    return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard.html')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


def welcome_view(request):
    return render(request, 'welcome.html')


def dashboard_view(request):
    return render(request, 'dashboard.html')


def register_view(request):
    return render(request, 'register.html')
