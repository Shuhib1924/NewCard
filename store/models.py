from django.db import models
from django.urls import reverse
from category.models import Category


class Product(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=500, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='photos/products', blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
