This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/views/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/views/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/views/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/views/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/views/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/views/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/views/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/views/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/views/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/views/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/views/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/views/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/views/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/views/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/views/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/views/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/views/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/views/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/views/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/views/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/views/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/views/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/views/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/views/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/views/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/views/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/views/)


  * [](https://docs.djangoproject.com/en/5.0/ref/views/#top)


# Built-in Views[¶](https://docs.djangoproject.com/en/5.0/ref/views/#module-django.views "Link to this heading")
Several of Django’s built-in views are documented in [Writing views](https://docs.djangoproject.com/en/5.0/topics/http/views/) as well as elsewhere in the documentation.
## Serving files in development[¶](https://docs.djangoproject.com/en/5.0/ref/views/#serving-files-in-development "Link to this heading")

static.serve(_request_ , _path_ , _document_root_ , _show_indexes =False_)[¶](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.static.serve "Link to this definition")

There may be files other than your project’s static assets that, for convenience, you’d like to have Django serve for you in local development. The [`serve()`](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.static.serve "django.views.static.serve") view can be used to serve any directory you give it. (This view is **not** hardened for production use and should be used only as a development aid; you should serve these files in production using a real front-end web server).
The most likely example is user-uploaded content in [`MEDIA_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_ROOT). `django.contrib.staticfiles` is intended for static assets and has no built-in handling for user-uploaded files, but you can have Django serve your [`MEDIA_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_ROOT) by appending something like this to your URLconf:
```
from django.conf import settings
from django.urls import re_path
from django.views.static import serve

# ... the rest of your URLconf goes here ...

if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {
                "document_root": settings.MEDIA_ROOT,
            },
        ),
    ]

```

Note, the snippet assumes your [`MEDIA_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_URL) has a value of `'media/'`. This will call the [`serve()`](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.static.serve "django.views.static.serve") view, passing in the path from the URLconf and the (required) `document_root` parameter.
Since it can become a bit cumbersome to define this URL pattern, Django ships with a small URL helper function [`static()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.conf.urls.static.static "django.conf.urls.static.static") that takes as parameters the prefix such as [`MEDIA_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_URL) and a dotted path to a view, such as `'django.views.static.serve'`. Any other function parameter will be transparently passed to the view.
## Error views[¶](https://docs.djangoproject.com/en/5.0/ref/views/#error-views "Link to this heading")
Django comes with a few views by default for handling HTTP errors. To override these with your own custom views, see [Customizing error views](https://docs.djangoproject.com/en/5.0/topics/http/views/#customizing-error-views).
### The 404 (page not found) view[¶](https://docs.djangoproject.com/en/5.0/ref/views/#the-404-page-not-found-view "Link to this heading")

defaults.page_not_found(_request_ , _exception_ , _template_name ='404.html'_)[¶](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.defaults.page_not_found "Link to this definition")

When you raise [`Http404`](https://docs.djangoproject.com/en/5.0/topics/http/views/#django.http.Http404 "django.http.Http404") from within a view, Django loads a special view devoted to handling 404 errors. By default, it’s the view [`django.views.defaults.page_not_found()`](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.defaults.page_not_found "django.views.defaults.page_not_found"), which either produces a “Not Found” message or loads and renders the template `404.html` if you created it in your root template directory.
The default 404 view will pass two variables to the template: `request_path`, which is the URL that resulted in the error, and `exception`, which is a useful representation of the exception that triggered the view (e.g. containing any message passed to a specific `Http404` instance).
Three things to note about 404 views:
  * The 404 view is also called if Django doesn’t find a match after checking every regular expression in the URLconf.
  * The 404 view is passed a [`RequestContext`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.RequestContext "django.template.RequestContext") and will have access to variables supplied by your template context processors (e.g. `MEDIA_URL`).
  * If [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is set to `True` (in your settings module), then your 404 view will never be used, and your URLconf will be displayed instead, with some debug information.


### The 500 (server error) view[¶](https://docs.djangoproject.com/en/5.0/ref/views/#the-500-server-error-view "Link to this heading")

defaults.server_error(_request_ , _template_name ='500.html'_)[¶](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.defaults.server_error "Link to this definition")

Similarly, Django executes special-case behavior in the case of runtime errors in view code. If a view results in an exception, Django will, by default, call the view `django.views.defaults.server_error`, which either produces a “Server Error” message or loads and renders the template `500.html` if you created it in your root template directory.
The default 500 view passes no variables to the `500.html` template and is rendered with an empty `Context` to lessen the chance of additional errors.
If [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is set to `True` (in your settings module), then your 500 view will never be used, and the traceback will be displayed instead, with some debug information.
### The 403 (HTTP Forbidden) view[¶](https://docs.djangoproject.com/en/5.0/ref/views/#the-403-http-forbidden-view "Link to this heading")

defaults.permission_denied(_request_ , _exception_ , _template_name ='403.html'_)[¶](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.defaults.permission_denied "Link to this definition")

In the same vein as the 404 and 500 views, Django has a view to handle 403 Forbidden errors. If a view results in a 403 exception then Django will, by default, call the view `django.views.defaults.permission_denied`.
This view loads and renders the template `403.html` in your root template directory, or if this file does not exist, instead serves the text “403 Forbidden”, as per `exception`, which is the string representation of the exception that triggered the view.
`django.views.defaults.permission_denied` is triggered by a [`PermissionDenied`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.PermissionDenied "django.core.exceptions.PermissionDenied") exception. To deny access in a view you can use code like this:
```
from django.core.exceptions import PermissionDenied


def edit(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied
    # ...

```

### The 400 (bad request) view[¶](https://docs.djangoproject.com/en/5.0/ref/views/#the-400-bad-request-view "Link to this heading")

defaults.bad_request(_request_ , _exception_ , _template_name ='400.html'_)[¶](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.defaults.bad_request "Link to this definition")

When a [`SuspiciousOperation`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation") is raised in Django, it may be handled by a component of Django (for example resetting the session data). If not specifically handled, Django will consider the current request a ‘bad request’ instead of a server error.
`django.views.defaults.bad_request`, is otherwise very similar to the `server_error` view, but returns with the status code 400 indicating that the error condition was the result of a client operation. By default, nothing related to the exception that triggered the view is passed to the template context, as the exception message might contain sensitive information like filesystem paths.
`bad_request` views are also only used when [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is `False`.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/validators/)
[Meta-documentation and miscellany ](https://docs.djangoproject.com/en/5.0/misc/)
[](https://docs.djangoproject.com/en/5.0/ref/views/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Thomas Kwon donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Built-in Views](https://docs.djangoproject.com/en/5.0/ref/views/)
    * [Serving files in development](https://docs.djangoproject.com/en/5.0/ref/views/#serving-files-in-development)
    * [Error views](https://docs.djangoproject.com/en/5.0/ref/views/#error-views)
      * [The 404 (page not found) view](https://docs.djangoproject.com/en/5.0/ref/views/#the-404-page-not-found-view)
      * [The 500 (server error) view](https://docs.djangoproject.com/en/5.0/ref/views/#the-500-server-error-view)
      * [The 403 (HTTP Forbidden) view](https://docs.djangoproject.com/en/5.0/ref/views/#the-403-http-forbidden-view)
      * [The 400 (bad request) view](https://docs.djangoproject.com/en/5.0/ref/views/#the-400-bad-request-view)


### Browse
  * Prev: [Validators](https://docs.djangoproject.com/en/5.0/ref/validators/)
  * Next: [Meta-documentation and miscellany](https://docs.djangoproject.com/en/5.0/misc/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * Built-in Views


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
