from rest_framework import permissions


class ManagerRequired(permissions.BasePermission):
    messafge = "Only managers can make these request"

    def has_permission(self, request, view):
        manager = getattr(request.user, 'manager', None)
        return request.user.is_authenticated() and manager