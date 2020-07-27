from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=80)
    last_name = models.CharField(blank=False, max_length=80)
    dob = models.DateField(blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    pageCount = models.IntegerField(blank=False)

    # relationships
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    authors = models.ManyToManyField(Author)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
