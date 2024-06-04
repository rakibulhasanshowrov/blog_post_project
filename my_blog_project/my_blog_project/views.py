from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
def Index(request):
    return HttpResponseRedirect(reverse('app_blog:blog_list'))