from django.shortcuts import render
from blog.forms import PostForm
from django.utils import timezone
from blog.models import Post
from django.views.generic import (TemplateView,ListView,DetailView,
                                   CreateView)

# Create your views here.
class base(TemplateView):
      template_name = 'base.html'

class AboutView(TemplateView):
      template_name = 'about.html'

class CareerView(TemplateView):
      template_name = 'career.html'

class BlogView(TemplateView):
      template_name = 'blogs.html'

class PostListView(ListView):
      model = Post

      def get_queryset(self):
           return Post.objects.filter(date__lte=timezone.now()).order_by('-date')

class PostDetailView(DetailView):
       model = Post

class CreatePostView(CreateView):
    form_class = PostForm
    model = Post
