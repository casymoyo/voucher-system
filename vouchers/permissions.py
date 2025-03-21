from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow admins full access but restrict others to read-only.
    """
    
    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS requests for all authenticated users
        if request.method in permissions.SAFE_METHODS:
            return True
            
        return request.user and request.user.is_staff