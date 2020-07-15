from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    fname = 'alvin'
    lname = 'koh'
    return render(request, 'reviews/reviews.template.html', {
        'first_name': fname,
        'last_name': lname,
    })
