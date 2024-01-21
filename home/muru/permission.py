from rest_framework.permissions import BasePermission

SAFE_METHODS=('GET','HEAD','OPTIONS', 'DELETE')

class personPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False
    
    def has_object_permission(self, request, view, obj):
        if obj:
            return True
        return False