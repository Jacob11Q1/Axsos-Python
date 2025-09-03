from django.shortcuts import render, redirect


# Create your views here.

# Display all blogs
def index(request):
    return render(request, 'blogs/index.html')

# Display form to create a new blog
def new(request):
    return render(request, 'blogs/new.html')

# Create a blog (redirect to /blogs)
def create(request):
    return redirect('/blogs')

# Display a single blog
def show(request, number):
    return render(request, 'blogs/show.html', {'number': number})

# Display edit form for a blog
def edit(request, number):
    return render(request, 'blogs/edit.html', {'number': number})

# Delete a blog (redirect to /blogs)
def destroy(request, number):
    return redirect('/blogs')