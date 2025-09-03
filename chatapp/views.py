from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def chat_list(request):
    """
    A simple DRF view that returns a sample chat list.
    """
    sample_chats = [
        {"id": 1, "message": "Hello from chatapp!", "sender": "System"},
        {"id": 2, "message": "This is a demo message.", "sender": "Bot"},
    ]
    return Response(sample_chats)
