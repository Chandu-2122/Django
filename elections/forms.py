from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=15)

class LiveImageCaptureForm(forms.Form):
    image = forms.ImageField()