# encoding: utf-8
from django.db import models

import datetime
import string
import random

CHARS = string.ascii_uppercase + string.digits


class Book(models.Model):
    title = models.CharField('Titel', max_length=255)
    slug = models.SlugField(unique=True)
    isbn = models.CharField('ISBN-Nummer', max_length=13, blank=True)
    author = models.CharField('Autor', max_length=100, blank=True)
    publisher = models.CharField('Verlag', max_length=100, blank=True)
    date_created = models.DateTimeField(editable=False)
    date_updated = models.DateTimeField(editable=False)
    book_uuid = models.CharField(max_length=11, editable=False)

    class Meta:
        verbose_name = 'Buch'
        verbose_name_plural = 'Bücher'

    def __unicode__(self):
        return self.name

    def generate_book_uuid(self):
        prefix = getattr(self, 'title', '0')[0] +\
            getattr(self, 'author', '0')[0] +\
            getattr(self, 'publisher', '0')[0] +\
            getattr(self, 'isbn', '0')[0]
        suffix = ''.join(random.choice(CHARS) for x in range(6))
        return prefix + '-' + suffix

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = datetime.datetime.now()
        if not self.book_uuid:
            self.book_uuid = self.generate_book_uuid()
        self.date_updated = datetime.datetime.now()
        super(Book, self).save(*args, **kwargs)
