from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404


def index(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            form.save()
            return redirect('image_boards:index')
    posts = Post.objects.order_by('-date_added')
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': page_obj, 'form': form}
    return render(request, 'image_boards/index.html', context)


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    other_posts_by_user = Post.objects.filter(owner=post.owner).exclude(id=post_id)
    context = {'post': post, 'user': request.user, 'other_posts': other_posts_by_user}
    return render(request, 'image_boards/post.html', context)


def user_posts(request, user_id):
    user = User.objects.get(id=user_id)
    posts = Post.objects.order_by('-date_added')
    context = {'posts': posts, 'user': user, 'requesting_user': request.user}
    return render(request, 'image_boards/user_posts.html', context)


@login_required
def new_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            form.save()
            return redirect('image_boards:index')

    context = {'form': form}
    return render(request, 'image_boards/new_post.html', context)


@login_required
def my_posts(request):
    posts = Post.objects.filter(owner=request.user).order_by('date_added')
    context = {'posts': posts}
    return render(request, 'image_boards/my_posts.html', context)


@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404
    post.delete()
    return redirect('image_boards:index')