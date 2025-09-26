# chats/middleware.py
from datetime import datetime
from django.http import HttpResponseForbidden

class RequestLoggingMiddleware:
    """
    Middleware to log incoming requests for debugging/audit purposes.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"[RequestLoggingMiddleware] {request.method} {request.path}")
        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    """
    Middleware that restricts access to chat outside allowed hours.
    Users cannot access chat between 9 PM (21:00) and 6 AM (06:00).
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Restrict access only to chat URLs
        if request.path.startswith('/chat/'):
            current_hour = datetime.now().hour
            if current_hour >= 21 or current_hour < 6:
                return HttpResponseForbidden(
                    "Chat is unavailable between 9 PM and 6 AM."
                )

        response = self.get_response(request)
        return response


class OffensiveLanguageMiddleware:
    """
    Placeholder middleware for offensive language filtering.
    Currently does nothing.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Just pass the request through for now
        response = self.get_response(request)
        return response
