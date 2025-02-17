"""
admin.py

Register the NewUser custom model on the admin portal.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser

class UserAdminConfig(UserAdmin):
    """
    custom layout for user model in admin portal

    :param UserAdmin: Django class to customise the user interface
    """

    search_fields = ("email", "user_name", "first_name")
    list_filter = ("email", "user_name", "is_active", "is_superuser")
    ordering = ("-created_at",)
    list_display = ("email", "user_name", "first_name", "is_active", "is_superuser")

    fieldsets = (
        (None, {"fields": ("email", "user_name", "first_name", "last_name",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Personal", {"fields": ("about", "location", "phone_number")})
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "user_name", "first_name", "last_name", "password1", 
                        "password2", "is_active", "is_staff")
        }),
    )

admin.site.register(NewUser, UserAdminConfig)
