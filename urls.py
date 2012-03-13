from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from settings import SITE_ROOT
import os

urlpatterns = patterns('',
    url(r'^$', 'wanderbuch.books.views.index', name='index'),
    url(r'^book/(?P<slug>[-\w]+)/$', 'wanderbuch.books.views.bookdetail', name='book_detail'),

    url(r'^add/book/', 'wanderbuch.books.views.addBook'),
    url(r'^add/location/(?P<slug>[-\w]+)/$', 'wanderbuch.books.views.addLocation'),

    url(r'^about/', 'wanderbuch.books.views.about'),
    url(r'^legal_notice/', 'wanderbuch.books.views.legalNotice'),
    url(r'^privacy/', 'wanderbuch.books.views.privacy'),

    # static
    url(r'^static/(?P<path>.*)', 'django.views.static.serve', 
        {'document_root': 'static'}),
    
    # admin and admindoc
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)
