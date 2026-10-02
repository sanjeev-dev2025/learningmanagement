from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "email", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")

    # Fields shown when editing an existing user
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {"fields": ("role",)}),
    )

    # Fields shown when creating a new user from admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Custom Fields", {"fields": ("email", "role")}),
    )


admin.site.register(User, CustomUserAdmin)