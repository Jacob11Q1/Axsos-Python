from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages as flash
from .models import Message, Comment
from django.utils import timezone

# Create your views here.

@login_required
def wall(request):
    messages_list = Message.objects.all().order_by("-created_at")
    return render(request, "wall_app/wall.html", {"messages": messages_list})

@login_required
def add_message(request):
    if request.method == "POST":
        content = request.POST.get("content")
        if content.strip() == "":
            flash.error(request, "Message cannot be empty")
        else:
            Message.objects.create(user=request.user, content=content)
    return redirect("wall")

@login_required
def add_comment(request, message_id):
    if request.method == "POST":
        comment_text = request.POST.get("comment")
        if comment_text.strip() == "":
            flash.error(request, "Comment cannot be empty")
        else:
            message_obj = get_object_or_404(Message, id=message_id)
            Comment.objects.create(user=request.user, message=message_obj, comment=comment_text)
    return redirect("wall")

@login_required
def delete_message(request, message_id):
    message_obj = get_object_or_404(Message, id=message_id)
    if message_obj.user == request.user and message_obj.can_delete():  # Sensei bonus
        message_obj.delete()
    return redirect("wall")

@login_required
def delete_comment(request, comment_id):
    comment_obj = get_object_or_404(Comment, id=comment_id)
    if comment_obj.user == request.user:
        comment_obj.delete()
    return redirect("wall")