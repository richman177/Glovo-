from rest_framework import permissions


class CheckOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == "owner":
            return True
        return False


class CheckUserReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'client':
            return True
        return False


class CheckStoreOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False