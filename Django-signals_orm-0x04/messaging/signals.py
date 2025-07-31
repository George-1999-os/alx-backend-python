from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory


@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    """Create a notification when a new message is sent."""
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)


@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    """
    Log the original content of a message before it's edited.
    Only triggers if the message already exists and content has changed.
    """
    if instance.id:
        try:
            original = Message.objects.get(id=instance.id)
            if original.content != instance.content:
                MessageHistory.objects.create(
                    message=instance,
                    old_content=original.content
                )
                instance.edited = True
        except Message.DoesNotExist:
            pass
