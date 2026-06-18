from rest_framework import permissions


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    """Права доступа: только автор или админ может изменять/удалять."""
    
    def has_object_permission(self, request, view, obj):
        # Для безопасных методов (GET, HEAD, OPTIONS) - доступ есть
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Изменять/удалять может только автор или админ
        return obj.creator == request.user or request.user.is_staff