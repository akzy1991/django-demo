from django.urls import path
import books.views


urlpatterns = [
    path('', books.views.index,),
    path('all/', books.views.show_books, name='all_books_route'),
    path('create/', books.views.create_book),
    path('update/<book_id>/', books.views.edit_book,
         name='update_book_route'),
    path('delete/<book_id>/', books.views.delete_book,
         name='delete_book_route'),
    path('authors/all/', books.views.show_authors),
    path('author/create/', books.views.create_author),
    path('authors/update/<author_id>/', books.views.edit_author, name='update_author_route'),
    path('authors/delete/<author_id>/', books.views.delete_author, name='delete_author_route'),
    path('details/<book_id>', books.views.view_book, name='book_details_route')

]
