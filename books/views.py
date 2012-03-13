from django.http import HttpResponse
from django.http import Http404

from django.template import Context, loader

from books.models import Book, Quote

import random

def getRandomQuote():
    quotes = Quote.objects.all()
    if quotes:
        return quotes[random.randrange(0, quotes.count())]

def index(request):
    books = Book.objects.all()[:3]
    template = loader.get_template('books/index.html')
    quote = getRandomQuote()
    context = Context({
        'object_list': books,
        'quote': quote,
    })
    return HttpResponse(template.render(context))

def addBookView(request):
    quote = getRandomQuote()
    context = Context({
        'quote': quote,
    })
    template = loader.get_template('books/add_book.html')
    return HttpResponse(template.render(context))

def addLocationView(request):
    quote = getRandomQuote()
    context = Context({
        'quote': quote,
    })
    template = loader.get_template('books/add_location.html')
    return HttpResponse(template.render(context))

def bookdetail(render, slug):
    try:
        book = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        raise Http404
    template = loader.get_template('books/detail.html')
    context = Context({'object': book})
    return HttpResponse(template.render(context))

def about(request):
    quote = getRandomQuote()
    context = Context({
        'quote': quote,
    })
    template = loader.get_template('books/about.html')
    return HttpResponse(template.render(context))

def legalNotice(request):
    quote = getRandomQuote()
    context = Context({
        'quote': quote,
    })
    template = loader.get_template('books/legal_notice.html')
    return HttpResponse(template.render(context))

def privacy(request):
    quote = getRandomQuote()
    context = Context({
        'quote': quote,
    })
    template = loader.get_template('books/privacy.html')
    return HttpResponse(template.render(context))
