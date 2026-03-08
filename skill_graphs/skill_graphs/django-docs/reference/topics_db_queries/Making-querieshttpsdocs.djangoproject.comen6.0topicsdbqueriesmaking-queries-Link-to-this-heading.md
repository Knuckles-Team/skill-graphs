# Making queries[¶](https://docs.djangoproject.com/en/6.0/topics/db/queries/#making-queries "Link to this heading")
Once you’ve created your [data models](https://docs.djangoproject.com/en/6.0/topics/db/models/), Django automatically gives you a database-abstraction API that lets you create, retrieve, update and delete objects. This document explains how to use this API. Refer to the [data model reference](https://docs.djangoproject.com/en/6.0/ref/models/) for full details of all the various model lookup options.
Throughout this guide (and in the reference), we’ll refer to the following models, which comprise a blog application:
```
from datetime import date

from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline

```
