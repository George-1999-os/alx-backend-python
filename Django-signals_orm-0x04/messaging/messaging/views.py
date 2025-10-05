from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message


@login_required
def inbox(request):
    messages = (
        Message.objects.filter(recipient=request.user)
        .select_related("sender", "recipient", "parent_message")
        .prefetch_related("replies__sender")
        .order_by("-created_at")
    )
    return render(request, "messaging/inbox.html", {"messages": messages})
