# backend/accounts/permissions.py
from rest_framework.permissions import BasePermission

class IsAdminUserRole(BasePermission):
    """
    僅允許管理員身分存取的權限檢查
    """
    def has_permission(self, request, view):
        # 判斷是否為登入使用者，且具備管理員權限 (相容 Django 內建 is_staff 或是自訂 role)
        return bool(
            request.user and 
            request.user.is_authenticated and 
            (getattr(request.user, 'is_staff', False) or getattr(request.user, 'role', '') == 'ADMIN')
        )

class IsStudentUserRole(BasePermission):
    """
    僅允許一般學生/借用者身分存取的權限檢查
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)