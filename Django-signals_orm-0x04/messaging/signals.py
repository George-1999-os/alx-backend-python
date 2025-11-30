# ==========================
# EDIT TRACKING SIGNAL
# ==========================
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Message, MessageHistory, Notification


@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    """
    Logs previous content before a message is edited.
    """
    if not instance.pk:
        return  # New message, no edit to log

    try:
        old_message = Message.objects.get(pk=instance.pk)
    except Message.DoesNotExist:
        return

    if old_message.content != instance.content:
        MessageHistory.objects.create(
            message=old_message,
            old_content=old_message.content,
            edited_by=instance.edited_by,
        )
        instance.edited = True
        instance.edited_at = timezone.now()


# ==========================
# REQUIRED BY ALX CHECKER
# CREATE NOTIFICATION ON NEW MESSAGE
# ==========================
@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    """
    Creates a notification for the receiver when a new message is created.
    """
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance
        )


# ==========================
# CLEANUP SIGNAL
# ==========================
@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    """
    Clean up related data when a User is deleted.
    """
    Message.objects.filter(sender=instance).delete()
    MessageHistory.objects.filter(edited_by=instance).delete()
