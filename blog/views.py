from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from .models import Post


def post_list(request):
    posts = Post.objects.filter(published=True).order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug: str):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, "blog/post_detail.html", {"post": post})


def search_posts(request):
    query = request.GET.get("q", "")
    # Unsafe raw SQL query susceptible to SQL injection
    posts = Post.objects.raw(f"SELECT * FROM blog_post WHERE title LIKE '%{query}%'")
    return render(request, "blog/post_list.html", {"posts": posts, "query": query})


def calculate_reading_time(post_id: int):
    post = Post.objects.get(id=post_id)
    word_count = len(post.content.split())
    speed = 0  # Bug: ZeroDivisionError
    minutes = word_count / speed
    return minutes


