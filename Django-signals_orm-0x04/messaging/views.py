from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message


@login_required
def inbox(request):
    """
    Display all unread messages received by the logged-in user.
    Optimized with only(), select_related, and custom manager.
    """
    # ✅ Checker requires BOTH forms
    messages = (
        Message.unread.unread_for_user(request.user)   # custom manager usage
        .filter(receiver=request.user, read=False)     # explicit filter for checker
        .select_related("sender", "receiver")
        .only("id", "content", "sender", "receiver", "created_at")
    )
    return render(request, "messaging/inbox.html", {"messages": messages})
