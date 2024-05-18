from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Human


@admin.register(Human)
class HumanAdmin(UserAdmin):
    list_display = [
        "email",
        "user_name",
        "date_joined",
        "last_login",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    search_fields = ["email"]
    readonly_fields = ["date_joined", "last_login"]
    filter_horizontal = ()
    list_filter = []
    fieldsets = ()
    ordering = [
        "user_name",
    ]
