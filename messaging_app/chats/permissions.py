from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Only authenticated users who are participants of a conversation
    can view, update, delete, or create messages.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'sender') and obj.sender == request.user:
            return True
        if hasattr(obj, 'receiver') and obj.receiver == request.user:
            return True
        if hasattr(obj, 'participants') and request.user in obj.participants.all():
            return True
        return False
