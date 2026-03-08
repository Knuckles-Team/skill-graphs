This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/conditional-view-processing/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/conditional-view-processing/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/conditional-view-processing/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/conditional-view-processing/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/conditional-view-processing/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/conditional-view-processing/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/conditional-view-processing/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/conditional-view-processing/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/conditional-view-processing/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/conditional-view-processing/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/conditional-view-processing/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/conditional-view-processing/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/conditional-view-processing/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/conditional-view-processing/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/conditional-view-processing/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/conditional-view-processing/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/conditional-view-processing/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/conditional-view-processing/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/conditional-view-processing/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/conditional-view-processing/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/conditional-view-processing/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/conditional-view-processing/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/conditional-view-processing/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/conditional-view-processing/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/conditional-view-processing/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/conditional-view-processing/)


  * [](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/#top)


# Conditional View Processing[¶](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/#conditional-view-processing "Link to this heading")
HTTP clients can send a number of headers to tell the server about copies of a resource that they have already seen. This is commonly used when retrieving a web page (using an HTTP `GET` request) to avoid sending all the data for something the client has already retrieved. However, the same headers can be used for all HTTP methods (`POST`, `PUT`, `DELETE`, etc.).
For each page (response) that Django sends back from a view, it might provide two HTTP headers: the `ETag` header and the `Last-Modified` header. These headers are optional on HTTP responses. They can be set by your view function, or you can rely on the [`ConditionalGetMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.http.ConditionalGetMiddleware "django.middleware.http.ConditionalGetMiddleware") middleware to set the `ETag` header.
When the client next requests the same resource, it might send along a header such as either `ETag` it was sent. If the current version of the page matches the `ETag` sent by the client, or if the resource has not been modified, a 304 status code can be sent back, instead of a full response, telling the client that nothing has changed. Depending on the header, if the page has been modified or does not match the `ETag` sent by the client, a 412 status code (Precondition Failed) may be returned.
When you need more fine-grained control you may use per-view conditional processing functions.
## The `condition` decorator[¶](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/#the-condition-decorator "Link to this heading")
Sometimes (in fact, quite often) you can create functions to rapidly compute the **without** needing to do all the computations needed to construct the full view. Django can then use these functions to provide an “early bailout” option for the view processing. Telling the client that the content has not been modified since the last request, perhaps.
These two functions are passed as parameters to the `django.views.decorators.http.condition` decorator. This decorator uses the two functions (you only need to supply one, if you can’t compute both quantities easily and quickly) to work out if the headers in the HTTP request match those on the resource. If they don’t match, a new copy of the resource must be computed and your normal view is called.
The `condition` decorator’s signature looks like this:
```
condition(etag_func=None, last_modified_func=None)

```

The two functions, to compute the ETag and the last modified time, will be passed the incoming `request` object and the same parameters, in the same order, as the view function they are helping to wrap. The function passed `last_modified_func` should return a standard datetime value specifying the last time the resource was modified, or `None` if the resource doesn’t exist. The function passed to the `etag` decorator should return a string representing the `None` if it doesn’t exist.
The decorator sets the `ETag` and `Last-Modified` headers on the response if they are not already set by the view and if the request’s method is safe (`GET` or `HEAD`).
Using this feature usefully is probably best explained with an example. Suppose you have this pair of models, representing a small blog system:
```
import datetime
from django.db import models


class Blog(models.Model): ...


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    published = models.DateTimeField(default=datetime.datetime.now)
    ...

```

If the front page, displaying the latest blog entries, only changes when you add a new blog entry, you can compute the last modified time very quickly. You need the latest `published` date for every entry associated with that blog. One way to do this would be:
```
def latest_entry(request, blog_id):
    return Entry.objects.filter(blog=blog_id).latest("published").published

```

You can then use this function to provide early detection of an unchanged page for your front page view:
```
from django.views.decorators.http import condition


@condition(last_modified_func=latest_entry)
def front_page(request, blog_id): ...

```

Be careful with the order of decorators
When `condition()` returns a conditional response, any decorators below it will be skipped and won’t apply to the response. Therefore, any decorators that need to apply to both the regular view response and a conditional response must be above `condition()`. In particular, [`vary_on_cookie()`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.vary.vary_on_cookie "django.views.decorators.vary.vary_on_cookie"), [`vary_on_headers()`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.vary.vary_on_headers "django.views.decorators.vary.vary_on_headers"), and [`cache_control()`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.cache.cache_control "django.views.decorators.cache.cache_control") should come first because
## Shortcuts for only computing one value[¶](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/#shortcuts-for-only-computing-one-value "Link to this heading")
As a general rule, if you can provide functions to compute _both_ the ETag and the last modified time, you should do so. You don’t know which headers any given HTTP client will send you, so be prepared to handle both. However, sometimes only one value is easy to compute and Django provides decorators that handle only ETag or only last-modified computations.
The `django.views.decorators.http.etag` and `django.views.decorators.http.last_modified` decorators are passed the same type of functions as the `condition` decorator. Their signatures are:
```
etag(etag_func)
last_modified(last_modified_func)

```

We could write the earlier example, which only uses a last-modified function, using one of these decorators:
```
@last_modified(latest_entry)
def front_page(request, blog_id): ...

```

…or:
```
def front_page(request, blog_id): ...


front_page = last_modified(latest_entry)(front_page)

```

### Use `condition` when testing both conditions[¶](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/#use-condition-when-testing-both-conditions "Link to this heading")
It might look nicer to some people to try and chain the `etag` and `last_modified` decorators if you want to test both preconditions. However, this would lead to incorrect behavior.
```
# Bad code. Don't do this!
@etag(etag_func)
@last_modified(last_modified_func)
def my_view(request): ...


# End of bad code.

```

The first decorator doesn’t know anything about the second and might answer that the response is not modified even if the second decorators would determine otherwise. The `condition` decorator uses both callback functions simultaneously to work out the right action to take.
## Using the decorators with other HTTP methods[¶](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/#using-the-decorators-with-other-http-methods "Link to this heading")
The `condition` decorator is useful for more than only `GET` and `HEAD` requests (`HEAD` requests are the same as `GET` in this situation). It can also be used to provide checking for `POST`, `PUT` and `DELETE` requests. In these situations, the idea isn’t to return a “not modified” response, but to tell the client that the resource they are trying to change has been altered in the meantime.
For example, consider the following exchange between the client and server:
  1. Client requests `/foo/`.
  2. Server responds with some content with an ETag of `"abcd1234"`.
  3. Client sends an HTTP `PUT` request to `/foo/` to update the resource. It also sends an `If-Match: "abcd1234"` header to specify the version it is trying to update.
  4. Server checks to see if the resource has changed, by computing the ETag the same way it does for a `GET` request (using the same function). If the resource _has_ changed, it will return a 412 status code, meaning “precondition failed”.
  5. Client sends a `GET` request to `/foo/`, after receiving a 412 response, to retrieve an updated version of the content before updating it.


The important thing this example shows is that the same functions can be used to compute the ETag and last modification values in all situations. In fact, you **should** use the same functions, so that the same values are returned every time.
Validator headers with non-safe request methods
The `condition` decorator only sets validator headers (`ETag` and `Last-Modified`) for safe HTTP methods, i.e. `GET` and `HEAD`. If you wish to return them in other cases, set them in your view. See `PUT` versus `POST`.
## Comparison with middleware conditional processing[¶](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/#comparison-with-middleware-conditional-processing "Link to this heading")
Django provides conditional `GET` handling via [`django.middleware.http.ConditionalGetMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.http.ConditionalGetMiddleware "django.middleware.http.ConditionalGetMiddleware"). While being suitable for many situations, the middleware has limitations for advanced usage:
  * It’s applied globally to all views in your project.
  * It doesn’t save you from generating the response, which may be expensive.
  * It’s only appropriate for HTTP `GET` requests.


You should choose the most appropriate tool for your particular problem here. If you have a way to compute ETags and modification times quickly and if some view takes a while to generate the content, you should consider using the `condition` decorator described in this document. If everything already runs fairly quickly, stick to using the middleware and the amount of network traffic sent back to the clients will still be reduced if the view hasn’t changed.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/cache/)
[Cryptographic signing ](https://docs.djangoproject.com/en/5.0/topics/signing/)
[](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Keith B. French Law, PLLC donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Conditional View Processing](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/)
    * [The `condition` decorator](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/#the-condition-decorator)
    * [Shortcuts for only computing one value](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/#shortcuts-for-only-computing-one-value)
      * [Use `condition` when testing both conditions](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/#use-condition-when-testing-both-conditions)
    * [Using the decorators with other HTTP methods](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/#using-the-decorators-with-other-http-methods)
    * [Comparison with middleware conditional processing](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/#comparison-with-middleware-conditional-processing)


### Browse
  * Prev: [Django’s cache framework](https://docs.djangoproject.com/en/5.0/topics/cache/)
  * Next: [Cryptographic signing](https://docs.djangoproject.com/en/5.0/topics/signing/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * Conditional View Processing


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
