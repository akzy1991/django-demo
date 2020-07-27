from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book, Author
from .forms import BookForm, AuthorForm, SearchForm

# Create your views here.


def index(request):
    # subquery = Q(title_icontains='ring')  # WHERE 'title' LIKE 'ring'
    # genre_filter = Q(genre=1)

    # SELECT * from Books WHERE 'title' LIKE ring
    # books = books.filter(subquery & genre_filter)
    # books.filter(query)

    form = SearchForm(request.GET)
    if request.GET:
        query = ~Q(pk__in=[])
        if 'title' in request.GET and request.GET['title']:
            title = request.GET['title']
            query = query & Q(title__icontains=title)
        if 'genre' in request.GET and request.GET["genre"]:
            genre_id = request.GET['genre']
            query = query & Q(genre=genre_id)
        if 'min_page_count' in request.GET and request.GET['min_page_count']:
            min_page_count = request.GET['min_page_count']
            query = query & Q(pageCount__gte=min_page_count)

        # select * from Books
        books = Book.objects.all()
        # SELECT * FROM Books WHERE title LIKES "%{title}%""
        books = books.filter(query)

        return render(request, 'books/index.template.html', {
            'form': form,
            'books': books
        })
    else:
        books = Book.objects.all()
        return render(request, 'books/index.template.html', {
            'form': form,
            'books': books
        })


def show_books(request):
    all_books = Book.objects.all()
    return render(request, 'books/all_books.template.html', {
        'books': all_books
    })


def view_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/details.template.html', {
        'book': book
    })


@login_required
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        form.save()
        messages.success(request, 'new book has been created')
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


def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == "POST":
        author.delete()
        return redirect(reverse(show_authors))
    return render(request, 'books/delete_author.template.html', {
        'author': author
    })
