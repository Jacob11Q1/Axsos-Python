from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Blog, Comment, Admin

# ----------------- Blog List -----------------
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/index.html', {'blogs': blogs})

# ----------------- Blog Create -----------------
def create_blog(request):
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

# ----------------- Blog Edit Form -----------------
def edit_blog(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blogs/edit.html', {'blog': blog})

# ----------------- Blog Update -----------------
def update_blog(request, id):
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

# ----------------- Blog Delete -----------------
def delete_blog(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.success(request, "Blog successfully deleted")
    return redirect('/blogs')

# ----------------- Comment Create -----------------
def create_comment(request, blog_id):
    if request.method == "POST":
        Comment.objects.create(
            comment=request.POST['comment'],
            blog=Blog.objects.get(id=blog_id)
        )
        messages.success(request, "Comment successfully added")
    return redirect('/blogs')

# ----------------- Comment Delete -----------------
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    messages.success(request, "Comment successfully deleted")
    return redirect('/blogs')

# ----------------- Admin Create -----------------
def create_admin(request):
    if request.method == "POST":
        errors = Blog.objects.basic_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/admins/new')
        admin = Admin.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email']
        )
        # Assign blogs to admin if selected
        if 'blogs' in request.POST:
            admin.blogs.set(request.POST.getlist('blogs'))
        messages.success(request, "Admin successfully created")
    return redirect('/admins')

# ----------------- Admin List -----------------
def admin_list(request):
    admins = Admin.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'blogs/admins.html', {'admins': admins, 'blogs': blogs})
