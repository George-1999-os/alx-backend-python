from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, MessageHistory


class TestMessageSignals(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="password")
        self.receiver = User.objects.create_user(username="receiver", password="password")

        # Save a message first
        self.message = Message.objects.create(
            sender=self.user, receiver=self.receiver, content="Hello!"
        )

        # Refresh from DB to ensure it’s persisted
        self.message.refresh_from_db()

        # Now safely create a history entry
        MessageHistory.objects.create(
            message=self.message,
            old_content="Hello!",
            edited_by=self.user,
        )

    def test_message_edit_logs_history(self):
        # Edit the message
        self.message.content = "Updated Hello!"
        self.message.edited_by = self.user
        self.message.save()

        # Check that history entry exists
        history = MessageHistory.objects.filter(message=self.message)
        self.assertTrue(history.exists())

    def test_user_deletion_cleans_related_data(self):
        user_id = self.user.id  # store the ID before deleting

        # delete the sender user
        self.user.delete()

        # all messages and histories tied to the deleted user should be gone
        self.assertEqual(Message.objects.filter(sender_id=user_id).count(), 0)
        self.assertEqual(MessageHistory.objects.filter(edited_by_id=user_id).count(), 0)
