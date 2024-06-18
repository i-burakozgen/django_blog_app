from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    #default comes with required if we dont wanna make it requireed we have specify in the EmailField(required = false)
    email = forms.EmailField()
    
    class Meta():
        model = User
        # oder fields going to show up
        fields = ['username', 'email', 'password1', 'password2']
        
    
