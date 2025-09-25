import datetime

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
