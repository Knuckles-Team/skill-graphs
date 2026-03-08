This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/class-based-views/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/class-based-views/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/class-based-views/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/class-based-views/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/class-based-views/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/class-based-views/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/class-based-views/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/class-based-views/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/class-based-views/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/class-based-views/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/class-based-views/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/class-based-views/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/class-based-views/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/class-based-views/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/class-based-views/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/class-based-views/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/class-based-views/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/class-based-views/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/class-based-views/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/class-based-views/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/class-based-views/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/class-based-views/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/class-based-views/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/class-based-views/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/class-based-views/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/class-based-views/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/class-based-views/)


  * [](https://docs.djangoproject.com/en/5.0/topics/class-based-views/#top)


# Class-based views[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/#class-based-views "Link to this heading")
A view is a callable which takes a request and returns a response. This can be more than just a function, and Django provides an example of some classes which can be used as views. These allow you to structure your views and reuse code by harnessing inheritance and mixins. There are also some generic views for tasks which we’ll get to later, but you may want to design your own structure of reusable views which suits your use case. For full details, see the [class-based views reference documentation](https://docs.djangoproject.com/en/5.0/ref/class-based-views/).
  * [Introduction to class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/)
  * [Built-in class-based generic views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/)
  * [Form handling with class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/)
  * [Using mixins with class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/mixins/)


## Basic examples[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/#basic-examples "Link to this heading")
Django provides base view classes which will suit a wide range of applications. All views inherit from the [`View`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View "django.views.generic.base.View") class, which handles linking the view into the URLs, HTTP method dispatching and other common features. [`RedirectView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.RedirectView "django.views.generic.base.RedirectView") provides a HTTP redirect, and [`TemplateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.TemplateView "django.views.generic.base.TemplateView") extends the base class to make it also render a template.
## Usage in your URLconf[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/#usage-in-your-urlconf "Link to this heading")
The most direct way to use generic views is to create them directly in your URLconf. If you’re only changing a few attributes on a class-based view, you can pass them into the [`as_view()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view") method call itself:
```
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("about/", TemplateView.as_view(template_name="about.html")),
]

```

Any arguments passed to [`as_view()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view") will override attributes set on the class. In this example, we set `template_name` on the `TemplateView`. A similar overriding pattern can be used for the `url` attribute on [`RedirectView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.RedirectView "django.views.generic.base.RedirectView").
## Subclassing generic views[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/#subclassing-generic-views "Link to this heading")
The second, more powerful way to use generic views is to inherit from an existing view and override attributes (such as the `template_name`) or methods (such as `get_context_data`) in your subclass to provide new values or methods. Consider, for example, a view that just displays one template, `about.html`. Django has a generic view to do this - [`TemplateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.TemplateView "django.views.generic.base.TemplateView") - so we can subclass it, and override the template name:
```
# some_app/views.py
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "about.html"

```

Then we need to add this new view into our URLconf. [`TemplateView`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.TemplateView "django.views.generic.base.TemplateView") is a class, not a function, so we point the URL to the [`as_view()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view") class method instead, which provides a function-like entry to class-based views:
```
# urls.py
from django.urls import path
from some_app.views import AboutView

urlpatterns = [
    path("about/", AboutView.as_view()),
]

```

For more information on how to use the built in generic views, consult the next topic on [generic class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/).
### Supporting other HTTP methods[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/#supporting-other-http-methods "Link to this heading")
Suppose somebody wants to access our book library over HTTP using the views as an API. The API client would connect every now and then and download book data for the books published since last visit. But if no new books appeared since then, it is a waste of CPU time and bandwidth to fetch the books from the database, render a full response and send it to the client. It might be preferable to ask the API when the most recent book was published.
We map the URL to book list view in the URLconf:
```
from django.urls import path
from books.views import BookListView

urlpatterns = [
    path("books/", BookListView.as_view()),
]

```

And the view:
```
from django.http import HttpResponse
from django.views.generic import ListView
from books.models import Book


class BookListView(ListView):
    model = Book

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest("publication_date")
        response = HttpResponse(
            # RFC 1123 date format.
            headers={
                "Last-Modified": last_book.publication_date.strftime(
                    "%a, %d %b %Y %H:%M:%S GMT"
                )
            },
        )
        return response

```

If the view is accessed from a `GET` request, an object list is returned in the response (using the `book_list.html` template). But if the client issues a `HEAD` request, the response has an empty body and the `Last-Modified` header indicates when the most recent book was published. Based on this information, the client may or may not download the full object list.
## Asynchronous class-based views[¶](https://docs.djangoproject.com/en/5.0/topics/class-based-views/#asynchronous-class-based-views "Link to this heading")
As well as the synchronous (`def`) method handlers already shown, `View` subclasses may define asynchronous (`async def`) method handlers to leverage asynchronous code using `await`:
```
import asyncio
from django.http import HttpResponse
from django.views import View


class AsyncView(View):
    async def get(self, request, *args, **kwargs):
        # Perform io-blocking view logic using await, sleep for example.
        await asyncio.sleep(1)
        return HttpResponse("Hello async world!")

```

Within a single view-class, all user-defined method handlers must be either synchronous, using `def`, or all asynchronous, using `async def`. An `ImproperlyConfigured` exception will be raised in `as_view()` if `def` and `async def` declarations are mixed.
Django will automatically detect asynchronous views and run them in an asynchronous context. You can read more about Django’s asynchronous support, and how to best use async views, in [Asynchronous support](https://docs.djangoproject.com/en/5.0/topics/async/).
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/templates/)
[Introduction to class-based views ](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/)
[](https://docs.djangoproject.com/en/5.0/topics/class-based-views/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Elif T. Kuş donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/)
    * [Basic examples](https://docs.djangoproject.com/en/5.0/topics/class-based-views/#basic-examples)
    * [Usage in your URLconf](https://docs.djangoproject.com/en/5.0/topics/class-based-views/#usage-in-your-urlconf)
    * [Subclassing generic views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/#subclassing-generic-views)
      * [Supporting other HTTP methods](https://docs.djangoproject.com/en/5.0/topics/class-based-views/#supporting-other-http-methods)
    * [Asynchronous class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/#asynchronous-class-based-views)


### Browse
  * Prev: [Templates](https://docs.djangoproject.com/en/5.0/topics/templates/)
  * Next: [Introduction to class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * Class-based views


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
