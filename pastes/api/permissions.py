from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    message = "you dont have the permission to view this paste, you may ask the owner to grand you permission"
    def has_object_permission(self, request, view, obj):
        my_safe_method = ['GET']
        if request.method in my_safe_method:
            if obj.privacy == "only_me":
                return obj.author == str(request.user)
            elif obj.privacy == "public":
                return True
            elif (obj.privacy == "custome") and (str(request.user) in str(obj.allow.all())):
                return True
        return obj.author == str(request.user)