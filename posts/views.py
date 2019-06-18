from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from django.views.generic import ListView
from django.contrib import messages
from .forms import PostForm
# Create your views here.

class List(ListView):
    template_name = 'base.html'
    queryset =  Post.objects.all()



def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == "POST":
        instance = form.save(commit=False)
        instance.save()
        # messages.success(request,"created post" )
        return HttpResponseRedirect( instance.get_abs_url())
        # print(str(instance.get_abs_url()))
    context  = {
        "form":form,
    }
    return render(request, "post_form.html", context)

def post_list(request):

    # qset = Post.objects.filter(id=7)
    # x = get_object_or_404(Post, id=7)
    qset = Post.objects.all()
    context = {
        "object_list":qset,
        "title": "list",
    }
    return render(request, "base.html", context)

def post_detail(request,id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance = instance)
    # if request.method == "POST":
    #     return HttpResponseRedirect(instance.edit_post())
    context = {
        "instance":instance,
        "form":form
    }

    return render(request, "post_detail.html", context)

def post_update(request, id = None):

    instance  = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance )

    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect(instance.get_abs_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form":form,
    }
    return render(request, "post_form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    if instance is not None:
        instance.delete()
    else:
        pass

    return redirect("posts:list")