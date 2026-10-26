# backend/accounts/serializers.py
from rest_framework import serializers

class UserReservationHistorySerializer(serializers.Serializer):
    """
    定義回傳給前端的個人借用紀錄 JSON 格式
    """
    id = serializers.IntegerField(read_only=True)
    room_name = serializers.CharField(read_only=True)
    start_time = serializers.DateTimeField(read_only=True)
    end_time = serializers.DateTimeField(read_only=True)
    reason = serializers.CharField(read_only=True)
    status = serializers.CharField(read_only=True)       # PENDING (審核中), APPROVED (核准), REJECTED (駁回)
    created_at = serializers.DateTimeField(read_only=True)