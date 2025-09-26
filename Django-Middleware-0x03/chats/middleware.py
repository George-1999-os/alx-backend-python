import logging
import datetime
from django.http import HttpResponseForbidden

# Configure logger
logger = logging.getLogger("request_logger")
handler = logging.FileHandler("requests.log")  # log file at project root
formatter = logging.Formatter("%(asctime)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


class RequestLoggingMiddleware:
    """Middleware that logs every request with username and path."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "AnonymousUser"
        log_message = f"User: {user} - Path: {request.path}"
        logger.info(log_message)
        return self.get_response(request)


class OffensiveLanguageMiddleware:
    """
    Middleware to limit the number of chat messages (POST requests) per IP.
    - Maximum: 5 messages per minute per IP address.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.message_log = {}  # {ip: [timestamps]}

    def __call__(self, request):
        if request.path.startswith("/chat/") and request.method == "POST":
            ip = self.get_client_ip(request)
            now = datetime.datetime.now()

            # Keep only requests within the last 60 seconds
            self.message_log[ip] = [
                ts for ts in self.message_log.get(ip, [])
                if (now - ts).seconds < 60
            ]

            # Block if limit exceeded
            if len(self.message_log[ip]) >= 5:
                return HttpResponseForbidden(
                    "Too many messages. Please wait before sending more."
                )

            # Log this request
            self.message_log[ip].append(now)

        return self.get_response(request)

    def get_client_ip(self, request):
        """Extract client IP from request."""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")
