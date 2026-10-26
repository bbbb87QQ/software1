# backend/accounts/urls.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserReservationHistoryView

urlpatterns = [
    # JWT 認證
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # 個人中心：歷史借用紀錄與狀態追蹤 API
    path('my-reservations/', UserReservationHistoryView.as_view(), name='user_reservations'),
]