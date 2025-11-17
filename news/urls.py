from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.detail, name='detail'),
    path('category/<int:id>/', views.category_view, name='category'),
]
