from django.contrib import admin
from django.urls import path
from chats.views import chat_home  # use chat_home instead of chat_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', chat_home, name='chat'),  # use chat_home
]
