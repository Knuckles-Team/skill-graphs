This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/http/views/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/http/views/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/http/views/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/http/views/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/http/views/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/http/views/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/http/views/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/http/views/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/http/views/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/http/views/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/http/views/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/http/views/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/http/views/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/http/views/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/http/views/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/http/views/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/http/views/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/http/views/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/http/views/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/http/views/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/http/views/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/http/views/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/http/views/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/http/views/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/http/views/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/http/views/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/http/views/)


  * [](https://docs.djangoproject.com/en/5.0/topics/http/views/#top)


# Writing views[¶](https://docs.djangoproject.com/en/5.0/topics/http/views/#writing-views "Link to this heading")
A view function, or _view_ for short, is a Python function that takes a web request and returns a web response. This response can be the HTML contents of a web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really. The view itself contains whatever arbitrary logic is necessary to return that response. This code can live anywhere you want, as long as it’s on your Python path. There’s no other requirement–no “magic,” so to speak. For the sake of putting the code _somewhere_ , the convention is to put views in a file called `views.py`, placed in your project or application directory.
## A simple view[¶](https://docs.djangoproject.com/en/5.0/topics/http/views/#a-simple-view "Link to this heading")
Here’s a view that returns the current date and time, as an HTML document:
```
from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

```

Let’s step through this code one line at a time:
  * First, we import the class [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") from the [`django.http`](https://docs.djangoproject.com/en/5.0/ref/request-response/#module-django.http "django.http: Classes dealing with HTTP requests and responses.") module, along with Python’s `datetime` library.
  * Next, we define a function called `current_datetime`. This is the view function. Each view function takes an [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") object as its first parameter, which is typically named `request`.
Note that the name of the view function doesn’t matter; it doesn’t have to be named in a certain way in order for Django to recognize it. We’re calling it `current_datetime` here, because that name clearly indicates what it does.
  * The view returns an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") object that contains the generated response. Each view function is responsible for returning an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") object. (There are exceptions, but we’ll get to those later.)


Django’s Time Zone
Django includes a [`TIME_ZONE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_ZONE) setting that defaults to `America/Chicago`. This probably isn’t where you live, so you might want to change it in your settings file.
## Mapping URLs to views[¶](https://docs.djangoproject.com/en/5.0/topics/http/views/#mapping-urls-to-views "Link to this heading")
So, to recap, this view function returns an HTML page that includes the current date and time. To display this view at a particular URL, you’ll need to create a _URLconf_ ; see [URL dispatcher](https://docs.djangoproject.com/en/5.0/topics/http/urls/) for instructions.
## Returning errors[¶](https://docs.djangoproject.com/en/5.0/topics/http/views/#returning-errors "Link to this heading")
Django provides help for returning HTTP error codes. There are subclasses of [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") for a number of common HTTP status codes other than 200 (which means _“OK”_). You can find the full list of available subclasses in the [request/response](https://docs.djangoproject.com/en/5.0/ref/request-response/#ref-httpresponse-subclasses) documentation. Return an instance of one of those subclasses instead of a normal [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") in order to signify an error. For example:
```
from django.http import HttpResponse, HttpResponseNotFound


def my_view(request):
    # ...
    if foo:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    else:
        return HttpResponse("<h1>Page was found</h1>")

```

There isn’t a specialized subclass for every possible HTTP response code, since many of them aren’t going to be that common. However, as documented in the [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") documentation, you can also pass the HTTP status code into the constructor for [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") to create a return class for any status code you like. For example:
```
from django.http import HttpResponse


def my_view(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)

```

Because 404 errors are by far the most common HTTP error, there’s an easier way to handle those errors.
### The `Http404` exception[¶](https://docs.djangoproject.com/en/5.0/topics/http/views/#the-http404-exception "Link to this heading")

_class_ django.http.Http404[¶](https://docs.djangoproject.com/en/5.0/topics/http/views/#django.http.Http404 "Link to this definition")

When you return an error such as [`HttpResponseNotFound`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseNotFound "django.http.HttpResponseNotFound"), you’re responsible for defining the HTML of the resulting error page:
```
return HttpResponseNotFound("<h1>Page not found</h1>")

```

For convenience, and because it’s a good idea to have a consistent 404 error page across your site, Django provides an `Http404` exception. If you raise `Http404` at any point in a view function, Django will catch it and return the standard error page for your application, along with an HTTP error code 404.
Example usage:
```
from django.http import Http404
from django.shortcuts import render
from polls.models import Poll


def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("Poll does not exist")
    return render(request, "polls/detail.html", {"poll": p})

```

In order to show customized HTML when Django returns a 404, you can create an HTML template named `404.html` and place it in the top level of your template tree. This template will then be served when [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is set to `False`.
When [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is `True`, you can provide a message to `Http404` and it will appear in the standard 404 debug template. Use these messages for debugging purposes; they generally aren’t suitable for use in a production 404 template.
## Customizing error views[¶](https://docs.djangoproject.com/en/5.0/topics/http/views/#customizing-error-views "Link to this heading")
The default error views in Django should suffice for most web applications, but can easily be overridden if you need any custom behavior. Specify the handlers as seen below in your URLconf (setting them anywhere else will have no effect).
The [`page_not_found()`](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.defaults.page_not_found "django.views.defaults.page_not_found") view is overridden by [`handler404`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.conf.urls.handler404 "django.conf.urls.handler404"):
```
handler404 = "mysite.views.my_custom_page_not_found_view"

```

The [`server_error()`](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.defaults.server_error "django.views.defaults.server_error") view is overridden by [`handler500`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.conf.urls.handler500 "django.conf.urls.handler500"):
```
handler500 = "mysite.views.my_custom_error_view"

```

The [`permission_denied()`](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.defaults.permission_denied "django.views.defaults.permission_denied") view is overridden by [`handler403`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.conf.urls.handler403 "django.conf.urls.handler403"):
```
handler403 = "mysite.views.my_custom_permission_denied_view"

```

The [`bad_request()`](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.defaults.bad_request "django.views.defaults.bad_request") view is overridden by [`handler400`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.conf.urls.handler400 "django.conf.urls.handler400"):
```
handler400 = "mysite.views.my_custom_bad_request_view"

```

See also
Use the [`CSRF_FAILURE_VIEW`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_FAILURE_VIEW) setting to override the CSRF error view.
### Testing custom error views[¶](https://docs.djangoproject.com/en/5.0/topics/http/views/#testing-custom-error-views "Link to this heading")
To test the response of a custom error handler, raise the appropriate exception in a test view. For example:
```
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import SimpleTestCase, override_settings
from django.urls import path


def response_error_handler(request, exception=None):
    return HttpResponse("Error handler content", status=403)


def permission_denied_view(request):
    raise PermissionDenied


urlpatterns = [
    path("403/", permission_denied_view),
]

handler403 = response_error_handler


# ROOT_URLCONF must specify the module that contains handler403 = ...
@override_settings(ROOT_URLCONF=__name__)
class CustomErrorHandlerTests(SimpleTestCase):
    def test_handler_renders_template_response(self):
        response = self.client.get("/403/")
        # Make assertions on the response here. For example:
        self.assertContains(response, "Error handler content", status_code=403)

```

## Async views[¶](https://docs.djangoproject.com/en/5.0/topics/http/views/#async-views "Link to this heading")
As well as being synchronous functions, views can also be asynchronous (“async”) functions, normally defined using Python’s `async def` syntax. Django will automatically detect these and run them in an async context. However, you will need to use an async server based on ASGI to get their performance benefits.
Here’s an example of an async view:
```
import datetime
from django.http import HttpResponse


async def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

```

You can read more about Django’s async support, and how to best use async views, in [Asynchronous support](https://docs.djangoproject.com/en/5.0/topics/async/).
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/http/urls/)
[View decorators ](https://docs.djangoproject.com/en/5.0/topics/http/decorators/)
[](https://docs.djangoproject.com/en/5.0/topics/http/views/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Gilbert Garcia Group, P.A. donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Writing views](https://docs.djangoproject.com/en/5.0/topics/http/views/)
    * [A simple view](https://docs.djangoproject.com/en/5.0/topics/http/views/#a-simple-view)
    * [Mapping URLs to views](https://docs.djangoproject.com/en/5.0/topics/http/views/#mapping-urls-to-views)
    * [Returning errors](https://docs.djangoproject.com/en/5.0/topics/http/views/#returning-errors)
      * [The `Http404` exception](https://docs.djangoproject.com/en/5.0/topics/http/views/#the-http404-exception)
    * [Customizing error views](https://docs.djangoproject.com/en/5.0/topics/http/views/#customizing-error-views)
      * [Testing custom error views](https://docs.djangoproject.com/en/5.0/topics/http/views/#testing-custom-error-views)
    * [Async views](https://docs.djangoproject.com/en/5.0/topics/http/views/#async-views)


### Browse
  * Prev: [URL dispatcher](https://docs.djangoproject.com/en/5.0/topics/http/urls/)
  * Next: [View decorators](https://docs.djangoproject.com/en/5.0/topics/http/decorators/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * [Handling HTTP requests](https://docs.djangoproject.com/en/5.0/topics/http/)
        * Writing views


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
