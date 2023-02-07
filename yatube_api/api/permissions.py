from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    message = 'Можно редактировать и удалять только свои записи!'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


class IsNotAuthorOrDenied(permissions.BasePermission):


    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.username == request.following:
            message = 'Нельзя подписываться на самого себя!'
            return False
        return True



    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.author != request.user:
            message = 'Можно удалять только свои записи'
            return False
        return True