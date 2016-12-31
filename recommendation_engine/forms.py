from django import forms
from django.contrib.auth.models import User


# This file defines the forms used within the web application.

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
