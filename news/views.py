from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostList(ListView):
    model = Post
    queryset = Post.objects.order_by('-data_creations')
    # ordering = '-data_creations'
    template_name = 'news.html'
    context_object_name = 'news'




class PostDetail(DetailView):
    model = Post
    template_name = 'new_s.html'
    context_object_name = 'new_s'

