from django.urls import path
import reviews.views


urlpatterns = [
    path('', reviews.views.index),
    path('create/<book_id>', reviews.views.create_review,
         name='create_review_route'),
    path('all/', reviews.views.show_reviews,
         name='all_reviews_route'),
    path('details/<review_id>', reviews.views.view_review,
         name='review_details'),
    path('create/comment/<review_id>', reviews.views.create_comment,
         name='create_comment_route'),
]
