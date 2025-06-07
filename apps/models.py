from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Users(AbstractUser):
    username = models.CharField(max_length=100, null=False, unique=True)
    email = models.EmailField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=100, null=False, unique=False)

class Product(models.Model):
    class ProductChoices(models.TextChoices):
        BOOK = 'BOOK', 'Book'
        HEALTH_WELLNESS ='HLT & WLN', 'Health & Wellness'
        FASHION = 'FASHION', 'FASHION'
        
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='productImage/')
    stock = models.PositiveIntegerField(default=1)
    category = models.CharField(max_length=100, choices=ProductChoices.choices)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name