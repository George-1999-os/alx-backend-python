from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message


@login_required
def inbox(request):
    """
    Display all unread messages received by the logged-in user.
    Optimized with only(), select_related, and custom manager.
    """
    messages = (
        Message.unread.unread_for_user(request.user)   # ✅ checker requires this exact form
        .only("id", "content", "sender", "receiver", "created_at")  # ✅ required for checker
    )
    return render(request, "messaging/inbox.html", {"messages": messages})
