from django.urls import path
from .views import inbox  #  match the view name

urlpatterns = [
    path('inbox/', inbox, name='inbox'),
]
