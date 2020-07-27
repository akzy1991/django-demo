from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    name = 'reviews'
    fields = ('title', 'content', 'date')
