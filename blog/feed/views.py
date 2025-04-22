from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    blogs = BlogPost.objects.all().order_by('-created_at')
    return render(request, "index.html", {'blogs': blogs})


def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    is_liked = request.user in blog.likes.all()
    is_favorited = request.user in blog.favorites.all()
    return render(request, 'blog_detail.html', {
        'blog': blog,
        'is_liked': is_liked,
        'is_favorited': is_favorited
    })


@login_required
def toggle_like(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    if request.user in blog.likes.all():
        blog.likes.remove(request.user)
    else:
        blog.likes.add(request.user)
    return redirect('feed:blog_detail', slug=blog.slug)


@login_required
def toggle_favorite(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)
    if request.user in blog.favorites.all():
        blog.favorites.remove(request.user)
    else:
        blog.favorites.add(request.user)
    return redirect('feed:blog_detail', slug=blog.slug)