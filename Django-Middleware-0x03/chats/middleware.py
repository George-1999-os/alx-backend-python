# chats/middleware.py
from django.http import HttpResponseForbidden

class RolePermissionMiddleware:
    """
    Middleware that restricts access based on user role.
    Only users with role 'admin' or 'moderator' are allowed.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check user role if logged in
        user = getattr(request, "user", None)
        if user and user.is_authenticated:
            # Assume user model has a 'role' field
            role = getattr(user, "role", None)
            if role not in ["admin", "moderator"]:
                return HttpResponseForbidden("You do not have permission to access this resource.")

        return self.get_response(request)
