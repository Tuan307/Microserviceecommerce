from django.db import models

# Create your models here.
class CartModel(models.Model):
    productId = models.IntegerField()
    userId = models.IntegerField()