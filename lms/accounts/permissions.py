from rest_framework.permissions import BasePermission
from accounts.models import User

class IsAdminUser(BasePermission):
    def has_permissions(self,request,view):
        return request.user and request.user.is_autheticated and request.user.role=="ADMIN"
class IsTeacher(BasePermission):
    def has_permissions(self,request,view):
        return request.user and request.user.is_autheticated and request.user.role=="TEACHER"
class IsStudent(BasePermission):
    def has_permissions(self,request,view):
        return request.user and request.user.is_authenticated and request.user.role=="STUDENT"
