from django.shortcuts import render, HttpResponse
from .models import Book

# Create your views here.


def index(request):
    fname = 'alvin'
    lname = 'koh'
    return render(request, 'books/index.template.html', {
        'first_name': fname,
        'last_name': lname
    })


def show_books(request):
    all_books = Book.objects.all()
    return render(request, 'books/all_books.template.html', {
        'books': all_books
    })
