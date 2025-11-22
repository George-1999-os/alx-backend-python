from rest_framework import permissions

class IsOwnerOrParticipant(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'sender') and obj.sender == request.user:
            return True
        if hasattr(obj, 'receiver') and obj.receiver == request.user:
            return True
        if hasattr(obj, 'participants') and request.user in obj.participants.all():
            return True
        return False
