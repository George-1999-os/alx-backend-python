from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # 👇 Add this for threaded conversations
    parent_message = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name="replies",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.sender} → {self.recipient}: {self.content[:30]}"
