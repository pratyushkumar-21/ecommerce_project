from itertools import product
from unicodedata import category

import pytest
from apps.inventory import models


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (2, "woman", "woman", 1),
        (3, "baseball", "baseball", 1),
    ],
)
def test_inventory_category_dbfixture(
    db, db_fixture_setup, id, name, slug, is_active
):
    category = models.Category.objects.get(id=id)
    assert category.name == name
    assert category.slug == slug
    assert category.is_active == is_active


@pytest.mark.parametrize(
    "name, slug, is_active",
    [
        ("fashion", "fashion", 1),
        ("woman", "woman", 1),
        ("baseball", "baseball", 1),
    ],
)
def test_inventory_db_category_insert_data(
    db, category_factory, name, slug, is_active
):
    category = category_factory.create(
        name=name, slug=slug, is_active=is_active
    )
    assert category.name == name
    assert category.slug == slug
    assert category.is_active == is_active


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, web_id, name, slug, description, is_active, created_at, updated_at",
    [
        (
            1,
            "1111",
            "shirt",
            "shirt",
            "test shirt",
            1,
            "2022-03-28 16:57:45",
            "2022-03-28 16:57:45",
        ),
        (
            2,
            "2222",
            "pant",
            "pant",
            "pant test",
            1,
            "2022-03-28 16:58:10",
            "2022-03-28 16:58:10",
        ),
    ],
)
def test_inventory_product_dbfixture(
    db,
    db_fixture_setup,
    id,
    web_id,
    name,
    slug,
    description,
    is_active,
    created_at,
    updated_at,
):
    product = models.Product.objects.get(id=id)
    product_created_at = product.created_at.strftime("%Y-%m-%d %H:%M:%S")
    product_updated_at = product.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    assert product.web_id == web_id
    assert product.name == name
    assert product.slug == slug
    assert product.description == description
    assert product.is_active == is_active
    assert product_created_at == created_at
    assert product_updated_at == updated_at


@pytest.mark.dbfixture
def test_inventory_db_product_insert_data(
    db,
    product_factory,
):
    product = product_factory.create(category=(1, 2))
    product_category_count = product.category.all().count()
    assert product_category_count == 2
