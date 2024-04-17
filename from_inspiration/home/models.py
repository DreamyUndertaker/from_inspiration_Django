from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='media/products/img', blank=True)

