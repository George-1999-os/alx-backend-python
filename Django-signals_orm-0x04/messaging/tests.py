from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class SignalTests(TestCase):
    def test_notification_created_on_message(self):
        sender = User.objects.create_user(username='alice', password='password')
        receiver = User.objects.create_user(username='bob', password='password')

        Message.objects.create(
            sender=sender,
            receiver=receiver,
            content="Hello Bob!"
        )

        self.assertEqual(Notification.objects.count(), 1)
        note = Notification.objects.first()
        self.assertEqual(note.user, receiver)
