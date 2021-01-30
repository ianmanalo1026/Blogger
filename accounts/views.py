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
    template_name = "accounts/signin.html"
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return render(request, 'core/home.html')

    
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