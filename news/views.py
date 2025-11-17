from django.shortcuts import render, get_object_or_404
from .models import News, Category

def home(request):
    query = request.GET.get("q")
    if query:
        posts = News.objects.filter(title__icontains=query)
        return render(request, "news/search_results.html", {"posts": posts, "query": query})

    posts = News.objects.all().order_by("-created_at")
    categories = Category.objects.all()
    return render(request, 'news/home.html', {'posts': posts, 'categories': categories})


def detail(request, id):
    post = get_object_or_404(News, id=id)
    return render(request, 'news/detail.html', {'post': post})


def category_view(request, id):
    category = get_object_or_404(Category, id=id)
    posts = News.objects.filter(category=category)
    return render(request, 'news/category.html', {'category': category, 'posts': posts})



