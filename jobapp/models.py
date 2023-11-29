from django.db import models
from django.urls import reverse

# Create your models here.
class jobposts(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # location = models.CharField(max_length=150, null=True)
    company = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('details', kwargs = {"pk":self.pk})
