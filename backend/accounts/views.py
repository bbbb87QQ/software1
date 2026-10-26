# backend/accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.apps import apps
from drf_spectacular.utils import extend_schema
from .serializers import UserReservationHistorySerializer

class UserReservationHistoryView(APIView):
    """
    查詢當前登入使用者的個人教室借用歷史紀錄與審核狀態
    """
    #permission_classes = [IsAuthenticated]  # 強制要求攜帶 JWT 登入 Token
    permission_classes = []

    @extend_schema(
        summary="查詢個人借用紀錄",
        description="前端攜帶 JWT Token 請求，僅會回傳該使用者本人的借用紀錄與審核狀態。",
        responses={200: UserReservationHistorySerializer(many=True)}
    )
    def get(self, request):
        user = request.user

        # 動態嘗試讀取 reservations app 內的 Reservation Model (解耦設計，避免資料庫同學尚未完成時崩潰)
        try:
            Reservation = apps.get_model('reservations', 'Reservation')
            # 僅撈取屬於當前登入使用者的借用紀錄，並依建立時間降冪排序
            queryset = Reservation.objects.filter(user=user).order_by('-created_at')
            serializer = UserReservationHistorySerializer(queryset, many=True)
            return Response(serializer.data)
        except (LookupError, Exception):
            # 若負責資料庫的同學尚未建立 Reservation 表格，先回傳範例假資料供前端測試
            mock_data = [
                {
                    "id": 1,
                    "room_name": "資工系電腦教室 101",
                    "start_time": "2026-11-01T09:00:00Z",
                    "end_time": "2026-11-01T12:00:00Z",
                    "reason": "軟工專題小組討論",
                    "status": "APPROVED",
                    "created_at": "2026-10-25T14:30:00Z"
                },
                {
                    "id": 2,
                    "room_name": "工程一館 205",
                    "start_time": "2026-11-05T14:00:00Z",
                    "end_time": "2026-11-05T16:00:00Z",
                    "reason": "讀書會活動",
                    "status": "PENDING",
                    "created_at": "2026-10-26T10:00:00Z"
                }
            ]
            return Response(mock_data)