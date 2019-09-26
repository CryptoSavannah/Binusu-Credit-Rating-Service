from rest_framework.permissions import BasePermission
from .models import User

# class ClientPermissions(BasePermission):
    
#     def has_permission(self, request, view):
#         return request.user.is_client and request.user.is_active

# class MerchantPermissions(BasePermission):

#     def has_permission(self, request, view):
#         return request.user.is_merchant and request.user.is_active

# class MerchantCientPermissions(BasePermission):

#     def has_permission(self, request, view):
#         return request.user.is_merchant or request.user.is_client and request.user.is_active