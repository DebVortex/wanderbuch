from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from settings import SITE_ROOT
import os

urlpatterns = patterns('',
    # dynamic sites
    url(r'^$',
        'wanderbuch.books.views.index',
        name='index'),
    url(r'^book/(?P<slug>[-\w]+)/$',
        'wanderbuch.books.views.bookdetail',
        name='book_detail'),
    url(r'^book/print/(?P<slug>[-\w]+)/$',
        'wanderbuch.books.views.bookPrint',
        name='book_print'),
    url(r'^booklist/',
        'wanderbuch.books.views.booklist',
        name='booklist'),

    url(r'^add/book/',
        'wanderbuch.books.views.addBook',
        name='book_add'),
    url(r'^add/location/(?P<slug>[-\w]+)/$',
        'wanderbuch.books.views.addLocation',
        name='location_add'),

    # static sites
    url(r'^about/',
        'wanderbuch.books.views.about',
        name='about'),
    url(r'^legal_notice/',
        'wanderbuch.books.views.legalNotice',
        name='legal_notice'),
    url(r'^privacy/',
        'wanderbuch.books.views.privacy',
        name='privacy'),
    url(r'^idea/',
        'wanderbuch.books.views.idea',
        name='idea'),
    url(r'^copyright/',
        'wanderbuch.books.views.copyright',
        name='copyright'),

    # static files
    url(r'^static/(?P<path>.*)',
        'django.views.static.serve',
        {'document_root': 'static'}),

    # admin and admindoc
    url(r'^admin/doc/',
        include('django.contrib.admindocs.urls')),
    url(r'^admin/',
        include(admin.site.urls)),
)
