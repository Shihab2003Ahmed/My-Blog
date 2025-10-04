from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "index.html", {"posts": posts})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request, "contact.html")

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})

from django.shortcuts import render, get_list_or_404
from .models import Post

def category_posts(request, category):
    # Get all posts for this category
    posts = Post.objects.filter(category=category).order_by('-date')
    
    # Optional: If you want 404 when no posts exist
    # posts = get_list_or_404(Post, category=category)

    context = {
        'posts': posts,
        'category': category.capitalize()
    }
    return render(request, 'category_posts.html', context)

