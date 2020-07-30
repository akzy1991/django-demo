from django import forms
from .models import Book, Author, Genre
from cloudinary.forms import CloudinaryJsFileField


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'authors', 'desc', 'ISBN', 'pageCount', 'genre',
                  'category', 'tags', 'owner', 'cost')
    cover = CloudinaryJsFileField()


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'dob')


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(),
                                   required=False)
    min_page_count = forms.IntegerField(required=False)
