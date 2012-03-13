from django.forms import ModelForm

from books.models import Book, Location

class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ('slug', 'date_created', 'date_updated', 'book_uuid')