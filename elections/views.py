from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, LiveImageCaptureForm


def register_view(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        image_form = LiveImageCaptureForm(request.POST, request.FILES)

        if user_form.is_valid() and image_form.is_valid():
            user = user_form.save()
            image = image_form.cleaned_data['image']

            # Save the live image associated with the user
            user.livefacialimage_set.create(image=image)

            return redirect('live_image_capture')
    else:
        user_form = CustomUserCreationForm()
        image_form = LiveImageCaptureForm()

    return render(request, 'register.html', {'user_form': user_form, 'image_form': image_form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})





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