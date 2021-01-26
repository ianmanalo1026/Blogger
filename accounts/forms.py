from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from accounts.models import Profile



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    
    class Meta:
        model = User
        fields = [
                    "username",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "email",
            ]
        

class UserSigninForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]