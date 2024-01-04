from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from vspaceapp.models import User

# Create your models here.
class jobposts(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=150)
    company = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)
    salary = models.IntegerField()
    job_type = models.CharField(max_length=200)
    experience = models.IntegerField()
    roles_and_responsibillities = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('details', kwargs = {"pk":self.pk})
    
    
class submit(models.Model):
    jobtitle = models.ForeignKey(jobposts,related_name='jobposts',on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.IntegerField()

   


class addpost(models.Model):
    author_name = models.CharField(max_length=120)
    post_type = models.CharField(max_length=120)
    post_title =models.CharField(max_length=120)
    sub_title = models.CharField(max_length=120,blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='userimg',blank=True)
    time = models.DateTimeField(auto_now_add=True)
    view_count=models.IntegerField(blank=True,null=True)
    likes = models.ManyToManyField(User,related_name='postlike',default=None,blank=True)
    bookmarks = models.ManyToManyField(User,related_name='bookmarks',default=None,blank=True)


    def no_of_likes(self):
        return self.likes.count()


class comment(models.Model):
    Content = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=80)
    Email = models.EmailField()
    post = models.ForeignKey(addpost,related_name='add_posts', on_delete=models.CASCADE)
    # Author = models.ForeignKey(User,related_name='User', on_delete=models.CASCADE)
    Author = models.CharField(max_length=120)
    parent = models.ForeignKey('self',on_delete =models.CASCADE,blank = True,null=True,related_name='replies')


    def __str__(self):
        return self.Name

    # def get_absolute_url(self):
    #     return reverse('jdetails', kwargs = {"pk":self.pk})




