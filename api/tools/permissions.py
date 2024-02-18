from rest_framework import permissions


class IsDriverUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'Driver'


class IsClientUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'Client'


class IsCompanyUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'Company'


class IsAdministratorUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'Administrator'


def get_user_info(user):
    if user.role == 'Client':
        data = {
            'name': user.client_full_name.name,
            'avatar': f'http://5.182.26.56/{user.client_avatar.image.url}'
        }
        return data
    if user.role == 'Company':
        data = {
            'name': user.logistic_company.company_name,
            'avatar': f'http://5.182.26.56/{user.logistic_company.avatar.url}'
        }
        return data
    if user.role == 'Driver':
        data = {
            'name': user.driver_full_name.name,
            'avatar': f'http://5.182.26.56/{user.driver_avatar.image.url}'
        }
        return data
