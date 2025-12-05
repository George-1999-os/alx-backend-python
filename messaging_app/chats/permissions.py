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
