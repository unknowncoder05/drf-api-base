"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from api.users.models import User, Profile


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'created_at', 'updated_at')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user', )
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    # list_filter = ('reputation',)


admin.site.register(User, CustomUserAdmin)
