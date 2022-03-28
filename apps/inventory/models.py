from operator import mod
from tabnanny import verbose
from unicodedata import category

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
