[Skip to main content](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#main-content)
[Django](https://www.djangoproject.com/)
The web framework for perfectionists with deadlines.
Menu Main navigation
  * [Overview](https://www.djangoproject.com/start/overview/)
  * [Download](https://www.djangoproject.com/download/)
  * [Documentation](https://docs.djangoproject.com/)
  * [News](https://www.djangoproject.com/weblog/)
  * [Issues](https://code.djangoproject.com/)
  * [Community](https://www.djangoproject.com/community/)
  * [Foundation](https://www.djangoproject.com/foundation/)
  * [♥ Donate](https://www.djangoproject.com/fundraising/)


Search Submit
Toggle theme (current theme: auto)
Toggle theme (current theme: light)
Toggle theme (current theme: dark)
Toggle Light / Dark / Auto color theme
[Documentation](https://docs.djangoproject.com/en/6.0/)
  * [ Getting Help ](https://docs.djangoproject.com/en/6.0/faq/help/)


  * Language: **en**
  * [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/topics/class-based-views/generic-display/)
  * [sv](https://docs.djangoproject.com/sv/6.0/topics/class-based-views/generic-display/)
  * [pt-br](https://docs.djangoproject.com/pt-br/6.0/topics/class-based-views/generic-display/)
  * [pl](https://docs.djangoproject.com/pl/6.0/topics/class-based-views/generic-display/)
  * [ko](https://docs.djangoproject.com/ko/6.0/topics/class-based-views/generic-display/)
  * [ja](https://docs.djangoproject.com/ja/6.0/topics/class-based-views/generic-display/)
  * [it](https://docs.djangoproject.com/it/6.0/topics/class-based-views/generic-display/)
  * [id](https://docs.djangoproject.com/id/6.0/topics/class-based-views/generic-display/)
  * [fr](https://docs.djangoproject.com/fr/6.0/topics/class-based-views/generic-display/)
  * [es](https://docs.djangoproject.com/es/6.0/topics/class-based-views/generic-display/)
  * [el](https://docs.djangoproject.com/el/6.0/topics/class-based-views/generic-display/)


  * Documentation version: **6.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-display/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/class-based-views/generic-display/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/class-based-views/generic-display/)
  * [5.0](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-display/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-display/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-display/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-display/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-display/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/class-based-views/generic-display/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-display/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/class-based-views/generic-display/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/class-based-views/generic-display/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/class-based-views/generic-display/)


  * [](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#top)


# Built-in class-based generic views[¶](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#built-in-class-based-generic-views "Link to this heading")
Writing web applications can be monotonous, because we repeat certain patterns again and again. Django tries to take away some of that monotony at the model and template layers, but web developers also experience this boredom at the view level.
Django’s _generic views_ were developed to ease that pain. They take certain common idioms and patterns found in view development and abstract them so that you can quickly write common views of data without having to write too much code.
We can recognize certain common tasks, like displaying a list of objects, and write code that displays a list of _any_ object. Then the model in question can be passed as an extra argument to the URLconf.
Django ships with generic views to do the following:
  * Display list and detail pages for a single object. If we were creating an application to manage conferences then a `TalkListView` and a `RegisteredUserListView` would be examples of list views. A single talk page is an example of what we call a “detail” view.
  * Present date-based objects in year/month/day archive pages, associated detail, and “latest” pages.
  * Allow users to create, update, and delete objects – with or without authorization.


Taken together, these views provide interfaces to perform the most common tasks developers encounter.
## Extending generic views[¶](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#extending-generic-views "Link to this heading")
There’s no question that using generic views can speed up development substantially. In most projects, however, there comes a moment when the generic views no longer suffice. Indeed, the most common question asked by new Django developers is how to make generic views handle a wider array of situations.
This is one of the reasons generic views were redesigned for the 1.3 release - previously, they were view functions with a bewildering array of options; now, rather than passing in a large amount of configuration in the URLconf, the recommended way to extend generic views is to subclass them, and override their attributes or methods.
That said, generic views will have a limit. If you find you’re struggling to implement your view as a subclass of a generic view, then you may find it more effective to write just the code you need, using your own class-based or functional views.
More examples of generic views are available in some third party applications, or you could write your own as needed.
## Generic views of objects[¶](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#generic-views-of-objects "Link to this heading")
[`TemplateView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.TemplateView "django.views.generic.base.TemplateView") certainly is useful, but Django’s generic views really shine when it comes to presenting views of your database content. Because it’s such a common task, Django comes with a handful of built-in generic views to help generate list and detail views of objects.
Let’s start by looking at some examples of showing a list of objects or an individual object.
We’ll be using these models:
```
# models.py
from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to="author_headshots")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField("Author")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

```

Now we need to define a view:
```
# views.py
from django.views.generic import ListView
from books.models import Publisher


class PublisherListView(ListView):
    model = Publisher

```

Finally hook that view into your urls:
```
# urls.py
from django.urls import path
from books.views import PublisherListView

urlpatterns = [
    path("publishers/", PublisherListView.as_view()),
]

```

That’s all the Python code we need to write. We still need to write a template, however. We could explicitly tell the view which template to use by adding a `template_name` attribute to the view, but in the absence of an explicit template Django will infer one from the object’s name. In this case, the inferred template will be `"books/publisher_list.html"` – the “books” part comes from the name of the app that defines the model, while the “publisher” bit is the lowercased version of the model’s name.
Note
Thus, when (for example) the `APP_DIRS` option of a `DjangoTemplates` backend is set to True in [`TEMPLATES`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-TEMPLATES), a template location could be: /path/to/project/books/templates/books/publisher_list.html
This template will be rendered against a context containing a variable called `object_list` that contains all the publisher objects. A template might look like this:
```
{% extends "base.html" %}

{% block content %}
    <h2>Publishers</h2>
    <ul>
        {% for publisher in object_list %}
            <li>{{ publisher.name }}</li>
        {% endfor %}
    </ul>
{% endblock %}

```

That’s really all there is to it. All the cool features of generic views come from changing the attributes set on the generic view. The [generic views reference](https://docs.djangoproject.com/en/6.0/ref/class-based-views/) documents all the generic views and their options in detail; the rest of this document will consider some of the common ways you might customize and extend generic views.
### Making “friendly” template contexts[¶](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#making-friendly-template-contexts "Link to this heading")
You might have noticed that our sample publisher list template stores all the publishers in a variable named `object_list`. While this works just fine, it isn’t all that “friendly” to template authors: they have to “just know” that they’re dealing with publishers here.
Well, if you’re dealing with a model object, this is already done for you. When you are dealing with an object or queryset, Django is able to populate the context using the lowercased version of the model class’ name. This is provided in addition to the default `object_list` entry, but contains exactly the same data, i.e. `publisher_list`.
If this still isn’t a good match, you can manually set the name of the context variable. The `context_object_name` attribute on a generic view specifies the context variable to use:
```
# views.py
from django.views.generic import ListView
from books.models import Publisher


class PublisherListView(ListView):
    model = Publisher
    context_object_name = "my_favorite_publishers"

```

Providing a useful `context_object_name` is always a good idea. Your coworkers who design templates will thank you.
### Adding extra context[¶](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#adding-extra-context "Link to this heading")
Often you need to present some extra information beyond that provided by the generic view. For example, think of showing a list of all the books on each publisher detail page. The [`DetailView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView "django.views.generic.detail.DetailView") generic view provides the publisher to the context, but how do we get additional information in that template?
The answer is to subclass [`DetailView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView "django.views.generic.detail.DetailView") and provide your own implementation of the `get_context_data` method. The default implementation adds the object being displayed to the template, but you can override it to send more:
```
from django.views.generic import DetailView
from books.models import Book, Publisher


class PublisherDetailView(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["book_list"] = Book.objects.all()
        return context

```

Note
Generally, `get_context_data` will merge the context data of all parent classes with those of the current class. To preserve this behavior in your own classes where you want to alter the context, you should be sure to call `get_context_data` on the super class. When no two classes try to define the same key, this will give the expected results. However if any class attempts to override a key after parent classes have set it (after the call to super), any children of that class will also need to explicitly set it after super if they want to be sure to override all parents. If you’re having trouble, review the method resolution order of your view.
Another consideration is that the context data from class-based generic views will override data provided by context processors; see [`get_context_data()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_data "django.views.generic.detail.SingleObjectMixin.get_context_data") for an example.
### Viewing subsets of objects[¶](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#viewing-subsets-of-objects "Link to this heading")
Now let’s take a closer look at the `model` argument we’ve been using all along. The `model` argument, which specifies the database model that the view will operate upon, is available on all the generic views that operate on a single object or a collection of objects. However, the `model` argument is not the only way to specify the objects that the view will operate upon – you can also specify the list of objects using the `queryset` argument:
```
from django.views.generic import DetailView
from books.models import Publisher


class PublisherDetailView(DetailView):
    context_object_name = "publisher"
    queryset = Publisher.objects.all()

```

Specifying `model = Publisher` is shorthand for saying `queryset = Publisher.objects.all()`. However, by using `queryset` to define a filtered list of objects you can be more specific about the objects that will be visible in the view (see [Making queries](https://docs.djangoproject.com/en/6.0/topics/db/queries/) for more information about [`QuerySet`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") objects, and see the [class-based views reference](https://docs.djangoproject.com/en/6.0/ref/class-based-views/) for the complete details).
To pick an example, we might want to order a list of books by publication date, with the most recent first:
```
from django.views.generic import ListView
from books.models import Book


class BookListView(ListView):
    queryset = Book.objects.order_by("-publication_date")
    context_object_name = "book_list"

```

That’s a pretty minimal example, but it illustrates the idea nicely. You’ll usually want to do more than just reorder objects. If you want to present a list of books by a particular publisher, you can use the same technique:
```
from django.views.generic import ListView
from books.models import Book


class AcmeBookListView(ListView):
    context_object_name = "book_list"
    queryset = Book.objects.filter(publisher__name="ACME Publishing")
    template_name = "books/acme_list.html"

```

Notice that along with a filtered `queryset`, we’re also using a custom template name. If we didn’t, the generic view would use the same template as the “vanilla” object list, which might not be what we want.
Also notice that this isn’t a very elegant way of doing publisher-specific books. If we want to add another publisher page, we’d need another handful of lines in the URLconf, and more than a few publishers would get unreasonable. We’ll deal with this problem in the next section.
Note
If you get a 404 when requesting `/books/acme/`, check to ensure you actually have a Publisher with the name ‘ACME Publishing’. Generic views have an `allow_empty` parameter for this case. See the [class-based-views reference](https://docs.djangoproject.com/en/6.0/ref/class-based-views/) for more details.
### Dynamic filtering[¶](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#dynamic-filtering "Link to this heading")
Another common need is to filter down the objects given in a list page by some key in the URL. Earlier we hardcoded the publisher’s name in the URLconf, but what if we wanted to write a view that displayed all the books by some arbitrary publisher?
Handily, the `ListView` has a [`get_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_queryset "django.views.generic.list.MultipleObjectMixin.get_queryset") method we can override. By default, it returns the value of the `queryset` attribute, but we can use it to add more logic.
The key part to making this work is that when class-based views are called, various useful things are stored on `self`; as well as the request (`self.request`) this includes the positional (`self.args`) and name-based (`self.kwargs`) arguments captured according to the URLconf.
Here, we have a URLconf with a single captured group:
```
# urls.py
from django.urls import path
from books.views import PublisherBookListView

urlpatterns = [
    path("books/<publisher>/", PublisherBookListView.as_view()),
]

```

Next, we’ll write the `PublisherBookListView` view itself:
```
# views.py
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from books.models import Book, Publisher


class PublisherBookListView(ListView):
    template_name = "books/books_by_publisher.html"

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs["publisher"])
        return Book.objects.filter(publisher=self.publisher)

```

Using `get_queryset` to add logic to the queryset selection is as convenient as it is powerful. For instance, if we wanted, we could use `self.request.user` to filter using the current user, or other more complex logic.
We can also add the publisher into the context at the same time, so we can use it in the template:
```
# ...


def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
    context = super().get_context_data(**kwargs)
    # Add in the publisher
    context["publisher"] = self.publisher
    return context

```

### Performing extra work[¶](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#performing-extra-work "Link to this heading")
The last common pattern we’ll look at involves doing some extra work before or after calling the generic view.
Imagine we had a `last_accessed` field on our `Author` model that we were using to keep track of the last time anybody looked at that author:
```
# models.py
from django.db import models


class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to="author_headshots")
    last_accessed = models.DateTimeField()

```

The generic `DetailView` class wouldn’t know anything about this field, but once again we could write a custom view to keep that field updated.
First, we’d need to add an author detail bit in the URLconf to point to a custom view:
```
from django.urls import path
from books.views import AuthorDetailView

urlpatterns = [
    # ...
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
]

```

Then we’d write our new view – `get_object` is the method that retrieves the object – so we override it and wrap the call:
```
from django.utils import timezone
from django.views.generic import DetailView
from books.models import Author


class AuthorDetailView(DetailView):
    queryset = Author.objects.all()

    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj

```

Note
The URLconf here uses the named group `pk` - this name is the default name that `DetailView` uses to find the value of the primary key used to filter the queryset.
If you want to call the group something else, you can set [`pk_url_kwarg`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.pk_url_kwarg "django.views.generic.detail.SingleObjectMixin.pk_url_kwarg") on the view.
Previous page and next page
[](https://docs.djangoproject.com/en/6.0/topics/class-based-views/intro/)
[Form handling with class-based views ](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-editing/)
[](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Scaffolding in Kent donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Built-in class-based generic views](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/)
    * [Extending generic views](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#extending-generic-views)
    * [Generic views of objects](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#generic-views-of-objects)
      * [Making “friendly” template contexts](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#making-friendly-template-contexts)
      * [Adding extra context](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#adding-extra-context)
      * [Viewing subsets of objects](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#viewing-subsets-of-objects)
      * [Dynamic filtering](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#dynamic-filtering)
      * [Performing extra work](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-display/#performing-extra-work)


### Browse
  * Prev: [Introduction to class-based views](https://docs.djangoproject.com/en/6.0/topics/class-based-views/intro/)
  * Next: [Form handling with class-based views](https://docs.djangoproject.com/en/6.0/topics/class-based-views/generic-editing/)
  * [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)


### You are here:
  * [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    * [Using Django](https://docs.djangoproject.com/en/6.0/topics/)
      * [Class-based views](https://docs.djangoproject.com/en/6.0/topics/class-based-views/)
        * Built-in class-based generic views


### Getting help

[FAQ](https://docs.djangoproject.com/en/6.0/faq/)
    Try the FAQ — it's got answers to many common questions.

[Index](https://docs.djangoproject.com/en/stable/genindex/), [Module Index](https://docs.djangoproject.com/en/stable/py-modindex/), or [Table of Contents](https://docs.djangoproject.com/en/stable/contents/)
    Handy when looking for specific information.

[Django Discord Server](https://chat.djangoproject.com)
    Join the Django Discord Community.

[Official Django Forum](https://forum.djangoproject.com/)
    Join the community on the Django Forum.

[Ticket tracker](https://code.djangoproject.com/)
    Report bugs with Django or Django documentation in our ticket tracker.
### Download:
Offline (Django 6.0): [HTML](https://media.djangoproject.com/docs/django-docs-6.0-en.zip) |
Provided by
### Diamond and Platinum Members
  * **JetBrains**


  * **Sentry**


  * **Kraken Tech**


## Django Links
### Learn More
  * [About Django](https://www.djangoproject.com/start/overview/)
  * [Getting Started with Django](https://www.djangoproject.com/start/)
  * [Team Organization](https://www.djangoproject.com/foundation/teams/)
  * [Django Software Foundation](https://www.djangoproject.com/foundation/)
  * [Code of Conduct](https://www.djangoproject.com/conduct/)
  * [Diversity Statement](https://www.djangoproject.com/diversity/)


### Get Involved
  * [Join a Group](https://www.djangoproject.com/community/)
  * [Contribute to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
  * [Submit a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
  * [Report a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
  * [Individual membership](https://www.djangoproject.com/foundation/individual-members/)


### Get Help
  * [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
  * [Django Discord](https://chat.djangoproject.com)
  * [Official Django Forum](https://forum.djangoproject.com/)


### Follow Us
  * [News RSS](https://www.djangoproject.com/rss/weblog/)


### Support Us
  * [Sponsor Django](https://www.djangoproject.com/fundraising/)
  * [Corporate membership](https://www.djangoproject.com/foundation/corporate-members/)
  * [Benevity Workplace Giving Program](https://www.djangoproject.com/fundraising/#benevity-giving)


[Django](https://www.djangoproject.com/)
  * Hosting by [In-kind donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
  * Design by &


© 2005-2026 [ Django Software Foundation](https://www.djangoproject.com/foundation/) and individual contributors. Django is a [registered trademark](https://www.djangoproject.com/trademarks/) of the Django Software Foundation.
