from django.contrib import admin
from django.urls import path
from chats.views import chat_view  # only import chat_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', chat_view, name='chat'),
]
