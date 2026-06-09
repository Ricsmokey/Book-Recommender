from django.db import models



class Book(models.Model):
    title = models.CharField(max_length=300)
    price = models.CharField(max_length=20)
    availability = models.CharField(max_length=100)
    rating = models.IntegerField()
    book_url = models.URLField(max_length=500, unique=True)
    image_url = models.URLField(max_length=500)
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
