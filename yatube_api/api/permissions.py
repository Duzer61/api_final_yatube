from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    message = 'Можно редактировать и удалять только свои записи!'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user