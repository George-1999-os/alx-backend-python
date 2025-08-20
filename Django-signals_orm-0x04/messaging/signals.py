from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Message


@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    """Stub for creating a notification when a new message is sent."""
    if created:
        # Notification.objects.create(user=instance.receiver, message=instance)
        pass  # Commented out since Notification model no longer exists


@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    """
    Log the original content of a message before it's edited.
    """
    if instance.id:
        try:
            original = Message.objects.get(id=instance.id)
            if original.content != instance.content:
                # MessageHistory.objects.create(
                #     message=instance,
                #     old_content=original.content,
                #     edited_by=instance.sender
                # )
                instance.edited = True
        except Message.DoesNotExist:
            pass


@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    """
    Deletes related messages when a User is deleted.
    """
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    # Notification.objects.filter(user=instance).delete()
    # MessageHistory.objects.filter(edited_by=instance).delete()
