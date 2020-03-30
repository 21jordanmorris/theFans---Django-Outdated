from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request, pk=None):
    instance = get_object_or_404(Post, id=pk)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "Posts"
    }
    return render(request, "posts_index.html", context)

def post_update(request):
    return HttpResponse("<h1>Update</h1>")

def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")