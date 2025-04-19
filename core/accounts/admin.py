from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
from .forms import UserCreationForm, UserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("phone_number", "is_superuser", "is_staff", "is_active", "is_verified")
    list_filter = ("phone_number", "is_staff", "is_active", "is_verified")
    fieldsets = (
        ("Authentication", {"fields": ("phone_number", "password")}),
        (
            "Permissions",
            {"fields": ("is_superuser", "is_staff", "is_active", "is_verified")},
        ),
        ("Group Permissions", {"fields": ("groups", "user_permissions")}),
        ("User Logs", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            "Authentication",
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "password1",
                    "password2",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "is_verified",
                ),
            },
        ),
    )
    search_fields = ("phone_number",)
    ordering = ("phone_number",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "email", "first_name", "last_name")
    searching_fields = ("user", "email", "first_name", "last_name")


admin.site.register(User, CustomUserAdmin)
