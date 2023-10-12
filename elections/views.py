from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustumUserCreationForm





def home_view(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    return render(request, 'logout.html')

def register_view(request):
    return render(request, 'register.html')

def live_image_capture_view(request):
    return render(request, 'live_image_capture.html')

def voting_view(request):
    return render(request, 'voting.html')

def results_view(request):
    return render(request, 'results.html')

def help_view(request):
    return render(request, 'help.html')