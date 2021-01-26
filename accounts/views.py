from django.shortcuts import render
from accounts.forms import UserRegisterForm, UserSigninForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic.edit import FormView
from django.views.generic import (CreateView, 
                                  DetailView, 
                                  DeleteView,
                                  ListView,
                                  UpdateView, 
                                  TemplateView)


class CreateUserView(CreateView):
    form_class = UserRegisterForm
    success_url = "/"
    template_name = "accounts/signup.html"
    

class SignInUserView(FormView):
    form_class = UserSigninForm
    success_url = "/"
    template_name = "accounts/signin.html"
    
    def form_valid(self, form):
        return super().form_valid(form)
        
    
    
class SignOutView(TemplateView):
    template_name = "accounts/signout.html"
    success_url = "/"
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'accounts/signout.html')

    
class ProfileUserView(TemplateView):
    pass