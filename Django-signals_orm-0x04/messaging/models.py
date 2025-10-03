from django.db import models
from django.contrib.auth.models import User


class UnreadMessagesManager(models.Manager):
    def unread_for_user(self, user):
        return (
            super().get_queryset()
            .filter(receiver=user, read=False)
            .only("id", "sender", "receiver", "content", "created_at")  # optimize
            .select_related("sender", "receiver")  # optimization
        )


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)  # ✅ required

    # parent_message already added from previous task
    parent_message = models.ForeignKey(
        "self", null=True, blank=True, related_name="replies", on_delete=models.CASCADE
    )

    objects = models.Manager()  # default manager
    unread = UnreadMessagesManager()  #  custom manager

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"
