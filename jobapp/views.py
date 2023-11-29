from django.shortcuts import render
from jobapp.models import jobposts
from django.views.generic import DetailView,ListView,TemplateView

# Create your views here.
# def job(request):
#     newjobs = job_posts.objects.all()
#     # print(newjobs)
#     return render(request, 'jobposts/index.html',{'newjobs':newjobs})


class indexView(TemplateView):
    template_name = "jobpost/index.html"


class JobList(ListView):
    context_object_name = 'mycompanies'
    model = jobposts

class Jobdetails(DetailView):
    context_object_name = 'details'
    model=jobposts