# encoding: utf-8
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.template import Context, loader
from django.shortcuts import render

from django.contrib import messages

from books.models import Book, Quote
from books.forms import BookForm

import random

def getRandomQuote():
    quotes = Quote.objects.all()
    if quotes:
        return quotes[random.randrange(0, quotes.count())]

def index(request):
    books = Book.objects.all()
    books.reverse()
    template = loader.get_template('books/index.html')
    quote = getRandomQuote()
    context = Context({
        'object_list': books[:3],
        'quote': quote,
    })
    return HttpResponse(template.render(context))

def addBook(request):
    if request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = form.save()
            #messages.add_message(request, messages.SUCCESS, 'Das Buch "' + book.title +\
            #    '" wurde erfolgreich angelegt.')
            return HttpResponseRedirect(book.get_absolute_url())
        else:
            messages.add_message(request, messages.ERROR, 'Fehler! Der Titel des Buches muss ausgefüllt sein.')
            return HttpResponseRedirect('book_add')
    else:
        form = BookForm()
        return render(request, 
            'books/add_book.html',
            {
                'form': form, 
                'add': True, 
                'quote': getRandomQuote()
            })

def addLocation(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        raise Http404
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

def booklist(render):
    books = Book.objects.all()
    quote = getRandomQuote()
    context = Context({
        'quote': quote,
        'books': books
    })
    template = loader.get_template('books/booklist.html')
    return HttpResponse(template.render(context))

# static sites

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
