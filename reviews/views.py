from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import ReviewForm, CommentForm
from .models import Review, Book

# Create your views here.


def index(request):
    fname = 'alvin'
    lname = 'koh'
    return render(request, 'reviews/reviews.template.html', {
        'first_name': fname,
        'last_name': lname,
    })


def show_reviews(request):
    all_reviews = Review.objects.all()
    return render(request, 'reviews/all_reviews.template.html', {
        'reviews': all_reviews
    })


def create_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return HttpResponse('review is created')
        else:
            return HttpResponse('something wrong')
    form = ReviewForm()
    return render(request, 'reviews/create_review.template.html', {
        'form': form,
        'book': book
    })


def view_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/details.template.html', {
        'review': review
    })


def create_comment(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            return HttpResponse('comment created')
        else:
            return HttpResponse('problem')
    else:
        form = CommentForm()
        return render(request, 'reviews/create_comment.template.html', {
            'form': form,
            'review': review
        })
