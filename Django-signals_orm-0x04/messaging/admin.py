from django.contrib import admin
from .models import Message, MessageHistory   # removed Notification


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'timestamp', 'edited', 'edited_at')


@admin.register(MessageHistory)
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'old_content', 'edited_at', 'edited_by')
