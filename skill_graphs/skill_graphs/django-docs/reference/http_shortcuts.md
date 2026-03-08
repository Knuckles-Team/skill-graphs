This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#main-content)
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
[Documentation](https://docs.djangoproject.com/en/5.0/)
  * [ Getting Help ](https://docs.djangoproject.com/en/5.0/faq/help/)


  * Language: **en**
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/http/shortcuts/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/http/shortcuts/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/http/shortcuts/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/http/shortcuts/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/http/shortcuts/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/http/shortcuts/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/http/shortcuts/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/http/shortcuts/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/http/shortcuts/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/http/shortcuts/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/http/shortcuts/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/http/shortcuts/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/http/shortcuts/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/http/shortcuts/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/http/shortcuts/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/http/shortcuts/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/http/shortcuts/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/http/shortcuts/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/http/shortcuts/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/http/shortcuts/)


  * [](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#top)


# Django shortcut functions[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#module-django.shortcuts "Link to this heading")
The package `django.shortcuts` collects helper functions and classes that “span” multiple levels of MVC. In other words, these functions/classes introduce controlled coupling for convenience’s sake.
##  `render()`[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render "Link to this heading")

render(_request_ , _template_name_ , _context =None_, _content_type =None_, _status =None_, _using =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/shortcuts/#render)[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#django.shortcuts.render "Link to this definition")

Combines a given template with a given context dictionary and returns an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") object with that rendered text.
Django does not provide a shortcut function which returns a [`TemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") because the constructor of [`TemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") offers the same level of convenience as [`render()`](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#django.shortcuts.render "django.shortcuts.render").
### Required arguments[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#required-arguments "Link to this heading")

`request`

The request object used to generate this response.

`template_name`

The full name of a template to use or sequence of template names. If a sequence is given, the first template that exists will be used. See the [template loading documentation](https://docs.djangoproject.com/en/5.0/topics/templates/#template-loading) for more information on how templates are found.
### Optional arguments[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#optional-arguments "Link to this heading")

`context`

A dictionary of values to add to the template context. By default, this is an empty dictionary. If a value in the dictionary is callable, the view will call it just before rendering the template.

`content_type`

The MIME type to use for the resulting document. Defaults to `'text/html'`.

`status`

The status code for the response. Defaults to `200`.

`using`

The [`NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-NAME) of a template engine to use for loading the template.
### Example[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#example "Link to this heading")
The following example renders the template `myapp/index.html` with the MIME type _application/xhtml+xml_ :
```
from django.shortcuts import render


def my_view(request):
    # View code here...
    return render(
        request,
        "myapp/index.html",
        {
            "foo": "bar",
        },
        content_type="application/xhtml+xml",
    )

```

This example is equivalent to:
```
from django.http import HttpResponse
from django.template import loader


def my_view(request):
    # View code here...
    t = loader.get_template("myapp/index.html")
    c = {"foo": "bar"}
    return HttpResponse(t.render(c, request), content_type="application/xhtml+xml")

```

##  `redirect()`[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#redirect "Link to this heading")

redirect(_to_ , _* args_, _permanent =False_, _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/shortcuts/#redirect)[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#django.shortcuts.redirect "Link to this definition")

Returns an [`HttpResponseRedirect`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseRedirect "django.http.HttpResponseRedirect") to the appropriate URL for the arguments passed.
The arguments could be:
  * A model: the model’s [`get_absolute_url()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.get_absolute_url "django.db.models.Model.get_absolute_url") function will be called.
  * A view name, possibly with arguments: [`reverse()`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.reverse "django.urls.reverse") will be used to reverse-resolve the name.
  * An absolute or relative URL, which will be used as-is for the redirect location.


By default issues a temporary redirect; pass `permanent=True` to issue a permanent redirect.
### Examples[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#examples "Link to this heading")
You can use the [`redirect()`](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#django.shortcuts.redirect "django.shortcuts.redirect") function in a number of ways.
  1. By passing some object; that object’s [`get_absolute_url()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.get_absolute_url "django.db.models.Model.get_absolute_url") method will be called to figure out the redirect URL:
```
from django.shortcuts import redirect


def my_view(request):
    ...
    obj = MyModel.objects.get(...)
    return redirect(obj)

```

  2. By passing the name of a view and optionally some positional or keyword arguments; the URL will be reverse resolved using the [`reverse()`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.reverse "django.urls.reverse") method:
```
def my_view(request):
    ...
    return redirect("some-view-name", foo="bar")

```

  3. By passing a hardcoded URL to redirect to:
```
def my_view(request):
    ...
    return redirect("/some/url/")

```

This also works with full URLs:
```
def my_view(request):
    ...
    return redirect("https://example.com/")

```



By default, [`redirect()`](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#django.shortcuts.redirect "django.shortcuts.redirect") returns a temporary redirect. All of the above forms accept a `permanent` argument; if set to `True` a permanent redirect will be returned:
```
def my_view(request):
    ...
    obj = MyModel.objects.get(...)
    return redirect(obj, permanent=True)

```

##  `get_object_or_404()`[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#get-object-or-404 "Link to this heading")

get_object_or_404(_klass_ , _* args_, _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/shortcuts/#get_object_or_404)[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#django.shortcuts.get_object_or_404 "Link to this definition")


aget_object_or_404(_klass_ , _* args_, _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/shortcuts/#aget_object_or_404)[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#django.shortcuts.aget_object_or_404 "Link to this definition")

_Asynchronous version_ : `aget_object_or_404()`
Calls [`get()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") on a given model manager, but it raises [`Http404`](https://docs.djangoproject.com/en/5.0/topics/http/views/#django.http.Http404 "django.http.Http404") instead of the model’s [`DoesNotExist`](https://docs.djangoproject.com/en/5.0/ref/models/class/#django.db.models.Model.DoesNotExist "django.db.models.Model.DoesNotExist") exception.
### Arguments[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#arguments "Link to this heading")

`klass`

A [`Model`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model "django.db.models.Model") class, a [`Manager`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager"), or a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") instance from which to get the object.

`*args`

[`Q objects`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.Q "django.db.models.Q").

`**kwargs`

Lookup parameters, which should be in the format accepted by `get()` and `filter()`.
### Example[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#id1 "Link to this heading")
The following example gets the object with the primary key of 1 from `MyModel`:
```
from django.shortcuts import get_object_or_404


def my_view(request):
    obj = get_object_or_404(MyModel, pk=1)

```

This example is equivalent to:
```
from django.http import Http404


def my_view(request):
    try:
        obj = MyModel.objects.get(pk=1)
    except MyModel.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

```

The most common use case is to pass a [`Model`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model "django.db.models.Model"), as shown above. However, you can also pass a [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") instance:
```
queryset = Book.objects.filter(title__startswith="M")
get_object_or_404(queryset, pk=1)

```

The above example is a bit contrived since it’s equivalent to doing:
```
get_object_or_404(Book, title__startswith="M", pk=1)

```

but it can be useful if you are passed the `queryset` variable from somewhere else.
Finally, you can also use a [`Manager`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager"). This is useful for example if you have a [custom manager](https://docs.djangoproject.com/en/5.0/topics/db/managers/#custom-managers):
```
get_object_or_404(Book.dahl_objects, title="Matilda")

```

You can also use [`related managers`](https://docs.djangoproject.com/en/5.0/ref/models/relations/#django.db.models.fields.related.RelatedManager "django.db.models.fields.related.RelatedManager"):
```
author = Author.objects.get(name="Roald Dahl")
get_object_or_404(author.book_set, title="Matilda")

```

Note: As with `get()`, a [`MultipleObjectsReturned`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.MultipleObjectsReturned "django.core.exceptions.MultipleObjectsReturned") exception will be raised if more than one object is found.
Changed in Django 5.0:
`aget_object_or_404()` function was added.
##  `get_list_or_404()`[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#get-list-or-404 "Link to this heading")

get_list_or_404(_klass_ , _* args_, _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/shortcuts/#get_list_or_404)[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#django.shortcuts.get_list_or_404 "Link to this definition")


aget_list_or_404(_klass_ , _* args_, _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/shortcuts/#aget_list_or_404)[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#django.shortcuts.aget_list_or_404 "Link to this definition")

_Asynchronous version_ : `aget_list_or_404()`
Returns the result of [`filter()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "django.db.models.query.QuerySet.filter") on a given model manager cast to a list, raising [`Http404`](https://docs.djangoproject.com/en/5.0/topics/http/views/#django.http.Http404 "django.http.Http404") if the resulting list is empty.
### Arguments[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#id2 "Link to this heading")

`klass`

A [`Model`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model "django.db.models.Model"), [`Manager`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") or [`QuerySet`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet "django.db.models.query.QuerySet") instance from which to get the list.

`*args`

[`Q objects`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.Q "django.db.models.Q").

`**kwargs`

Lookup parameters, which should be in the format accepted by `get()` and `filter()`.
### Example[¶](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#id3 "Link to this heading")
The following example gets all published objects from `MyModel`:
```
from django.shortcuts import get_list_or_404


def my_view(request):
    my_objects = get_list_or_404(MyModel, published=True)

```

This example is equivalent to:
```
from django.http import Http404


def my_view(request):
    my_objects = list(MyModel.objects.filter(published=True))
    if not my_objects:
        raise Http404("No MyModel matches the given query.")

```

Changed in Django 5.0:
`aget_list_or_404()` function was added.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/)
[Generic views ](https://docs.djangoproject.com/en/5.0/topics/http/generic-views/)
[](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Dan Lewis donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Django shortcut functions](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/)
    * [`render()`](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render)
      * [Required arguments](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#required-arguments)
      * [Optional arguments](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#optional-arguments)
      * [Example](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#example)
    * [`redirect()`](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#redirect)
      * [Examples](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#examples)
    * [`get_object_or_404()`](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#get-object-or-404)
      * [Arguments](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#arguments)
      * [Example](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#id1)
    * [`get_list_or_404()`](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#get-list-or-404)
      * [Arguments](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#id2)
      * [Example](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#id3)


### Browse
  * Prev: [File Uploads](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/)
  * Next: [Generic views](https://docs.djangoproject.com/en/5.0/topics/http/generic-views/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * [Handling HTTP requests](https://docs.djangoproject.com/en/5.0/topics/http/)
        * Django shortcut functions


### Getting help

[FAQ](https://docs.djangoproject.com/en/5.0/faq/)
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
Offline (Django 5.0): [HTML](https://media.djangoproject.com/docs/django-docs-5.0-en.zip) |
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
