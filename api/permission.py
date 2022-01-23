from rest_framework import permissions


class ProfileUpdate(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.profile.is_done:
            return True


class ClinicPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.profile.typr == "کلینیک":
            return True


class DoctorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.profile.clinic:
            return True
