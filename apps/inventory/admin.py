from django.contrib import admin

from apps.inventory.models import Category, Product


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


admin.site.register(
    Category,
    CategoryAdmin,
)

admin.site.register(
    Product,
    ProductAdmin,
)
