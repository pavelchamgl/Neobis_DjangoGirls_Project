from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.filter(date_published__lte=timezone.now()).order_by('date_published')
    context = {'posts': posts}
    return render(request, 'news_feed/post_list.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'news_feed/post_detail.html', context)


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_published = timezone.now()
            post.save()
            messages.success(request, 'Статья успешно добавлена!')
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'news_feed/post_update.html', context)


def post_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            messages.success(request, 'Статья успешно изменена!')
            return redirect('post_detail', post_id=post_id)
    else:
        form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'news_feed/post_update.html', context)


def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    messages.success(request, 'Статья удалена!')
    return redirect('post_list')
