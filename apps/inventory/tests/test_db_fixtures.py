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


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, sku, product_type, product, brand, is_active, retail_price, store_price, sale_price, created_at, updated_at",
    [
        (
            1,
            "1111",
            2,
            1,
            3,
            1,
            10.00,
            10.00,
            10.00,
            "2022-04-15 24:28:46",
            "2022-04-15 24:28:46",
        ),
        (
            2,
            "222",
            2,
            2,
            3,
            1,
            100.00,
            50.00,
            110.00,
            "2022-04-15 18:18:25",
            "2022-04-15 18:18:25",
        ),
    ],
)
def test_inventory_product_inventory_dbfixture(
    db,
    db_fixture_setup,
    id,
    sku,
    product_type,
    product,
    brand,
    is_active,
    retail_price,
    store_price,
    sale_price,
    created_at,
    updated_at,
):
    product_inventory = models.ProductInventory.objects.get(id=id)
    product_inventory_created_at = product_inventory.created_at.strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    product_inventory_updated_at = product_inventory.updated_at.strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    assert product_inventory.sku == sku
    assert product_inventory.product_type == product_type
    assert product_inventory.product == product
    assert product_inventory.brand == brand
    assert product_inventory.is_active == is_active
    assert product_inventory.retail_price == retail_price
    assert product_inventory.store_price == store_price
    assert product_inventory.sale_price == sale_price
    assert product_inventory_created_at == created_at
    assert product_inventory_updated_at == updated_at


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, product_inventory, image, alt_text, is_active, created_at, updated_at",
    [
        (
            1,
            "111",
            "images/default.png",
            "coming soon",
            1,
            "2022-03-29 19:00:10",
            "2022-03-29 19:00:10",
        ),
        (
            2,
            "222",
            "images/default.png",
            "coming soon",
            1,
            "2022-03-29 19:00:10",
            "2022-03-29 19:00:10",
        ),
    ],
)
def test_inventory_media_dbfixture(
    db,
    db_fixture_setup,
    id,
    product_inventory,
    image,
    alt_text,
    is_active,
    created_at,
    updated_at,
):
    media = models.Media.objects.get(id=id)
    media_created_at = media.created_at.strftime("%Y-%m-%d %H:%M:%S")
    media_updated_at = media.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    assert media.product_inventory == product_inventory
    assert media.image == image
    assert media.alt_text == alt_text
    assert media.is_active == is_active
    assert media_created_at == created_at
    assert media_updated_at == updated_at


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, product_inventory, last_checked, units, units_sold",
    [
        (1, 1, "2022-03-29 19:00:10", 100, 50),
        (2, 2, "2022-03-29 19:00:10", 50, 50),
    ],
)
def test_inventory_stock_dbfixture(
    db,
    db_fixture_setup,
    id,
    product_inventory,
    last_checked,
    units,
    units_sold,
):
    stock = models.Stock.objects.get(id=id)
    stock_last_checked = stock.last_checked.strftime("%Y-%m-%d %H:%M:%S")
    assert stock.product_inventory == product_inventory
    assert stock_last_checked == last_checked
    assert stock.units == units
    assert stock.units_sold == units_sold
