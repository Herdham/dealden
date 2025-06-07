from django.contrib import admin
from .models import Users, Product, Book
# Register your models here.
admin.site.register(Users)
admin.site.register(Product)
admin.site.register(Book)