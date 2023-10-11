from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
