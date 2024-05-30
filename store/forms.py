from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _

from .models import User
from django import forms
from .models import ContactUser
from django.core import validators


class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Confirm password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactUserForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter firstname'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter phone'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter subject'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Confirm city'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter country'}))
    class Meta:
        model = ContactUser
        fields = ['firstname','name', 'email','phone', 'subject', 'city','country']



        




