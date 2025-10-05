from django.urls import path
from . import views

urlpatterns = [
    path("inbox/", views.inbox, name="inbox"),
    path("delete_user/", views.delete_user, name="delete_user"),
    path("threaded_conversation/", views.threaded_conversation, name="threaded_conversation"),
]
