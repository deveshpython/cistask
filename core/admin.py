from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'deadline', 'status', 'created_at')
    search_fields = ('title', 'assigned_to__username')
    list_filter = ('status', 'deadline')

