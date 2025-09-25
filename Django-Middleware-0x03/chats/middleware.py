import datetime
from django.http import HttpResponseForbidden

class RequestLoggingMiddleware:
    """
    Middleware that logs each request to requests.log
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log request
        with open("requests.log", "a") as f:
            f.write(f"{datetime.datetime.now()} - {request.method} {request.path}\n")

        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware:
    """
    Deny access to the chat outside 6AM–9PM server time.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only restrict chat URLs
        if request.path.startswith("/chat/"):
            # TEMPORARY: simulate blocked hour for testing
            now_hour = 23
            if not (6 <= now_hour < 21):
                # Log denied access
                with open("requests.log", "a") as f:
                    f.write(f"{datetime.datetime.now()} - DENIED {request.method} {request.path}\n")
                return HttpResponseForbidden("Chat is only available between 6AM and 9PM.")
        return self.get_response(request)
