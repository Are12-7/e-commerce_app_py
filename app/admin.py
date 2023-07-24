from django.contrib import admin
from . models import Product, User, Cart, Orders, Contact


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_title', 'selling_price',
                    'discounted_price', 'description', 'features', 'category', 'product_image']


admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(Contact)
