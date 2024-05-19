from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        """Actually in here allow users to view other users but only able to make changes to their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
