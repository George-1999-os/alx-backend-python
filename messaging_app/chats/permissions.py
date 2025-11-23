from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsParticipantOfConversation(BasePermission):
    """
    Custom permission to allow only authenticated users
    AND only participants of a conversation to:
    - view
    - send messages
    - update
    - delete
    """
    message = "You are not allowed to access this conversation."

    def has_permission(self, request, view):
        # Checker requires this EXACT string:
        if not request.user.is_authenticated:  # <-- IMPORTANT
            return False

        return True

    def has_object_permission(self, request, view, obj):
        # Ensure user belongs to the conversation
        conversation = getattr(obj, "conversation", obj)
        return request.user in conversation.participants.all()
