from django.contrib import admin
from .models import Line, Category, Product


@admin.register(Line)
class LineAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "created_at",
        "deleted_at",
        "updated_at",
    ]
    list_display_links = [
        "name",
    ]
    ordering = [
        "name",
    ]
    readonly_fields = [
        "created_at",
        "deleted_at",
        "updated_at",
    ]
    search_fields = [
        "name",
    ]
    prepopulated_fields = {
        "slug": [
            "name",
        ]
    }


@admin.register(Category)
class LineAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "line",
        "created_at",
        "deleted_at",
        "updated_at",
    ]
    list_display_links = ["name", "line"]
    ordering = [
        "name",
    ]
    readonly_fields = [
        "created_at",
        "deleted_at",
        "updated_at",
    ]
    search_fields = ["name", "line"]
    prepopulated_fields = {
        "slug": [
            "name",
        ]
    }


@admin.register(Product)
class LineAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "sku",
        "line",
        "category",
        "quantity",
        "price",
        "price_before",
        "tag",
        "is_available",
        "created_at",
        "deleted_at",
        "updated_at",
    ]
    list_display_links = [
        "name",
        "sku",
        "line",
        "category",
    ]
    list_editable = [
        "quantity",
        "tag",
    ]
    ordering = ["line", "category", "name", "sku"]
    readonly_fields = [
        "created_at",
        "deleted_at",
        "updated_at",
    ]
    search_fields = [
        "name",
        "sku",
        "line",
        "category",
        "tag",
        "is_available",
    ]
    prepopulated_fields = {
        "slug": [
            "name",
            "sku",
        ]
    }
