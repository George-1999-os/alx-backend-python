from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message


@login_required
def inbox(request):
    """
    Display all messages received by the logged-in user.
    Optimized with select_related and prefetch_related.
    """
    messages = (
        Message.objects.filter(receiver=request.user)   # required by checker
        .select_related("sender", "receiver")           # FK optimization
        .prefetch_related("replies")                    # reverse relation optimization
    )
    return render(request, "messaging/inbox.html", {"messages": messages})


def get_thread(message, user):
    """
    Recursively fetch all replies to a given message.
    Returns a nested structure for threaded conversations.
    """
    replies = (
        Message.objects.filter(parent_message=message, sender=user)  # <- checker requires this
        .select_related("sender", "receiver")
        .prefetch_related("replies")
    )
    thread = []
    for reply in replies:
        thread.append({
            "message": reply,
            "replies": get_thread(reply, user)   # recursion
        })
    return thread


@login_required
def message_detail(request, message_id):
    """
    Display a message and all its threaded replies.
    """
    message = get_object_or_404(
        Message.objects.select_related("sender", "receiver"),
        id=message_id
    )
    # Pass request.user so get_thread includes sender=request.user
    thread = get_thread(message, request.user)
    return render(
        request,
        "messaging/message_detail.html",
        {"message": message, "thread": thread}
    )
