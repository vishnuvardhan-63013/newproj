from django.shortcuts import render
from vspaceapp.forms import userform
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index1(request):
    registered = False
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            print('username',form.cleaned_data['username'])
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
    return render(request,"home.html",{})

def user_logout(request):
    logout(request)
    return redirect('login')