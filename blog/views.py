from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView
    )
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'   # set the name for model objects
    ordering = ['-date_posted']      # '-' on the beginning means reversed direction of ordering


class PostDetailView(DetailView):
    model = Post
    # default template name: blog/post-detail.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # We need to tell Django that author of created post is currently logged in user.
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # We need to tell Django that author of created post is currently logged in user.
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        # Check if user is owner of updated post
        return self.request.user == post.author


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})