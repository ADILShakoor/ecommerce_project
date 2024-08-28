

# Create your views here.
from django.shortcuts import render, redirect

def login_view(request):
    return render(request, 'accounts/login.html')

def register_view(request):
    return render(request, 'accounts/register.html')

def logout_view(request):
    return redirect('login')
