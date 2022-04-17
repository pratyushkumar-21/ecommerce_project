from email.policy import default
from operator import mod
from statistics import mode

from django.db import models


# Create your models here.
class Category(models.Model):
    """
    Inventory Category table
    """

    name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        unique=False,
        verbose_name="category name",
    )
    slug = models.SlugField(
        max_length=128,
        null=False,
        unique=False,
        blank=False,
        verbose_name="category safe url",
    )
    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        verbose_name = "Product category"
        verbose_name_plural = "Product categories"

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(
        max_length=128,
        unique=False,
        null=False,
        blank=False,
        verbose_name="product name",
    )

    slug = models.SlugField(
        max_length=128,
        unique=False,
        null=False,
        blank=False,
        verbose_name="product safe url",
    )

    web_id = models.CharField(
        max_length=128,
        unique=True,
        null=False,
        blank=False,
        verbose_name="product website id",
    )

    description = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name="product description",
    )

    category = models.ManyToManyField(Category)

    is_active = models.BooleanField(
        unique=False,
        null=False,
        blank=False,
        default=True,
        verbose_name="product visibility",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name="data product created",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="date product last update",
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class ProductType(models.Model):

    name = models.CharField(
        max_length=128,
        unique=True,
        null=False,
        blank=False,
        verbose_name="type of product",
    )

    def __str__(self):
        return self.name


class Brand(models.Model):

    name = models.CharField(
        max_length=128,
        unique=True,
        null=False,
        blank=False,
        verbose_name="type of product",
    )

    def __str__(self):
        return self.name


class ProductAttribute(models.Model):

    """product attribute list table"""

    name = models.CharField(
        max_length=128,
        blank=False,
        null=False,
        unique=False,
        verbose_name="product attribute name",
    )

    description = models.TextField(
        unique=False,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.name}"


class ProductAttributeValue(models.Model):

    """Product attribute value table"""

    product_attribute = models.ForeignKey(
        ProductAttribute,
        related_name="product_attribute_value",
        on_delete=models.PROTECT,
    )

    value = models.CharField(
        max_length=128,
        unique=False,
        null=False,
        blank=False,
    )

    description = models.TextField(
        unique=False,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"< {self.product_attribute.name} --> {self.value} >"


class ProductInventory(models.Model):

    sku = models.CharField(
        max_length=12,
        unique=True,
        null=False,
        blank=False,
        verbose_name="stock keeping unit",
    )
    product_type = models.ForeignKey(
        ProductType,
        related_name="product_type",
        on_delete=models.PROTECT,
    )
    product = models.ForeignKey(
        Product,
        related_name="product",
        on_delete=models.PROTECT,
    )
    brand = models.ForeignKey(
        Brand,
        related_name="brand",
        on_delete=models.PROTECT,
    )
    attribute_values = models.ManyToManyField(
        ProductAttributeValue,
        related_name="product_inventory_attribute_values",
        through="ProductInventoryAttributeValue",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="product visibility",
    )
    retail_price = models.CharField(
        max_length=10,
        unique=False,
        null=False,
        blank=False,
        verbose_name="recommended retail price",
    )
    stock_price = models.CharField(
        max_length=10,
        unique=False,
        null=False,
        blank=False,
        verbose_name="stock price",
    )
    sale_price = models.CharField(
        max_length=10,
        unique=False,
        null=False,
        blank=False,
        verbose_name="sale price",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name="date sub-product created",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="date sub-product updated",
    )

    class Meta:
        verbose_name = "Product Inventory"
        verbose_name_plural = "Product Inventories"

    def __str__(self):
        return self.product.name


class ProductInventoryAttributeValue(models.Model):

    """Product Inventory mapping with attribute value table"""

    product_inventory = models.ForeignKey(
        ProductInventory,
        related_name="product_attribute_values",
        on_delete=models.PROTECT,
    )

    product_attribute_value = models.ForeignKey(
        ProductAttributeValue,
        related_name="product_attribute_values",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"< {self.product_inventory.product.name} --> {self.product_attribute_value.value} >"

    class Meta:
        unique_together = (
            "product_inventory",
            "product_attribute_value",
        )


class Media(models.Model):

    """product image table"""

    product_inventory = models.ForeignKey(
        ProductInventory,
        related_name="media",
        on_delete=models.PROTECT,
    )

    image = models.ImageField(
        unique=False,
        null=False,
        blank=False,
        verbose_name="product image",
        upload_to="images/",
        default="images/default.png",
    )

    alt_text = models.CharField(
        max_length=128,
        unique=False,
        null=False,
        blank=False,
        verbose_name="image alternate text",
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"image of {self.product_inventory.product.name}"
