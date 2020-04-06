from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Post
from .forms import PostForm

def post_create(request):
    if not request.user.is_staff and not request.user.is_superuser: 
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    
    context = {
        "form": form,
        "button_name": "Create",
    }

    return render(request, "post_form.html", context)

def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    context = {
        "title": instance.title,
        "instance": instance,
    }

    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    paginator = Paginator(queryset, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "object_list": queryset,
        "title": "Posts",
        "page_obj": page_obj,
    }

    return render(request, "posts_index.html", context)

def post_update(request, slug=None):
    if not request.user.is_staff and not request.user.is_superuser: 
        raise Http404
    instance = get_object_or_404(Post, slug=slug)

    form = PostForm(request.POST or None, request.FILES or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        messages.success(request, instance.title + " Updated.")
        return HttpResponseRedirect(instance.get_absolute_url())
    
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
        "button_name": "Update",
    }

    return render(request, "post_form.html", context)

def post_delete(request, slug=None):
    if not request.user.is_staff and not request.user.is_superuser: 
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, instance.title + " deleted.")
    return redirect('post_list')