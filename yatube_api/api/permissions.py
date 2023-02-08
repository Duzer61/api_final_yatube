from django.shortcuts import get_object_or_404
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    message = 'У вас недостаточно прав для выполнения данного действия.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user


#class IsNotAuthorOrDenied(permissions.BasePermission):


    #def has_permission(self, request, view):
    #    if request.method in permissions.SAFE_METHODS:
    #        return True
    #    following = get_object_or_404(User, username=request.following)
    #    if request.user == request.following:
    #        message = 'Нельзя подписываться на самого себя!'
    #        return False
    #    return True
#
#
#
    #def has_object_permission(self, request, view, obj):
    #    if request.method in permissions.SAFE_METHODS:
    #        return True
#
    #    if obj.author != request.user:
    #        message = 'Можно удалять только свои записи'
    #        return False
    #    return True