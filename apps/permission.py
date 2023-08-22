#
# from rest_framework.permissions import BasePermission, SAFE_METHODS
#
#
# class IsSuperUser(BasePermission):
#
#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_authenticated and request.user.is_superuser)
#
#     def has_object_permission(self, request, view, obj):
#         return self.has_permission(request, view)
#
#
# class IsAuthor(BasePermission):
#
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS or request.method.is_staff
#
#     def has_object_permission(self, request, view, obj):
#         return request.user == obj.author and request.user.is_staff or request.method in SAFE_METHODS
#
#
# class NewsCategoryPermission(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True
#         return request.user and request.user.is_superuser
#
#
# class AreaCategoryPermission(BasePermission):
#
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True
#         return request.user and request.user.is_superuser
#
#
# class PostPermissions(BasePermission):
#
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True
#         return request.user and request.user.is_superuser


from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsAuthor(BasePermission):

    def has_permission(self, request, view):
        return super().has_permission(request, view)


class NewsCategoryPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser


class AreaCategoryPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser


class PostPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser
