from django.shortcuts import render, redirect
from .models import User

def register_view(request):
    messages = []
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        
        
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.append('Username already exists.')
            elif User.objects.filter(email=email).exists():
                messages.append('Email already exists.')
            else:
                user = User(username=username, email=email, password=password)
                user.set_password(password)
                user.save()
                messages.append('User details registered successfully.')
                return render(request, 'live_image_capture.html')
        else:
            messages.append('Passwords did not match.')

    return render(request, 'signup.html', {'custom_messages': messages})
    



def login_view(request):
    
    return render(request, 'login.html')





def home_view(request):
    return render(request, 'index.html')

def logout_view(request):
    return render(request, 'logout.html')



def live_image_capture_view(request):
    return render(request, 'live_image_capture.html')

def voting_view(request):
    return render(request, 'voting.html')

def results_view(request):
    return render(request, 'results.html')

def help_view(request):
    return render(request, 'help.html')