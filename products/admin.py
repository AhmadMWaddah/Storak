from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category

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
    search_fields = ["name", "line"]
    prepopulated_fields = {
        "slug": [
            "name",
        ]
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    list_display = [
        "name",
        "sku",
        "category",
        "inventory",
        "price",
        "price_before",
        "badge",
        "in_stock",
        "created_at",
        "deleted_at",
        "updated_at",
    ]
    list_display_links = [
        "name",
        "sku",
        "category",
    ]
    list_editable = [
        "inventory",
        "in_stock",
        "badge",
    ]
    ordering = [
        "category",
        "name",
        "sku",
    ]
    readonly_fields = [
        "created_at",
        "deleted_at",
        "updated_at",
    ]
    search_fields = [
        "name",
        "sku",
        "category",
        "badge",
        "in_stock",
    ]
    prepopulated_fields = {
        "slug": [
            "name",
            "sku",
        ]
    }
