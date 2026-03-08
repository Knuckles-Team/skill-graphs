This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/clickjacking/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/clickjacking/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/clickjacking/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/clickjacking/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/clickjacking/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/clickjacking/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/clickjacking/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/clickjacking/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/clickjacking/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/clickjacking/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/clickjacking/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/clickjacking/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/clickjacking/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/clickjacking/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/clickjacking/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/clickjacking/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/clickjacking/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/clickjacking/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/clickjacking/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/clickjacking/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/clickjacking/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/clickjacking/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/clickjacking/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/clickjacking/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/clickjacking/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/clickjacking/)


  * [](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#top)


# Clickjacking Protection[¶](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#module-django.middleware.clickjacking "Link to this heading")
The clickjacking middleware and decorators provide easy-to-use protection against
## An example of clickjacking[¶](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#an-example-of-clickjacking "Link to this heading")
Suppose an online store has a page where a logged in user can click “Buy Now” to purchase an item. A user has chosen to stay logged into the store all the time for convenience. An attacker site might create an “I Like Ponies” button on one of their own pages, and load the store’s page in a transparent iframe such that the “Buy Now” button is invisibly overlaid on the “I Like Ponies” button. If the user visits the attacker’s site, clicking “I Like Ponies” will cause an inadvertent click on the “Buy Now” button and an unknowing purchase of the item.
## Preventing clickjacking[¶](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#preventing-clickjacking "Link to this heading")
Modern browsers honor the `SAMEORIGIN` then the browser will only load the resource in a frame if the request originated from the same site. If the header is set to `DENY` then the browser will block the resource from loading in a frame no matter which site made the request.
Django provides a few ways to include this header in responses from your site:
  1. A middleware that sets the header in all responses.
  2. A set of view decorators that can be used to override the middleware or to only set the header for certain views.


The `X-Frame-Options` HTTP header will only be set by the middleware or view decorators if it is not already present in the response.
## How to use it[¶](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#how-to-use-it "Link to this heading")
### Setting `X-Frame-Options` for all responses[¶](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#setting-x-frame-options-for-all-responses "Link to this heading")
To set the same `X-Frame-Options` value for all responses in your site, put `'django.middleware.clickjacking.XFrameOptionsMiddleware'` to [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE):
```
MIDDLEWARE = [
    ...,
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ...,
]

```

This middleware is enabled in the settings file generated by [`startproject`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startproject).
By default, the middleware will set the `X-Frame-Options` header to `DENY` for every outgoing `HttpResponse`. If you want any other value for this header instead, set the [`X_FRAME_OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-X_FRAME_OPTIONS) setting:
```
X_FRAME_OPTIONS = "SAMEORIGIN"

```

When using the middleware there may be some views where you do **not** want the `X-Frame-Options` header set. For those cases, you can use a view decorator that tells the middleware not to set the header:
```
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")

```

Note
If you want to submit a form or access a session cookie within a frame or iframe, you may need to modify the [`CSRF_COOKIE_SAMESITE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_SAMESITE) or [`SESSION_COOKIE_SAMESITE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_SAMESITE) settings.
Changed in Django 5.0:
Support for wrapping asynchronous view functions was added to the `@xframe_options_exempt` decorator.
### Setting `X-Frame-Options` per view[¶](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#setting-x-frame-options-per-view "Link to this heading")
To set the `X-Frame-Options` header on a per view basis, Django provides these decorators:
```
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin


@xframe_options_deny
def view_one(request):
    return HttpResponse("I won't display in any frame!")


@xframe_options_sameorigin
def view_two(request):
    return HttpResponse("Display in a frame if it's from the same origin as me.")

```

Note that you can use the decorators in conjunction with the middleware. Use of a decorator overrides the middleware.
Changed in Django 5.0:
Support for wrapping asynchronous view functions was added to the `@xframe_options_deny` and `@xframe_options_sameorigin` decorators.
## Limitations[¶](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#limitations "Link to this heading")
The `X-Frame-Options` header will only protect against clickjacking in
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/)
[`contrib` packages ](https://docs.djangoproject.com/en/5.0/ref/contrib/)
[](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Jiratip Wutthichayan donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Clickjacking Protection](https://docs.djangoproject.com/en/5.0/ref/clickjacking/)
    * [An example of clickjacking](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#an-example-of-clickjacking)
    * [Preventing clickjacking](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#preventing-clickjacking)
    * [How to use it](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#how-to-use-it)
      * [Setting `X-Frame-Options` for all responses](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#setting-x-frame-options-for-all-responses)
      * [Setting `X-Frame-Options` per view](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#setting-x-frame-options-per-view)
    * [Limitations](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#limitations)


### Browse
  * Prev: [Class-based generic views - flattened index](https://docs.djangoproject.com/en/5.0/ref/class-based-views/flattened-index/)
  * Next: [`contrib` packages](https://docs.djangoproject.com/en/5.0/ref/contrib/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * Clickjacking Protection


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
