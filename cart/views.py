from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from books.models import Book

# Create your views here.


def add_to_cart(request, book_id):
    cart = request.session.get('shopping_cart', {})

    if book_id not in cart:
        book = get_object_or_404(Book, pk=book_id)
        cart[book_id] = {
            'id': book_id,
            'title': book.title,
            'cost': float(book.cost),
            'qty': 1
        }

        messages.success(request, f'added book {book.title} to cart')
    else:
        cart[book_id]['qty'] += 1

    request.session['shopping_cart'] = cart
    print(request.session['shopping_cart'])
    return render(request, 'cart/view_cart.template.html', {
        'cart': cart
    })


def view_cart(request):
    cart = request.session['shopping_cart']

    total = 0

    for k, v in cart.items():
        total = float(v['cost']) * int(v['qty'])

    return render(request, 'cart/view_cart.template.html', {
        'cart': cart,
        'total': total
    })


def remove_from_cart(request, book_id):
    cart = request.session['shopping_cart']
    if book_id in cart:
        del cart[book_id]
        request.session['shopping_cart'] = cart
        messages.success(request, 'item has been removed')

    return redirect(reverse(view_cart))


def update_quantity(request, book_id):
    cart = request.session['shopping_cart']
    if book_id in cart:
        cart[book_id]['qty'] = request.POST['qty']
        cart[book_id]['total_cost'] = int(request.POST['qty']) * float(cart[book_id]['cost'])
        request.session['shopping_cart'] = cart
        messages.success(request, 'quantity has been updated')
        return redirect(reverse(view_cart))
    else:
        messages.success(request, 'Book doesnt exist')
        return redirect(reverse(view_cart))
