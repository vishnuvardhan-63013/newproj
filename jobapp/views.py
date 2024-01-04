from django.shortcuts import render,get_object_or_404
from jobapp.models import jobposts,submit,addpost,comment,User
from jobapp.forms import submitform,addform,commentform
from django.views.generic import DetailView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def job(request):
    newjobs = jobposts.objects.all()
    # print(newjobs)
    return render(request, 'jobpost/index.html',{'newjobs':newjobs})

class Jobdetails(DetailView):
    context_object_name = 'details'
    model=jobposts

def submits(request):
    register = False
    userform = submitform()
    if request.method == 'POST':
        userform = submitform(request.POST)
        if userform.is_valid():
            userform.save()
            register = True
            print("hello")
    return render(request,"jobpost/submit.html",{'userform':userform,'register':register})

def appjobs(request):
    vishnu = submit.objects.all()
    return render(request,"jobpost/appliedjobs.html",{'vishnu':vishnu})

def addposts(request):
    form2 = addform()
    if request.method=='POST':
        form2 =addform(request.POST,request.FILES)
        if form2.is_valid():
            form2.save()
            print("posted Successfully")
    return render(request,"jobpost/add_post.html",{'form2':form2})

def blog(request):
    vishnuu = addpost.objects.all()
    print(vishnuu)
    return render(request,"jobpost/blog.html",{'vishnuu':vishnuu})


def jdetails(request, pk):
    j = addpost.objects.get(pk=pk)
    sa = addpost.objects.all()
    cform = commentform()
    

    vish = addpost.objects.all().order_by("-view_count")[0:3]
    vi = addpost.objects.all().order_by("-view_count")[0:1]
    vis = addpost.objects.all().order_by("-time")[0:3]

    # ja = addpost.objects.filter(post_type = request.user)
    # for i in ja:
    #     return i.post_type

    # likes code 
    liked = False 
    if j.likes.filter(id=request.user.id).exists():
        liked = True 
    post_is_liked = liked
    number_of_likes = j.no_of_likes()

    #bookmarks code 
    book = False 
    if j.bookmarks.filter(id=request.user.id).exists():
        book = True 
    book_is_click = book


    print("hi")
    
    if request.method == 'POST':
        print("data coming")
        cform = commentform(request.POST) 
        if cform.is_valid():
            parent_obj = None
            if request.POST.get('parent'):
                # save reply
                parent=request.POST.get('parent')
                parent_obj = comment.objects.get(id=parent)
                if parent_obj:
                    comment_reply = cform.save(commit=False)
                    comment_reply.parent = parent_obj
                    comment_reply.post = j
                    comment_reply.save()
            else:
                print("valid success")
                print(request.POST.get('Name'))
                print(request.POST.get('Email'))
                comment1 = cform.save(commit=False)
                print(comment1)
                postid = request.POST.get('post_id')
                # print("id->",postid)
                post = addpost.objects.get(id=postid)
                # print('hii')
                comment1.post = post
                # print('hello')
                comment1.save()

    if j.view_count is None:
        j.view_count = 1
    else:
        j.view_count = j.view_count + 1
    j.save()
    k = comment.objects.filter(post=j)
    context = {'j':j, 'cform':cform,'k':k,'sa':sa,'post_is_liked':post_is_liked,'number_of_likes':number_of_likes,'book_is_click':book_is_click,'vish':vish,'vis':vis,'vi':vi}
    return render(request, 'details.html', context)

# def tag(request):
#     posts = addpost.objects.filter(post_type=request.user)
#     posts.save()
#     return redirect('jdetails')



def search(request):
    pandu = addpost.objects.all().order_by("-view_count")[0:3]
    ammu = addpost.objects.all().order_by("-time")[0:3]
    if request.method == 'POST':
        search_qry = request.POST['search_qry']
        posts = addpost.objects.filter(post_title__contains=search_qry)
        print(search_qry)
        return render(request, 'search.html', {'search_qry':search_qry, 'posts':posts,'pandu':pandu,'ammu':ammu})
    else:
        return render(request, 'search.html',{'pandu':pandu,'ammu':ammu})
    
def like_post(request,pk):  
    res = request.POST.get('post_id')
    print(res)
    posts=get_object_or_404(addpost,id=request.POST.get('post_id'))
    print("x->",posts)
    
    # posts = addpost.objects.get('post_id')
    if posts.likes.filter(id=request.user.id).exists():
        posts.likes.remove(request.user)
        print("removed")
    else:
        posts.likes.add(request.user)
        print("added")
    # return render(request,"details.html")
    # return redirect('jdetails',pk=pk)
    return HttpResponseRedirect(reverse('jdetails',args=[pk]))

def bookmark(request,pk):
    post = get_object_or_404(addpost, id=request.POST.get('post_id'))
    print("x->",post)

    if post.bookmarks.filter(id=request.user.id).exists():
        post.bookmarks.remove(request.user)
        print("removed")

    else:
        post.bookmarks.add(request.user)
        print("added")
    # return redirect('jdetails',pk=pk)
    return HttpResponseRedirect(reverse('jdetails',args=[pk]))
    


def bpost(request):
    q = addpost.objects.filter(bookmarks = request.user)
    print(q)
    return render(request,"jobpost/bookmarks.html",{'q':q})

def lpost(request):
    qa = addpost.objects.filter(likes = request.user)
    print(qa)
    return render(request,"jobpost/like.html",{'qa':qa})