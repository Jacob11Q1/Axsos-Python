from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Blog, Comment, Admin

# Display all blogs + form to create blog + comments
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/index.html', {'blogs': blogs})

# Create a new blog
def create(request):
    if request.method == "POST":
        errors = Blog.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/blogs')
        Blog.objects.create(
            name=request.POST['name'],
            desc=request.POST['desc']
        )
        messages.success(request, "Blog successfully created")
        return redirect('/blogs')

# Edit blog page
def edit(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blogs/edit.html', {'blog': blog})

# Update blog
def update(request, id):
    if request.method == "POST":
        errors = Blog.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/blogs/edit/{id}')
        blog = Blog.objects.get(id=id)
        blog.name = request.POST['name']
        blog.desc = request.POST['desc']
        blog.save()
        messages.success(request, "Blog successfully updated")
        return redirect('/blogs')

# Delete blog
def delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.success(request, "Blog deleted")
    return redirect('/blogs')

# Create comment for a blog
def create_comment(request, blog_id):
    if request.method == "POST":
        comment_text = request.POST.get('comment', '')
        if len(comment_text) < 1:
            messages.error(request, "Comment cannot be empty")
            return redirect('/blogs')
        blog = Blog.objects.get(id=blog_id)
        Comment.objects.create(comment=comment_text, blog=blog)
        messages.success(request, "Comment added")
        return redirect('/blogs')

# Delete comment
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    messages.success(request, "Comment deleted")
    return redirect('/blogs')
