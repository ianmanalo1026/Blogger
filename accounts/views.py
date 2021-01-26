from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import (CreateView, 
                                  DetailView, 
                                  DeleteView,
                                  ListView,
                                  UpdateView, 
                                  TemplateView)


class CreateUserView(CreateView):
    form_class = UserCreationForm
    success_url = "core/home.html"
    template_name = "accounts/create.html"

class SignInUserView(TemplateView):
    form_class = AuthenticationForm
    success_url = "core/home.html"
    template_name = "accounts/signin.html"
    
class ProfileUserView(TemplateView):
    pass