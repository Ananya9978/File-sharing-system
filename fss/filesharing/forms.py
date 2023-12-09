from django.forms import ModelForm
from django import forms
from .models import UserDetails

class SignForm(ModelForm):        
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserDetails
        fields = '__all__'

class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserDetails
        fields = ["email","password"]