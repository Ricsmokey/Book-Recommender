from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Book


def home(request):
    featured = Book.objects.order_by('?')[:4]
    top = (Book.objects.values('category')
           .annotate(count=Count('id'))
           .order_by('-count')[:3])          
    top_genres = []
    for g in top:                            
        sample = Book.objects.filter(category=g['category']).order_by('?').first()
        top_genres.append({'category': g['category'], 'book': sample})
    return render(request, 'books/home.html', {
        'featured': featured,
        'top_genres': top_genres,
    })


def genre_list(request):
    genres = (Book.objects.values_list('category', flat=True)
              .distinct().order_by('category'))     
    return render(request, 'books/genre_list.html', {'genres': genres})


def genre_detail(request, category):
    books = Book.objects.filter(category=category).order_by('title')
    return render(request, 'books/genre_detail.html', {
        'category': category,
        'books': books,
    })


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    stars = '★' * (book.rating or 0) + '☆' * (5 - (book.rating or 0))
    return render(request, 'books/book_detail.html', {'book': book, 'stars': stars})