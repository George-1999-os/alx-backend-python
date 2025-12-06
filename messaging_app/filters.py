import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    sender = django_filters.CharFilter(field_name="sender__username", lookup_expr='icontains')
    recipient = django_filters.CharFilter(field_name="recipient__username", lookup_expr='icontains')
    start_date = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = Message
        fields = ['sender', 'recipient', 'start_date', 'end_date']
