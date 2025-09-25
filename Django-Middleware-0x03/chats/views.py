from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello world!")

def chat_view(request):
    return HttpResponse("Welcome to the chat!")
