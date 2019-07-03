from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    message = "you must be the author"
    def has_object_permission(self, request, view, obj):
        my_safe_method = ['GET']
        if request.method in my_safe_method:
            return True
        return obj.author == request.user