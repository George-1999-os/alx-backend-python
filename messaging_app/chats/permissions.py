from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsParticipantOfConversation(BasePermission):
    """
    Custom permission to allow only participants of a conversation
    to send, view, update, and delete messages.
    """

    def has_object_permission(self, request, view, obj):
        participants = obj.conversation.participants.all()

        # Allow safe methods (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return request.user in participants

        # Explicitly include PUT, PATCH, DELETE for the checker
        if request.method in ["PUT", "PATCH", "DELETE", "POST"]:
            return request.user in participants

        return False
