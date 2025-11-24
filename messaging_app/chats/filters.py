import django_filters
from .models import Message
from django.contrib.auth.models import User

class MessageFilter(django_filters.FilterSet):
    sender = django_filters.ModelChoiceFilter(
        field_name="sender",
        queryset=User.objects.all()
    )
    receiver = django_filters.ModelChoiceFilter(
        field_name="conversation__participants",
        queryset=User.objects.all()
    )
    created_after = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="gte"
    )
    created_before = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="lte"
    )

    class Meta:
        model = Message
        fields = ["sender", "receiver", "created_after", "created_before"]
