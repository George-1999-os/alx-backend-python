from rest_framework import permissions

class IsOwnerOrParticipant(permissions.BasePermission):
    """
    Allow access only if user is the sender, receiver,
    or a participant of the conversation or message.
    """

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "sender") and obj.sender == request.user:
            return True
        if hasattr(obj, "receiver") and obj.receiver == request.user:
            return True
        if hasattr(obj, "participants") and request.user in obj.participants.all():
            return True
        return False


class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allow only authenticated users who are participants of a conversation
    to send, view, update, or delete messages.
    """

    message = "You are not allowed to access this conversation."

    def has_permission(self, request, view):
        # Only authenticated users can access
        if not request.user.is_authenticated:
            return False

        # Ensure allowed HTTP methods are referenced
        allowed_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        if request.method not in allowed_methods:
            return False

        return True

    def has_object_permission(self, request, view, obj):
        # Conversation could be Message or Conversation object
        conversation = getattr(obj, "conversation", obj)
        # Only participants can access
        return request.user in conversation.participants.all()
