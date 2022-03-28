import factory
import pytest
from apps.inventory import models
from faker import Faker
from pytest_factoryboy import register

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):

    name = fake.lexify(text="cat_name_??????")
    slug = fake.lexify(text="cat_slug_??????")

    class Meta:
        model = models.Category


class ProductFactory(factory.django.DjangoModelFactory):

    web_id = factory.Sequence(lambda n: f"111{n}")
    name = fake.lexify(text="prod_name_??????")
    slug = fake.lexify(text="prod_slug_??????")
    description = fake.text()
    is_active = 1
    created_at = "2022-03-28T16:58:10.652Z"
    updated_at = "2022-03-28T16:58:10.652Z"

    class Meta:
        model = models.Product

    @factory.post_generation
    def category(self, create, extracted, **kwargs):

        if not create or not extracted:
            return

        if extracted:
            for cat in extracted:
                self.category.add(cat)


register(CategoryFactory)
register(ProductFactory)
