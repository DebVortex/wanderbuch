# encoding: utf-8
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader
from django.shortcuts import render
from django.contrib import messages

from books.models import Book, Quote, Location
from books.forms import BookForm, LocationForm

from settings import DOMAIN

import random


def getRandomQuote():
    quotes = Quote.objects.all()
    if quotes:
        return quotes[random.randrange(0, quotes.count())]

def index(request):
    prefix = None
    suffix = None
    if request.GET.has_key('book_preffix'):
        prefix = request.GET['book_preffix'].upper()
    if request.GET.has_key('book_suffix'):
        suffix = request.GET['book_suffix'].upper()
    if prefix and suffix:
        try:
            import pdb;pdb.set_trace()
            book = Book.objects.get(book_uuid = prefix + "-" + suffix)
            return HttpResponseRedirect(book.get_absolute_url())
        except Book.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'Fehler! Der Buche mit der ID ' +\
                prefix + "-" + suffix +' konnte nicht gefunden werden')
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
    if request.method == 'POST':
        form = LocationForm(data=request.POST)
        if form.is_valid():
            location = form.save()
            book = location.book_uuid
            return HttpResponseRedirect(book.get_absolute_url())
        else:
            messages.add_message(request, messages.ERROR, 'Fehler! Es muss eine gültige Buch-ID ' +\
                ' und wenigstens eine Stadt eingetragen werden.')
            return HttpResponseRedirect('/add/location/'+slug)
    try:
        book = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        raise Http404
    quote = getRandomQuote()
    form = LocationForm()
    return render(
        request,
        'books/add_location.html',
        {
            'form': form,
            'add': True,
            'quote': quote,
            'uuid': book.book_uuid,
        }
    )

def bookdetail(render, slug):
    try:
        book = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        raise Http404
    template = loader.get_template('books/detail.html')
    location_list = Location.objects.filter(book_uuid=book)
    context = Context({'object': book, 'location_list': location_list})
    return HttpResponse(template.render(context))

def bookPrint(render, slug):
    try:
        book = Book.objects.get(slug=slug)
    except Book.DoesNotExist:
        raise Http404
    template = loader.get_template('books/book_print.html')
    context = Context({'book': book, 'DOMAIN': DOMAIN})
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

def idea(request):
    quote = getRandomQuote()
    context = Context({
        'quote': quote,
    })
    template = loader.get_template('books/idea.html')
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
