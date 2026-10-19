from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)
    category_image = models.ImageField(upload_to='category_image')

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    city = models.CharField(max_length=32, null=True, blank=True)
    type = models.BooleanField(default=False)
    owner = models.CharField()
    product_image = models.ImageField(upload_to='product_image', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name