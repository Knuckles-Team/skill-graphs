This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/http/decorators/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/http/decorators/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/http/decorators/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/http/decorators/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/http/decorators/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/http/decorators/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/http/decorators/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/http/decorators/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/http/decorators/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/http/decorators/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/http/decorators/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/http/decorators/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/http/decorators/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/http/decorators/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/http/decorators/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/http/decorators/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/http/decorators/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/http/decorators/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/http/decorators/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/http/decorators/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/http/decorators/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/http/decorators/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/http/decorators/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/http/decorators/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/http/decorators/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/http/decorators/)


  * [](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#top)


# View decorators[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#module-django.views.decorators.http "Link to this heading")
Django provides several decorators that can be applied to views to support various HTTP features.
See [Decorating the class](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#id1) for how to use these decorators with class-based views.
## Allowed HTTP methods[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#allowed-http-methods "Link to this heading")
The decorators in [`django.views.decorators.http`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#module-django.views.decorators.http "django.views.decorators.http") can be used to restrict access to views based on the request method. These decorators will return a [`django.http.HttpResponseNotAllowed`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseNotAllowed "django.http.HttpResponseNotAllowed") if the conditions are not met.

require_http_methods(_request_method_list_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/views/decorators/http/#require_http_methods)[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.http.require_http_methods "Link to this definition")

Decorator to require that a view only accepts particular request methods. Usage:
```
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def my_view(request):
    # I can assume now that only GET or POST requests make it this far
    # ...
    pass

```

Note that request methods should be in uppercase.
Changed in Django 5.0:
Support for wrapping asynchronous view functions was added.

require_GET()[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.http.require_GET "Link to this definition")

Decorator to require that a view only accepts the GET method.
Changed in Django 5.0:
Support for wrapping asynchronous view functions was added.

require_POST()[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.http.require_POST "Link to this definition")

Decorator to require that a view only accepts the POST method.
Changed in Django 5.0:
Support for wrapping asynchronous view functions was added.

require_safe()[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.http.require_safe "Link to this definition")

Decorator to require that a view only accepts the GET and HEAD methods. These methods are commonly considered “safe” because they should not have the significance of taking an action other than retrieving the requested resource.
Note
Web servers should automatically strip the content of responses to HEAD requests while leaving the headers unchanged, so you may handle HEAD requests exactly like GET requests in your views. Since some software, such as link checkers, rely on HEAD requests, you might prefer using `require_safe` instead of `require_GET`.
Changed in Django 5.0:
Support for wrapping asynchronous view functions was added.
## Conditional view processing[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#conditional-view-processing "Link to this heading")
The following decorators in [`django.views.decorators.http`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#module-django.views.decorators.http "django.views.decorators.http") can be used to control caching behavior on particular views.

condition(_etag_func =None_, _last_modified_func =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/views/decorators/http/#condition)[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.http.condition "Link to this definition")


etag(_etag_func_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/views/decorators/http/#etag)[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.http.etag "Link to this definition")


last_modified(_last_modified_func_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/views/decorators/http/#last_modified)[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.http.last_modified "Link to this definition")

These decorators can be used to generate `ETag` and `Last-Modified` headers; see [conditional view processing](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/).
Changed in Django 5.0:
Support for wrapping asynchronous view functions was added.
## GZip compression[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#gzip-compression "Link to this heading")
The decorators in [`django.views.decorators.gzip`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#module-django.views.decorators.gzip "django.views.decorators.gzip") control content compression on a per-view basis.

gzip_page()[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.gzip.gzip_page "Link to this definition")

This decorator compresses content if the browser allows gzip compression. It sets the `Vary` header accordingly, so that caches will base their storage on the `Accept-Encoding` header.
Changed in Django 5.0:
Support for wrapping asynchronous view functions was added.
## Vary headers[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#vary-headers "Link to this heading")
The decorators in [`django.views.decorators.vary`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#module-django.views.decorators.vary "django.views.decorators.vary") can be used to control caching based on specific request headers.

vary_on_cookie(_func_)[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.vary.vary_on_cookie "Link to this definition")

Changed in Django 5.0:
Support for wrapping asynchronous view functions was added.

vary_on_headers(_* headers_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/views/decorators/vary/#vary_on_headers)[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.vary.vary_on_headers "Link to this definition")

The `Vary` header defines which request headers a cache mechanism should take into account when building its cache key.
See [using vary headers](https://docs.djangoproject.com/en/5.0/topics/cache/#using-vary-headers).
Changed in Django 5.0:
Support for wrapping asynchronous view functions was added.
## Caching[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#caching "Link to this heading")
The decorators in [`django.views.decorators.cache`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#module-django.views.decorators.cache "django.views.decorators.cache") control server and client-side caching.

cache_control(_** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/views/decorators/cache/#cache_control)[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.cache.cache_control "Link to this definition")

This decorator patches the response’s `Cache-Control` header by adding all of the keyword arguments to it. See [`patch_cache_control()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.cache.patch_cache_control "django.utils.cache.patch_cache_control") for the details of the transformation.
Changed in Django 5.0:
Support for wrapping asynchronous view functions was added.

never_cache(_view_func_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/views/decorators/cache/#never_cache)[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.cache.never_cache "Link to this definition")

This decorator adds an `Expires` header to the current date/time.
This decorator adds a `Cache-Control: max-age=0, no-cache, no-store, must-revalidate, private` header to a response to indicate that a page should never be cached.
Each header is only added if it isn’t already set.
Changed in Django 5.0:
Support for wrapping asynchronous view functions was added.
## Common[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#common "Link to this heading")
The decorators in [`django.views.decorators.common`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#module-django.views.decorators.common "django.views.decorators.common") allow per-view customization of [`CommonMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.common.CommonMiddleware "django.middleware.common.CommonMiddleware") behavior.

no_append_slash()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/views/decorators/common/#no_append_slash)[¶](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.common.no_append_slash "Link to this definition")

This decorator allows individual views to be excluded from [`APPEND_SLASH`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-APPEND_SLASH) URL normalization.
Changed in Django 5.0:
Support for wrapping asynchronous view functions was added. Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/http/views/)
[File Uploads ](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/)
[](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Fako Berkers donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [View decorators](https://docs.djangoproject.com/en/5.0/topics/http/decorators/)
    * [Allowed HTTP methods](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#allowed-http-methods)
    * [Conditional view processing](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#conditional-view-processing)
    * [GZip compression](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#gzip-compression)
    * [Vary headers](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#vary-headers)
    * [Caching](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#caching)
    * [Common](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#common)


### Browse
  * Prev: [Writing views](https://docs.djangoproject.com/en/5.0/topics/http/views/)
  * Next: [File Uploads](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * [Handling HTTP requests](https://docs.djangoproject.com/en/5.0/topics/http/)
        * View decorators


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
