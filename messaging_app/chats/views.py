from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Message, Conversation
from .serializers import MessageSerializer, ConversationSerializer
from .permissions import IsParticipantOfConversation

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsParticipantOfConversation]

    def get_queryset(self):
        return Conversation.objects.filter(participants=self.request.user)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsParticipantOfConversation]

    def get_queryset(self):
        conversation_id = self.request.query_params.get('conversation_id')
        if conversation_id:
            return Message.objects.filter(
                conversation__id=conversation_id,
                conversation__participants=self.request.user
            )
        return Message.objects.none()
