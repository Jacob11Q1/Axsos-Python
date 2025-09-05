# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Message, Comment
from django.contrib.auth.models import User
import datetime
import json

def index(request):
    messages = Message.objects.all().order_by('-created_at')
    users = User.objects.all()
    return render(request, 'messaging/index.html', {'messages': messages, 'users': users})

def add_comment(request, msg_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        comment_text = data.get('comment')
        msg = get_object_or_404(Message, id=msg_id)
        comment = Comment.objects.create(user=request.user, message=msg, comment=comment_text)
        return JsonResponse({'success': True, 'user': request.user.first_name, 'comment': comment_text, 'created_at': comment.created_at.strftime("%b %d, %Y %H:%M")})

def add_post(request):
    if request.method == 'POST':
        msg_text = request.POST.get('message')
        image = request.FILES.get('image')
        Message.objects.create(user=request.user, message=msg_text, image=image)
        return JsonResponse({'success': True})

def like_post(request, msg_id):
    # For demo, we just return success (implement like toggle in real model)
    return JsonResponse({'success': True})
