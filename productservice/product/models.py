from django.db import models

# Create your models here.
from django.db import models
# This is our model for user registration.


class product_details(models.Model):
    # The following are the fields of our table.
    product_id = models.CharField(max_length=10)
    product_category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=10)
    productType = models.CharField(max_length=50, null=True)
    size = models.CharField(max_length=50, null=True)