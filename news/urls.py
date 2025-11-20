from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.detail, name='detail'),
    path('category/<int:id>/', views.category_view, name='category'),
    path('search/', views.search, name='search'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

]
