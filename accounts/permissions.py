from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView

SAFE_METHODS = ("GET", "HEAD", "OPTIONS")


class IsManager(permissions.BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_manager


class IsAccountantOrIsManager(permissions.BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_manager or request.user.is_accountant
