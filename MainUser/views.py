from django.shortcuts import render, redirect# 
from django.contrib.auth.forms import UserCreationForm
from .forms import MyOwnRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.forms import AuthenticationForm # we need it for login 
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def register(request):

    # GET - reads date from server
    if request.method == "GET":
        return render(request, 'register.html', {'form': MyOwnRegisterForm})
    # POST - when user has to provide information by the use of form
    else:
        username = request.POST.get('username') # get username from request
        name = request.POST.get('name')
        email = request.POST.get('email')# the email is not required , you can check it in forms.py
        password1 = request.POST.get('password1') # get password1 from request
        password2 = request.POST.get('password2') # get password2 from request
        

        # we have to check if password1 and password2 are same , and if username and email is still available 

        if password1 == password2:

            emailTaken = User.objects.filter(email=email)

            usernameTaken = User.objects.filter(username=username).exists()

            if emailTaken:
                    error = f'Sorry, email: {email} is already exist'

            if usernameTaken:
                error = f'Sorry, but Username: {username} is already exist'

         # password validation
            if not emailTaken and not usernameTaken:
                try:
                    validate_password(password1)
                except ValidationError as e:
                    return render(request, 'register.html', {'form': MyOwnRegisterForm(), 'passError': e.message })
                else:
                    emailValid = validate_email(email)
                    if emailValid:
                    # create user if email valid
                        user = User.objects.create_user(
                            username=username, password=password1
                            )
                        userPrint = f'{username}! You were registered well'
                        return render(request, 'register.html', {'form': MyOwnRegisterForm, 'userPrint':userPrint})
                    else:
                        error = f'{email} is not a valid email. Please try again'

        else:
            error = "Your passwords are not same"

        return render(request, 'register.html', {'form': MyOwnRegisterForm, 'error': error})
    

def logUser(request):
    if request.method == 'GET':
        return render(request, 'logUser.html', {'form': AuthenticationForm}) # Authentication Form - its a standard login form
    else:
    # we have to check the username and password 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password) # we have to check if this pair : username and password are in DB. If authenticate is ok , returns a user object , if it's not ok its NONE, so :

        # if user exist - we have to login user
        if user is not None: # this is correct logIn
        # we have to import login function 
            login(request, user)
            return redirect('home') # home is in Registration , we have to know where we want to put user through. home is name from urls.
        
        # if we cannot logIn the user, we have to chcek if username exist 
        else:
            usernameExists = User.objects.filter(username=username).exists()

        # if we are sure that username exist - probably password is incorrect
            if usernameExists:
                error = f'Sorry, but password for user {username} is incorrect'

            else:
                error = f'Sorry, but username: {username} is incorrect'

        # we have to return page with error . we have to complete the templates logUser.html
            return render(request, 'logUser.html', {'form':AuthenticationForm(), 'error':error})
        
# we have to import logout function and we return directly to home
def logOutUser(request):
    logout(request)
    return render(request, 'logOutUser.html') # we could use retur redirect('home' )home is in Registration , we have to know where we want to put user through after logOut. home is name from urls. but we wanted , that user knew that he is logOut
            
        