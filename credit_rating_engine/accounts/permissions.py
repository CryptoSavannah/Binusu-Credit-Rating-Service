from rest_framework.permissions import BasePermission
from .models import User

class ClientPermissions(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.is_active
