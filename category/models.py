from distutils.command.upload import upload
import black
from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=500, unique=True)
    image = models.ImageField(upload_to='photos/categories', blank=True)

    def __str__(self):
        return self.category_name

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
