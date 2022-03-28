# Generated by Django 4.0.3 on 2022-03-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Product category', 'verbose_name_plural': 'Product categories'},
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='product name')),
                ('slug', models.SlugField(max_length=128, verbose_name='product safe url')),
                ('web_id', models.CharField(max_length=128, unique=True, verbose_name='product website id')),
                ('description', models.TextField(verbose_name='product description')),
                ('is_active', models.BooleanField(default=True, verbose_name='product visibility')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='data product created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date product last update')),
                ('category', models.ManyToManyField(to='inventory.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]