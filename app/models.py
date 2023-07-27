from django.db import models
from django.contrib.auth.models import AbstractUser

CATEGORY_OPTIONS = (
    ('TS', 'Shirts'), # 'ML', 'Milk'
    ('JR', 'Jersey'), # 'JR', 'Lassi'
    ('CP', 'Cap'), # 'CP', 'Cap'
    ('HD', 'Hoodie'), # 'HD', 'Hoodie'
    ('JS','Jogger'),
    ('JK','Jacket'),
)



# USER
class User(AbstractUser):
    username = models.CharField(max_length=8, null=True)
    first_name = models.CharField(max_length=80, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=14, unique=True, null=True)
    address = models.CharField(max_length=150, unique=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name', 'phone','address']


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
    
    
# SHOPPING CART
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

  
    
# CHECKOUT
class Orders(models.Model):
    session_id = models.CharField(max_length=200)
    product_title = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    cart_total = models.FloatField()
    total_amount = models.FloatField()
    shipping_cost = models.FloatField()
    tax_rate = models.FloatField()
    
    def __str__(self):
        return self.session_id
    
    
# CONTACT FORM
class Contact(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=False, null=True)
    subject = models.CharField(max_length=80)
    message = models.TextField(default='')
    
    def __str__(self):
        return self.full_name
    


    
