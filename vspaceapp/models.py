from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def get_absolute_url(self):
            return reverse('details', kwargs = {"pk":self.pk})

# # additional fields

#     Phone = models.IntegerField()
    

class subscribe(models.Model):
    Email = models.EmailField()
    Time = models.DateTimeField(auto_now_add=True)