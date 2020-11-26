from django.shortcuts import render
from .forms import LoginForm

def home_view(request):
    return render(request, 'home.html', {})


def login_view(request):
    return render(request, 'login.html', {})