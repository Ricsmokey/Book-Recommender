import sqlite3
from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    help = "Import books from the scraper's Books.db into Django"

    def handle(self, *args, **options):
        source = sqlite3.connect("Books.db")          
        cursor = source.cursor()
        cursor.execute("""SELECT title, price, availability, rating,
                                 book_url, image_url, category, description
                          FROM books""")
        rows = cursor.fetchall()
        source.close()

        created = 0
        for row in rows:
            obj, was_created = Book.objects.get_or_create(
                book_url=row[4],     
                defaults={
                    'title': row[0],
                    'price': row[1],
                    'availability': row[2],
                    'rating': row[3],
                    'image_url': row[5],
                    'category': row[6],
                    'description': row[7],
                },
            )
            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(
            f"Imported {created} new books ({len(rows)} found in source)."))