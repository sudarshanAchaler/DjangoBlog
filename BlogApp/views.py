from django.shortcuts import render,redirect
from .models import Post, Comment, PostDraft
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods
# Create your views here.

def index(request):
    context={'page':'Home'}
    return render(request, 'BlogApp/index.html', context)



def posts(request):
    posts=Post.objects.all().order_by('-id')
    featuredPost=Post.objects.get(featured=True)

    paginator= Paginator(posts,2)
    pageNum=request.GET.get('pageNumber', 1)
    page= paginator.page(pageNum)
    pageHasPrevious= page.has_previous()
    pageHasNext= page.has_next()
    

    
    try:
        nextpageNum=page.next_page_number()
    except:
        nextpageNum=paginator.num_pages

    try:
        previouspageNum=page.previous_page_number()
    except:
        previouspageNum=1

    context={'page':'Posts', 'posts':posts, 'featuredPost': featuredPost , 'pageHasPrevious':pageHasPrevious, 'pageHasNext':pageHasNext, 'nextpageNum':nextpageNum, 'previouspageNum':previouspageNum, "pageN": page}
    return render(request, 'BlogApp/posts.html', context)




def about(request):
    context={'page':'About'}
    return render(request, 'BlogApp/about.html', context)

def writeforus(request):
    context={'page':'Write for Us'}
    return render(request, 'BlogApp/writeforus.html', context)

def Post1(request,pk):
    post=Post.objects.get(id=pk)
    comments=Comment.objects.filter(post=post).order_by('-created_on')
    commentCount=comments.count()
    likesCount= post.likes.count()
    liked=False

    
    if post.likes.filter(id=request.user.id).exists():
            liked=True
    

    
    context={'page':'Posts', 'post':post, 'comments': comments, 'commentCount': commentCount , 'likesCount':likesCount ,'liked': liked}

    return render(request, 'BlogApp/post.html', context)

def addComment(request):
    user=request.user
    data= json.loads(request.body)
    PostId= data['PostId']
    commentBody= data['commentBody']
    post=Post.objects.get(id=PostId)
    comments=Comment.objects.filter(post=post)
    commentCount=comments.count()
    c=Comment(post=post, user=user, body=commentBody)
    c.save()
    return JsonResponse({'commentCount': commentCount }, safe=False)


def like(request):
    
    data= json.loads(request.body)
    PostId= data['PostId']
    post=Post.objects.get(id=PostId)
    liked='false'
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
                 
    else:
        post.likes.add(request.user)
        liked='true'

    c=post.likes.count() 
    return JsonResponse({'likesCount':c , 'liked':liked})


def LoginPage(request):
    if request.user.is_authenticated:
        messages.error(request, 'User Already Logged In ') 
        return redirect('home')
    return render(request, 'BlogApp/login.html', {})

def RegisterPage(request):
    return render(request, 'BlogApp/register.html', {})


def loginUser(request):
    if request.method=="POST":
        username= request.POST.get('username', '')
        password= request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            messages.success(request, "Login Successful. Hello {}".format(request.user))
            return redirect('home')    
        else:
            # No backend authenticated the credentials
            messages.error(request, "Wrong username or password")
            return redirect('login-page')
    

def registerUser(request):
    if request.method=="POST":
        firstName= request.POST.get('firstName','')
        lastName= request.POST.get('lastName','')
        email= request.POST.get('email','')
        username= request.POST.get('username','')
        password= request.POST.get('password','')

        user=User.objects.create_user(username, email, password)
        user.first_name= firstName
        user.last_name=lastName
        user.save()
        login(request, user)
        messages.success(request, "Account Created Successfully")
        return redirect('home')

def logoutUser(request):
    logout(request)
    messages.success(request, "Logout Successful")
    return redirect('login-page')




def draftSubmission(request):

    if request.method=="POST":
        email=request.POST.get('email','')
        username=request.POST.get('username','')
        link=request.POST.get('link','')
        note=request.POST.get('note','')
        
        draft=PostDraft(email=email, username=username, note=note, draftLink=link)
        draft.save()

        messages.success(request, "Draft details submitted successfully")

    context={}
    return render(request, 'BlogApp/draftSubmissionForm.html', context)



def searchPost(request):
    if request.method!="POST":
        messages.error(request, "/searchResults/ not accessible directly.")
        return redirect('home') 

    
    posts=[]
    if request.method=="POST":
        keyword=request.POST.get('keyword', '')
        posts= Post.objects.filter(title__icontains='{}'.format(keyword))
        if not posts:
            posts= Post.objects.filter(content__icontains='{}'.format(keyword))
        if not posts:
            posts= Post.objects.filter(postCategory__icontains='{}'.format(keyword))
        
        
        
        


    
    context={'posts':posts, 'keyword':keyword}
    return render(request, 'BlogApp/search.html', context)