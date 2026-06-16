from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('genres/', views.genre_list, name='genre_list'),
    path('genre/<str:category>/', views.genre_detail, name='genre_detail'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path("search/", views.search, name="search"),
]