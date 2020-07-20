from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Book, Author
from .forms import BookForm, AuthorForm

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


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        form.save()
        return redirect(reverse(show_books))
    else:
        form = BookForm()
        return render(request, 'books/create_book.template.html', {
            'form': form
        })


def show_authors(request):
    all_authors = Author.objects.all()
    return render(request, 'books/all_authors.template.html', {
        'authors': all_authors
    })


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        form.save()
        return redirect(reverse(show_authors))
    else:
        form = AuthorForm()
        return render(request, 'books/create_author.template.html', {
            'form': form
        })


def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        form.save()
        return redirect(reverse(show_books))
    form = BookForm(instance=book)
    return render(request, 'books/edit_book.template.html', {
        'form': form
    })


def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        book.delete()
        return redirect(reverse(show_books))
    return render(request, 'books/delete_book.template.html', {
        'book': book
    })


def edit_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        form.save()
        return redirect(reverse(show_authors))
    form = AuthorForm(instance=author)
    return render(request, 'books/edit_author.template.html', {
        'form': form
    })
