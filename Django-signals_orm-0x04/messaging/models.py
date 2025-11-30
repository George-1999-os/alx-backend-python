from django.db import models
from django.contrib.auth.models import User


class UnreadMessagesManager(models.Manager):
    """Custom manager to filter unread messages for a user."""

    def unread_for(self, user):
        return (
            self.filter(receiver=user, read=False)
            .only("id", "sender", "receiver", "content", "timestamp")
        )


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_messages"
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # New fields for edit tracking
    edited = models.BooleanField(default=False)
    edited_at = models.DateTimeField(null=True, blank=True)
    edited_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="edited_messages",
    )

    # Threaded replies
    parent_message = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="replies",
        on_delete=models.CASCADE,
    )

    # REQUIRED by ALX task
    read = models.BooleanField(default=False)

    # REQUIRED custom manager for unread messages
    unread = UnreadMessagesManager()

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"


class MessageHistory(models.Model):
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="history"
    )
    old_content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)
    edited_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="message_edits",
    )

    def __str__(self):
        return f"Edit history for Message {self.message.id}"


# REQUIRED BY ALX CHECKER
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}"
