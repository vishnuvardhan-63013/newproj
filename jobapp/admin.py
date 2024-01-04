from django.contrib import admin
from jobapp.models import jobposts,submit,addpost,comment

# Register your models here.
admin.site.register(jobposts)
admin.site.register(submit)
admin.site.register(comment)
admin.site.register(addpost)



