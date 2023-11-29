from django.urls import path
# from django.jobposts.urls import
from vspaceapp import views
# from jobposts import views

urlpatterns = [
    path('',views.index1,name='register'),
    path('login/',views.index2,name='login'),
    path('home/',views.index3,name='home'),
    path('user_logout/',views.user_logout,name="user_logout"),  
    # path('jobposts',views.job,name='jobposts'),
    
]