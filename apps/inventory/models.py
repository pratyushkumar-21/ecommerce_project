from operator import mod
from tabnanny import verbose
from django.db import models


# Create your models here.
class Category(models.Model):
    '''
    Inventory Category table
    '''
    name = models.CharField(
        max_length= 128,
        blank= False,
        null= False,
        unique= False,
        verbose_name= "category name"
    )
    slug = models.SlugField(
        max_length= 128,
        null= False,
        unique= False,
        blank= False,
        verbose_name= 'category safe url'
    )
    is_active = models.BooleanField(
        default= True,
    )

    class Meta:
        verbose_name = "Product category"
        verbose_name_plural = "Product categories"

    def __str__(self):
        return self.name