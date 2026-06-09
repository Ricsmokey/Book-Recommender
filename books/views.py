from django.shortcuts import render
from .models import Book


def random_book(request):
    book = Book.objects.order_by('?').first()
    stars = '★' * book.rating + '☆' * (5 - book.rating)
    return render(request, 'books/random_book.html', {'book': book, 'stars': stars})