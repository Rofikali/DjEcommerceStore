from django.contrib import admin
from .models import Product, ProductImage, Category


class ChoiceInline(admin.TabularInline):
    model = Product
    extra = 0  # by default 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'price', 'image']
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = [
        (None,               {'fields': ['slug']}),
        ('Required information', {'fields': [
         'title', 'content', 'image', 'price']}),
    ]


@ admin.register(ProductImage)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['slug', 'image']
    fieldsets = [
        (None,               {'fields': ['slug']}),
        ('Required information', {'fields': ['image']}),
    ]
    inlines = [ChoiceInline, ]


@ admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    list_filter = ['slug']

    fieldsets = [
        (None,               {'fields': ['slug']}),
        ('Required information', {'fields': [
         'name']}),
    ]

    inlines = [ChoiceInline]
