from django.http import JsonResponse

def chat_view(request):
    return JsonResponse({"message": "Hello from chat_view!"})
