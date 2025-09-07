from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Description, Comment
from django.contrib import messages


# Create your views here.

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc_content = request.POST.get('description')

        if len(name) < 6:
            messages.error(request, "Course name must be more than 5 characters.")
        elif len(desc_content) < 15:
            messages.error(request, "Description must be more than 15 characters.")
        else:
            desc = Description.objects.create(content=desc_content)
            Course.objects.create(name=name, description=desc)
            messages.success(request, "Course added successfully!")

        return redirect('index')

    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'courses/index.html', {'courses': courses})

def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        if request.POST.get('confirm') == 'Yes':
            course.delete()
        return redirect('index')
    return render(request, 'courses/delete_course.html', {'course': course})

def comment_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if len(content) >= 5:
            Comment.objects.create(course=course, content=content)
    comments = course.comments.all().order_by('-created_at')
    return render(request, 'courses/comments.html', {'course': course, 'comments': comments})