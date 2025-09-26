# chats/views.py
from django.http import JsonResponse

def chat_home(request):
    """
    Simple endpoint for the chat page.
    Returns a welcome message as JSON.
    """
    return JsonResponse({"message": "Welcome to the chat!"})
