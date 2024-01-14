from django.shortcuts import render
from .models import post

# Create your views here.
def vblog(request):
    posts = post.objects.all()
    
    return render(request, 'blog/blog.html',{'posts': posts})
