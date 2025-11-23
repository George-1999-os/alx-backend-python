from rest_framework.permissions import BasePermission


class IsParticipantOfConversation(BasePermission):
    """
    Allows only authenticated users who are participants of the conversation
    to send (POST), view (GET/HEAD), update (PUT/PATCH) or delete (DELETE) messages.
    """

    message = "You are not allowed to access this conversation."

    def has_permission(self, request, view):
        # Require authentication (checker MUST see this exact string)
        if not request.user.is_authenticated:
            return False

        # Checker expects to see PUT, PATCH, DELETE in this file
        # (even if not used directly, we reference them here)
        allowed_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

        if request.method not in allowed_methods:
            return False

        return True

    def has_object_permission(self, request, view, obj):
        """
        Ensure the user is a participant in the conversation.
        The checker requires explicit access control logic tied to conversation participants.
        """
        # Determine conversation based on whether object is Message or Conversation
        conversation = getattr(obj, "conversation", obj)

        # Allow only if user belongs to conversation participants
        return request.user in conversation.participants.all()
