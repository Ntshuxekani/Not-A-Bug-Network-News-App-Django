from django.shortcuts import render, get_object_or_404
from .models import News, Category

def home(request):
    posts = News.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'news/home.html', {
        'posts': posts,
        'categories': categories
    })

def detail(request, id):
    post = get_object_or_404(News, id=id)
    categories = Category.objects.all()
    return render(request, 'news/detail.html', {
        'post': post,
        'categories': categories
    })

def category_view(request, id):
    category = get_object_or_404(Category, id=id)
    posts = News.objects.filter(category=category)
    categories = Category.objects.all()

    return render(request, 'news/category.html', {
        'category': category,
        'posts': posts,
        'categories': categories
    })

def search(request):
    query = request.GET.get('q')
    posts = News.objects.filter(title__icontains=query)
    categories = Category.objects.all()

    return render(request, 'news/home.html', {
        'posts': posts,
        'categories': categories,
        'query': query
    })
