from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class ProductImages(BaseModel):
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        upload_to='ProductImgs/', height_field='height_field', width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)


class Category(BaseModel):
    slug = models.SlugField(unique=True)
    category_img = models.ImageField(
        upload_to='CategoryImages/', height_field='height_field',  width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")

    def __str__(self):
        return self.slug


class Product(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category')

    image = models.ForeignKey(
        ProductImages, on_delete=models.CASCADE, related_name='product_image')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("cores:detail", kwargs={"slug": self.slug})
