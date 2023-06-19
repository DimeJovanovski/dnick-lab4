from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import datetime

from .models import *
from .forms import *


def posts(request):
    blocked_users = Block.objects.filter(blocker__user=request.user)\
        .values_list("blocked__user", flat=True)
    visible_posts = Post.objects.get_queryset()\
        .exclude(user__user__in=blocked_users)
    context = {"posts": visible_posts}

    return render(request, "posts.html", context=context)


def addPost(request):
    if request.method=="POST":
        form_data = PostForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            post = form_data.save(commit=False)
            post.user = Blogger.objects.get(user=request.user)
            post.save()
            return redirect("/posts")

    context = {"form": PostForm}
    return render(request, "addPostForm.html", context=context)


def profile(request):
    loggedInUser = Blogger.objects.get(user=request.user)
    posts = Post.objects.filter(user=loggedInUser)

    context = {"user": loggedInUser, "posts": posts}
    return render(request, "profile.html", context=context)


def blockedUsers(request):
    if request.method == "POST":
        form_data = BlockForm(data=request.POST, files=request.FILES)

        if form_data.is_valid():
            block = form_data.save(commit=False)
            block.blocker = Blogger.objects.get(user=request.user)
            block.save()
            return redirect("/blockedUsers")

    blocks = Block.objects.filter(blocker__user=request.user)
    blocked_users = Blogger.objects\
        .filter(user__in=blocks.values_list("blocked__user", flat=True))
    context = {"form": BlockForm, "users": blocked_users}
    return render(request, "blockedUsers.html", context=context)

