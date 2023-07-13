from django.contrib import admin
from . models import Product, Profile


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_title', 'selling_price',
                    'discounted_price', 'description', 'features', 'category', 'product_image']


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'mobile',
                    'city', 'address', 'zipcode', 'province']
