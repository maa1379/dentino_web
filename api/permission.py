from rest_framework import permissions


class ProfileUpdate(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.profile.is_done:
            return True
