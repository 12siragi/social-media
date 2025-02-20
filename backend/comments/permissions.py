# comments/permissions.py
from rest_framework import permissions

class IsCommentAuthorOrPostAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only access for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow update only if the comment author is making the request
        if request.method in ['PUT', 'PATCH']:
            return obj.user == request.user

        # Allow deletion if the request is from either the comment author or the post author
        if request.method == 'DELETE':
            return obj.user == request.user or obj.post.user == request.user

        return False
