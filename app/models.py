from django.db import models
from django.contrib.auth.models import User

PROVINCE_OPTIONS = (
    ('Alberta', 'AL'),
    ('British Columbia', 'BC'),
    ('Manitoba', 'MB'),
    ('New Brunswick', 'NB'),
    ('Newfoundland and Labrador', 'NL'),
    ('Nova Scotia', 'NS'),
    ('Ontario', 'ON'),
    ('Prince Edward Island', 'PE'),
    ('Quebec', 'QC'),
    ('Saskatchewan', 'SK'),
    ('Northwest Territories', 'NT'),
    ('Nunavut', 'NU'),
    ('Yukon', 'YT'),
)

CATEGORY_OPTIONS = (
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'Milkshake'),
    ('PN', 'Paneer'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-Creams'),
)

# PROFILE


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    mobile = models.IntegerField(default=0)
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=150)
    province = models.CharField(choices=PROVINCE_OPTIONS, max_length=150)

    def __str__(self):
        return self.full_name


# PRODUCT
class Product(models.Model):
    product_title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    features = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.product_title
