from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from chats.views import MessageViewSet, ConversationViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet)
router.register(r'conversations', ConversationViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/chats/', include(router.urls)),
]
