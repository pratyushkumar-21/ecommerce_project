from operator import is_
from unicodedata import category
import pytest
from apps.inventory import models


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    'id, name, slug, is_active',
    [
        (1, 'fashion', 'fashion', 1),
        (2, 'woman', 'woman', 1),
        (3, 'baseball', 'baseball', 1),
    ]
)
def test_inventory_category_dbfixture(
    db, db_fixture_setup, id, name, slug, is_active
):
    category = models.Category.objects.get(id =id)
    assert category.name == name
    assert category.slug == slug
    assert category.is_active == is_active
    
@pytest.mark.parametrize(
    'name, slug, is_active',
    [
        ('fashion', 'fashion', 1),
        ('woman', 'woman', 1),
        ('baseball', 'baseball', 1),
    ]
)
def test_inventory_db_category_insert_data(
    db, category_factory, name, slug, is_active
):
    category = category_factory.create(name= name, slug= slug, is_active= is_active)
    assert category.name == name
    assert category.slug == slug
    assert category.is_active == is_active