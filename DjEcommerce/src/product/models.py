from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
# from django.contrib.auth.models import User


class ProductImage(BaseModel):
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='ProductImages')


class Category(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    price = models.IntegerField()
    image = models.ForeignKey(
        ProductImage, on_delete=models.CASCADE, related_name='product')

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category')

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.title

    
