# chats/middleware.py

import time
from datetime import datetime
from django.http import HttpResponseForbidden

# --------------------------
# 1. Request Logging Middleware
# --------------------------
class RequestLoggingMiddleware:
    """
    Logs incoming requests and outgoing responses.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"Request: {request.method} {request.path}")
        response = self.get_response(request)
        print(f"Response status: {response.status_code}")
        return response

# --------------------------
# 2. Restrict Access By Time Middleware
# --------------------------
class RestrictAccessByTimeMiddleware:
    """
    Middleware that restricts access to chat outside allowed hours.
    Users cannot access chat between 9 PM (21:00) and 6 AM (06:00).
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/chat/'):
            current_hour = datetime.now().hour
            if current_hour >= 21 or current_hour < 6:
                return HttpResponseForbidden(
                    "Chat is unavailable between 9 PM and 6 AM."
                )
        return self.get_response(request)

# --------------------------
# 3. Offensive Language / Rate Limit Middleware
# --------------------------
class OffensiveLanguageMiddleware:
    """
    Middleware that limits the number of chat messages a user can send
    from a single IP address. Maximum 5 messages per 1 minute.
    """
    MESSAGE_LIMIT = 5
    TIME_WINDOW = 60  # seconds

    ip_message_log = {}

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST" and request.path.startswith('/chat/'):
            ip = self.get_client_ip(request)
            now = time.time()
            
            if ip not in self.ip_message_log:
                self.ip_message_log[ip] = []
            
            # Remove timestamps older than TIME_WINDOW
            self.ip_message_log[ip] = [t for t in self.ip_message_log[ip] if now - t < self.TIME_WINDOW]

            if len(self.ip_message_log[ip]) >= self.MESSAGE_LIMIT:
                return HttpResponseForbidden(
                    f"Message limit exceeded: Max {self.MESSAGE_LIMIT} messages per minute."
                )

            self.ip_message_log[ip].append(now)

        return self.get_response(request)

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

        # --------------------------
# 4. Role Permission Middleware
# --------------------------
class RolePermissionMiddleware:
    """
    Middleware that allows only users with specific roles (admin or moderator)
    to access certain chat actions.
    """
    ALLOWED_ROLES = ["admin", "moderator"]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only enforce for chat URLs
        if request.path.startswith('/chat/'):
            user = getattr(request, "user", None)
            if not user or not hasattr(user, "role") or user.role not in self.ALLOWED_ROLES:
                return HttpResponseForbidden(
                    "You do not have permission to perform this action."
                )
        return self.get_response(request)

