from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from chats.views import MessageViewSet, ConversationViewSet
from chats.auth import urlpatterns as auth_urls

# Initialize DRF router
router = DefaultRouter()
router.register(r'messages', MessageViewSet)
router.register(r'conversations', ConversationViewSet)

urlpatterns = [
    # Authentication endpoints
    path('api/auth/', include(auth_urls)),

    # JWT token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Main API routes
    path('api/', include(router.urls)),
]
