from django.urls import path
from jobapp import views

urlpatterns =[
    path('',views.job,name='jobpost'),
    # path('',views.JobList.as_view(),name="jobpost"),
    path('<int:pk>/',views.Jobdetails.as_view(),name='details'),
    path('submit/',views.submits,name="submit"),
    path('appjobs/',views.appjobs,name="appjobs"),
    path('addposts/',views.addposts,name='addposts'),
    path('blog/',views.blog,name='blog'),
    path('jdetails/<int:pk>/',views.jdetails,name='jdetails'),
    path('search/',views.search,name='search'),
    path('likes/<int:pk>/',views.like_post,name='likes'),
    path('bookmarks/<int:pk>/',views.bookmark,name='bookmarks'),
    path('bpost/',views.bpost,name='bpost'),
    path('lpost/',views.lpost,name='lpost'),
    # path('tag/',views.tag,name='tag'),
]