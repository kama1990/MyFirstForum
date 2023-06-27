from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import MyOwnRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

# Create your views here.

def register(request):

    if request.method == "GET":
        return render(request, 'register.html', {'form': MyOwnRegisterForm})
    else:
        username = request.POST.get('username') # get username from request
        email = request.POST.get('email') # the email is not required , you can check it in forms.py
        password1 = request.POST.get('password1') # get password1 from request
        password2 = request.POST.get('password2') # get password2 from request

        # we have to check if password1 and password2 are same , and if username is still available 

        if password1 == password2:

            emailTaken = User.objects.filter(email=email).exists()

            usernameTaken = User.objects.filter(username=username).exists()

            if emailTaken:
                error = f'Sorry, email: {email} is already exist'

            if usernameTaken:
                error = f'Sorry, but Username: {username} is already exist'
          
            if not emailTaken and not usernameTaken:
                try:
                    validate_password(password1)
                except ValidationError as e:
                    return render(request, 'register.html', {'form': MyOwnRegisterForm(), 'passError': e.message })
                else:
                    user = User.objects.create_user(
                            username=username, email=email, password=password1)
                    return render(request, 'register.html', {'form': MyOwnRegisterForm})
                




        else:
            error = "Your passwords are not same"

        return render(request, 'register.html', {'form': MyOwnRegisterForm, 'error': error})