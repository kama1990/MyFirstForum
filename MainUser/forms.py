from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class MyOwnRegisterForm(UserCreationForm):
    """UserCrationForm is used for creating a new user that can use our web application, we want to add email field, which is not required"""
    email = forms.EmailField(required=False)
    email.clean('')
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')