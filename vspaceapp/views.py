from django.shortcuts import render
from vspaceapp.forms import userform,subscribeform
from vspaceapp.models import User,subscribe
from jobapp.models import addpost
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="login")
def footer(request):
    vj = subscribe.objects.all()
    j = subscribeform()
    save = False
    if request.method == 'POST':
        j = subscribeform(request.POST)
        if j.is_valid():
            j.save()
            save = True
            print('subscribe success')
    return render(request,"base.html",{'j':j,'vj':vj,'save':save})


def index1(request):
    registered = False
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            print("Successs")
            registered = True

    else:
        form = userform()
    
    return render(request,"register.html",{'form':form ,'registered':registered})

def index2(request):
    if request.method == 'POST':
        print("hi")
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username,password=password)
        print(user)
        if user:
            print("hello")
            if user.is_active:
                print("hellooooo")
                login(request,user)
                return redirect ("home")
            else:
                return HttpResponse("user is not active")
        else:
            return HttpResponse("please check your cred.....!!")
    return render(request,"login.html",{})

@login_required(login_url="login")
def index3(request):
    vish = addpost.objects.all().order_by("-view_count")[0:3]
    vi = addpost.objects.all().order_by("-view_count")[0:1]
    vis = addpost.objects.all().order_by("-time")[0:3]

    
    v = subscribe.objects.all()
    i = subscribeform()
    saved = False
    if request.method == 'POST':
        i = subscribeform(request.POST)
        if i.is_valid():
            i.save()
            saved = True
            print('subscribe success')
    return render(request,"home.html",{'vish':vish,'v':v,'i':i,'saved':saved,'vi':vi,'vis':vis})

def user_logout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request,"jobpost/dashboard.html")

