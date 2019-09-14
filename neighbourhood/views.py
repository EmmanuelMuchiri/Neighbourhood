from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
# Create your views here.

def index(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user=request.user
        profile =Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')
    return render(request,'index.html')


@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)
    return render(request,'profile/user_profile.html',{"profile":profile})


@login_required(login_url='/accounts/login/')
def user_profile(request,username):
    user = User.objects.get(username=username)
    profile =Profile.objects.get(username=user)

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user=request.user
    if request.method=="POST":
        form =ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return HttpResponseRedirect('/')
    else:
        form = ProfileForm()
        return render(request,'profile/profile_form.html',{"form":form})
    

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user=request.user
    if request.method=="POST":
        instance = Profile.objects.get(username=current_user)
        form =ProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()

        return redirect('Index')

    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'profile/update_profile.html',{"form":form})


@login_required(login_url='/accounts/login/')
def blog(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    blogposts = BlogPost.objects.filter(neighbourhood=profile.neighbourhood)


@login_required(login_url='/accounts/login/')
def new_blogpost(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    if request.method=="POST":
        form =BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            blogpost = form.save(commit = False)
            blogpost.username = current_user
            blogpost.neighbourhood = profile.neighbourhood
            blogpost.avatar = profile.avatar
            blogpost.save()

        return HttpResponseRedirect('/blog')

    else:
        form = BlogPostForm()

    return render(request,'blogpost_form.html',{"form":form})



