from datetime import datetime
import logging

# Configure logger to write to requests.log
logger = logging.getLogger("request_logger")
handler = logging.FileHandler("requests.log")
formatter = logging.Formatter("%(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, "user", None)
        username = user.username if user and user.is_authenticated else "Anonymous"
        logger.info(f"{datetime.now()} - User: {username} - Path: {request.path}")
        return self.get_response(request)
