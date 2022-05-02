from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm

from .models import User
from django import forms
from .models import Feedback

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter confirm password'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]
        
        
class FeedbackForm(forms.ModelForm):
    customer_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Customer name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter email'}))
    product = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter Product name'}))
    feedback = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Your feedback'}))
    
    class Meta:
        model = Feedback
        fields= ['customer_name', 'email', 'product', 'feedback']