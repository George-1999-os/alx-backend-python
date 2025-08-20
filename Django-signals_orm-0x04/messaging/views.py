from django.shortcuts import render
from .models import Message

def inbox(request):
    unread_messages = Message.unread.unread_for_user(request.user).select_related('sender').only('content', 'timestamp', 'sender__username')
    return render(request, 'messaging/inbox.html', {'messages': unread_messages})
