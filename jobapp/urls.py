from django.urls import path
from jobapp import views

urlpatterns =[
    # path('',views.job,name='jobpost'),
    path('',views.JobList.as_view(),name="jobpost"),
    path('<int:pk>/',views.Jobdetails.as_view(),name='details'),

]