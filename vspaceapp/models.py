from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

# # additional fields

#     Phone = models.IntegerField()