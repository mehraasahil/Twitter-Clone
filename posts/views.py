#from urllib import request
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import Post
from django.http import HttpResponse
from .forms import PostForm
# Create your views here.
def index(request):
    #if the method is Post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
           form.save()
           return HttpResponseRedirect('/')
        else:
           return HttpResponseRedirect('form.erros.as_json()')
    posts = Post.objects.all().order_by('-created_at')[:20]
    form=PostForm
        #show
    return render(request, 'posts.html',{'posts':posts})
    



def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    posts = Post.objects.get(id=post_id)
    if request.method == "GET":
        posts = Post.objects.get(id=post_id)
        return render(request, "edit.html", {"posts": posts})
    if request.method == "POST":
        editposts = Post.objects.get(id=post_id)
        form = PostForm(request.POST, request.FILES, instance=editposts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("not valid")
# def like(request, post_id):
#     post=Post.objects.get(id=post_id)
#     new_like=post.likes + 1
#     post.likes=new_like
#     post.save()
#     return HttpResponseRedirect('/')
def like(request, post_id):
    newlikecount = Post.objects.get(id=post_id)
    newlikecount.likecount += 1
    newlikecount.save()
    return HttpResponseRedirect('/')











