from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DetailView,View,TemplateView,DeleteView,TemplateView
from .models import Blog,Comment,Likes
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
# Create your views here.


class CreateBlog(CreateView):
    model=Blog
    template_name='app_blog/create_blog.html'
    fields=('blog_title','blog_content','blog_image',)
    
    
    def form_valid(self, form):
        blog_obj= form.save(commit=False)
        blog_obj.author=self.request.user
        title=blog_obj.blog_title
        blog_obj.slug=title.replace(' ','-') + '-' + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse("index"))

class BlogList(ListView):
    context_object_name = 'blogs'
    model=Blog
    template_name='app_blog/blog_list.html'
    # queryset=Blog.objects.order_by('-publish_date')