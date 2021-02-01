from django.shortcuts import render,redirect
from accounts.forms import UserRegisterForm, UserSigninForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.contrib import messages
from django.views.generic import (CreateView, 
                                  DetailView, 
                                  DeleteView,
                                  ListView,
                                  UpdateView, 
                                  TemplateView)
from django.contrib.auth.mixins import (LoginRequiredMixin, 
                                        UserPassesTestMixin)
from accounts.forms import EditProfileForm, EditUserForm


class CreateUserView(CreateView):
    form_class = UserRegisterForm
    success_url = "/"
    template_name = "accounts/signup.html"
    

class SignInUserView(FormView):
    form_class = UserSigninForm
    success_url = '/'
    template_name = "accounts/signin.html"
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(self.success_url)
            else:
                message = messages.warning(request, 'Invalid credential')
                return render(request, self.template_name, {"form":self.form_class,"message":message})
                
    
class SignOutView(TemplateView):
    template_name = "accounts/signout.html"
    success_url = "/"
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'accounts/signout.html')

    
class UserEditView(LoginRequiredMixin, TemplateView):
    model = User
    form_class = EditUserForm
    success_url = '/'
    template_name = "accounts/user_edit.html"
    
    def post(self, request, *args, **kwargs):
        u_form = self.form_class(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect(self.success_url)
        
    def get(self, request, *args, **kwargs):
        u_form = self.form_class(instance=request.user)
        context = {'form':u_form}
        return render(request, self.template_name , context)



