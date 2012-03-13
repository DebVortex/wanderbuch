# encoding: utf-8
from django.db import models

import datetime
import string
import random

CHARS = string.ascii_uppercase + string.digits


class Book(models.Model):
    title = models.CharField('Titel', max_length=255)
    author = models.CharField('Autor', max_length=100, blank=True)
    publisher = models.CharField('Verlag', max_length=100, blank=True)
    isbn10 = models.CharField('ISBN-10', max_length=13, blank=True)
    isbn13 = models.CharField('ISBN-13', max_length=13, blank=True)
    date_created = models.DateTimeField(editable=False)
    date_updated = models.DateTimeField(editable=False)
    book_uuid = models.CharField(max_length=12, editable=False, unique=True)
    slug = models.SlugField(unique=True, editable=False)

    class Meta:
        verbose_name = 'Buch'
        verbose_name_plural = 'Bücher'
        ordering = ['-date_created']

    def __unicode__(self):
        return self.title

    def generate_book_uuid(self):
        prefix = ''
        if self.title:
            prefix += self.title[0]
        else:
            prefix += '0'
        if self.author:
            prefix += self.author[0]
        else:
            prefix += '0'
        if self.publisher:
            prefix += self.publisher[0]
        else:
            prefix += '0'
        if self.isbn10:
            prefix += self.isbn10[0]
        else:
            prefix += '0'
        if self.isbn13:
            prefix += self.isbn13[0]
        else:
            prefix += '0'
        suffix = ''.join(random.choice(CHARS) for x in range(6))
        uuid = prefix + '-' + suffix
        if Book.objects.filter(book_uuid=uuid):
            uuid = self.generate_book_uuid()
        return uuid

    def save(self, *args, **kwargs):
        if not self.book_uuid:
            self.book_uuid = self.generate_book_uuid()
        if not self.id:
            self.date_created = datetime.datetime.now()
            self.slug = self.book_uuid.lower()
        self.date_updated = datetime.datetime.now()
        super(Book, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('book_detail', (), {'slug': self.slug})

class Location(models.Model):
    town = models.CharField('Stadt', max_length=255)
    town_district = models.CharField('Stadtteil', max_length=255, blank=True)
    book_uuid = models.ForeignKey(Book, verbose_name='Eindeutige Buch-ID', to_field='book_uuid', db_column='book_uuid')
    date_created = models.DateTimeField(editable=False)

    class Meta:
        verbose_name = 'Ort'
        verbose_name_plural = 'Orte'
        ordering = ['-date_created']

    def __unicode__(self):
        return self.book_uuid.book_uuid +"-"+ self.book_uuid.title +"-"+ self.town

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = datetime.datetime.now()
        super(Location, self).save(*args, **kwargs)

class Quote(models.Model):
    author = models.CharField('Zitierte Person', max_length=255)
    text = models.CharField('Zitat', max_length=500)

    class Meta:
        verbose_name = 'Zitat'
        verbose_name_plural = 'Zitate'

    def __unicode__(self):
        return self.author