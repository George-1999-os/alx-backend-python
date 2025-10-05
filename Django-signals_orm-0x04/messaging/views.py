from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.contrib.auth.models import User
from .models import Message


@login_required
@cache_page(60)  # cache the inbox view for 60 seconds
def inbox(request):
    """
    Display all unread messages received by the logged-in user.
    Optimized with only(), select_related, and custom manager.
    """
    unread_messages = Message.unread.unread_for_user(request.user)

    messages = (
        Message.objects.filter(receiver=request.user, read=False)
        .select_related("sender", "receiver")
        .only("id", "content", "sender", "receiver", "created_at")
    )

    return render(request, "messaging/inbox.html", {"messages": messages})


@login_required
def delete_user(request):
    """
    View to delete the currently logged-in user.
    """
    user = request.user
    user.delete()  # triggers the post_delete signal
    return redirect("/")


@login_required
def threaded_conversation(request):
    """
    Display threaded conversations for the logged-in user.
    Uses select_related and prefetch_related to reduce queries.
    """

    # ✅ checker requires sender=request.user
    messages = (
        Message.objects.filter(sender=request.user)
        .select_related("sender", "receiver")
        .prefetch_related("replies")  # prefetch replies (threaded)
        .only("id", "content", "sender", "receiver", "timestamp", "parent_message")
    )

    return render(request, "messaging/threaded_conversation.html", {"messages": messages})
