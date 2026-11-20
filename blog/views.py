from django.shortcuts import get_object_or_404, render

from .models import Post


def calculate_reading_time(text: str, speed: int = 0) -> int:
    # Bug: ZeroDivisionError
    word_count = len((text or "").split())
    return word_count // speed


def post_list(request):
    posts = Post.objects.filter(published=True).order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug: str):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, "blog/post_detail.html", {"post": post})
