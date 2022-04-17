from django.contrib import admin

from apps.inventory.models import (
    Brand,
    Category,
    Media,
    Product,
    ProductAttribute,
    ProductAttributeValue,
    ProductInventory,
    ProductInventoryAttributeValue,
    ProductType,
)


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "slug",
        "is_active",
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "slug",
        "web_id",
        "description",
        "is_active",
        "created_at",
        "updated_at",
    ]


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]


class BrandAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]


class ProductInventoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "sku",
        "is_active",
        "retail_price",
        "stock_price",
        "sale_price",
        "created_at",
        "updated_at",
    ]


class MediaAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "image",
        "alt_text",
        "is_active",
        "created_at",
        "updated_at",
    ]


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
        "is_active",
        "created_at",
        "updated_at",
    ]


class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "value",
        "description",
        "is_active",
        "created_at",
        "updated_at",
    ]


admin.site.register(
    Category,
    CategoryAdmin,
)

admin.site.register(
    Product,
    ProductAdmin,
)

admin.site.register(
    ProductType,
    ProductTypeAdmin,
)

admin.site.register(
    Brand,
    BrandAdmin,
)

admin.site.register(
    ProductInventory,
    ProductInventoryAdmin,
)

admin.site.register(
    Media,
    MediaAdmin,
)

admin.site.register(
    ProductAttribute,
    ProductAttributeAdmin,
)

admin.site.register(
    ProductAttributeValue,
    ProductAttributeValueAdmin,
)

admin.site.register(
    ProductInventoryAttributeValue,
)
