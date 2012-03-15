from django.forms import ModelForm

from books.models import Book, Location


class BookForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Book
        exclude = ('slug', 'date_created', 'date_updated', 'book_uuid')


class LocationForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Location
        exclude = ('date_created', 'book_uuid')

    def save(self, commit=True):
    	book = Book.objects.get(book_uuid = self.data.get('book_uuid'))
        self.instance.book_uuid = book
        return super(LocationForm, self).save(commit)