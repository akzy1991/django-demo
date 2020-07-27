import django.forms as forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'date')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content','date')
