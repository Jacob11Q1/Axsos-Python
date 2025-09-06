from django.shortcuts import render
from .models import Blog

# Create your views here.

def index(request):
    blogs = Blog.objects.all()  # get all blogs
    return render(request, 'blogs/index.html', {'blogs': blogs})