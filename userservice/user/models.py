from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import now
# Create your models here.


class UserModel(models.Model):
    account = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    dob = models.DateField(max_length=255, default=now)
    email = models.CharField(max_length=255, default="")
    password = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=255, default="")
    type = models.CharField(max_length=255,default="user")