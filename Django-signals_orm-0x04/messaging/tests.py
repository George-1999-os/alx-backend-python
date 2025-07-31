from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class SignalTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='sender', password='testpass')
        self.user2 = User.objects.create_user(username='receiver', password='testpass')

    def test_notification_created_on_message(self):
        message = Message.objects.create(
            sender=self.user1,
            receiver=self.user2,
            content="Hello, test!"
        )
        self.assertEqual(Notification.objects.count(), 1)
        notification = Notification.objects.first()
        self.assertEqual(notification.user, self.user2)
        self.assertEqual(notification.message, message)
