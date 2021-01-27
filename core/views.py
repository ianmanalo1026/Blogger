from core.models import Post
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from core.forms import CreateForm, UpdateForm
from django.contrib.auth.mixins import (LoginRequiredMixin, 
                                        UserPassesTestMixin)
from django.views.generic import (CreateView, 
                                  DetailView, 
                                  DeleteView,
                                  ListView,
                                  UpdateView)


class HomeListView(ListView):
    
    model = Post
    template_name = "core/home.html"
    
    def get_queryset(self):
        return Post.objects.filter(publish=True)
    

class UserListView(ListView):
    
    model = Post
    template_name = "core/user.html"
    
        def get_queryset(self):
        return Post.objects.filter(publish=True)
    
    
class CreatePostView(CreateView):
    
    model = Post
    template_name = "core/create.html"
    form_class = CreateForm
    success_url = "/"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePostView, self).form_valid(form)
    
    
class DetailPostView(DetailView):
    
    model = Post
    template_name = "core/detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Post
    template_name = "core/update.html"
    form_class = UpdateForm
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
    

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
    model = Post
    template_name = "core/delete.html"
    success_url = "/"
    
    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Post, pk=pk_)
    
    def get_success_url(self):
        return reverse("core:home")
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False