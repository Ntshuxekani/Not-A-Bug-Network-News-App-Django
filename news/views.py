import requests
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import News, Category
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    posts = News.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    api_articles = []

    try:
        url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=f6ba60fd2f9c45808cc8b4fb7e27bd25"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            api_articles = data.get("articles", [])
        else:
            print("API error:", response.status_code)

    except Exception as e:
        print("API request failed:", e)

    return render(request, "news/home.html", {
        "posts": posts,
        "categories": categories,
        "api_articles": api_articles
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
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'news/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")

    else:
        form = AuthenticationForm()

    return render(request, 'news/login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out.")
    return redirect('login')

def search(request):
    query = request.GET.get('q')
    posts = News.objects.filter(title__icontains=query)
    categories = Category.objects.all()

    return render(request, 'news/home.html', {
        'posts': posts,
        'categories': categories,
        'query': query
    })
