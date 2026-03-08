This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/urls/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/urls/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/urls/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/urls/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/urls/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/urls/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/urls/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/urls/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/urls/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/urls/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/urls/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/urls/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/urls/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/urls/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/urls/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/urls/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/urls/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/urls/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/urls/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/urls/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/urls/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/urls/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/urls/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/urls/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/urls/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/urls/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/urls/)


  * [](https://docs.djangoproject.com/en/5.0/ref/urls/#top)


#  `django.urls` functions for use in URLconfs[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#module-django.urls.conf "Link to this heading")
##  `path()`[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#path "Link to this heading")

path(_route_ , _view_ , _kwargs =None_, _name =None_)[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.path "Link to this definition")

Returns an element for inclusion in `urlpatterns`. For example:
```
from django.urls import include, path

urlpatterns = [
    path("index/", views.index, name="main-view"),
    path("bio/<username>/", views.bio, name="bio"),
    path("articles/<slug:title>/", views.article, name="article-detail"),
    path("articles/<slug:title>/<int:section>/", views.section, name="article-section"),
    path("blog/", include("blog.urls")),
    ...,
]

```

The `route` argument should be a string or [`gettext_lazy()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.gettext_lazy "django.utils.translation.gettext_lazy") (see [Translating URL patterns](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/#translating-urlpatterns)) that contains a URL pattern. The string may contain angle brackets (like `<username>` above) to capture part of the URL and send it as a keyword argument to the view. The angle brackets may include a converter specification (like the `int` part of `<int:section>`) which limits the characters matched and may also change the type of the variable passed to the view. For example, `<int:section>` matches a string of decimal digits and converts the value to an `int`. See [How Django processes a request](https://docs.djangoproject.com/en/5.0/topics/http/urls/#how-django-processes-a-request) for more details.
The `view` argument is a view function or the result of [`as_view()`](https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view") for class-based views. It can also be an [`django.urls.include()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.include "django.urls.include").
The `kwargs` argument allows you to pass additional arguments to the view function or method. See [Passing extra options to view functions](https://docs.djangoproject.com/en/5.0/topics/http/urls/#views-extra-options) for an example.
See [Naming URL patterns](https://docs.djangoproject.com/en/5.0/topics/http/urls/#naming-url-patterns) for why the `name` argument is useful.
##  `re_path()`[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#re-path "Link to this heading")

re_path(_route_ , _view_ , _kwargs =None_, _name =None_)[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.re_path "Link to this definition")

Returns an element for inclusion in `urlpatterns`. For example:
```
from django.urls import include, re_path

urlpatterns = [
    re_path(r"^index/$", views.index, name="index"),
    re_path(r"^bio/(?P<username>\w+)/$", views.bio, name="bio"),
    re_path(r"^blog/", include("blog.urls")),
    ...,
]

```

The `route` argument should be a string or [`gettext_lazy()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.gettext_lazy "django.utils.translation.gettext_lazy") (see [Translating URL patterns](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/#translating-urlpatterns)) that contains a regular expression compatible with Python’s `r''`) so that they can contain sequences like `\d` without the need to escape the backslash with another backslash. When a match is made, captured groups from the regular expression are passed to the view – as named arguments if the groups are named, and as positional arguments otherwise. The values are passed as strings, without any type conversion.
When a `route` ends with `$` the whole requested URL, matching against [`path_info`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.path_info "django.http.HttpRequest.path_info"), must match the regular expression pattern (
The `view`, `kwargs` and `name` arguments are the same as for [`path()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.path "django.urls.path").
Changed in Django 2.2.25:
In older versions, a full-match wasn’t required for a `route` which ends with `$`.
##  `include()`[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#include "Link to this heading")

include(_module_ , _namespace =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/urls/conf/#include)[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.include "Link to this definition")


include(_pattern_list_)


include(_(pattern_list_ , _app_namespace)_ , _namespace=None_)

A function that takes a full Python import path to another URLconf module that should be “included” in this place. Optionally, the [application namespace](https://docs.djangoproject.com/en/5.0/topics/http/urls/#term-application-namespace) and [instance namespace](https://docs.djangoproject.com/en/5.0/topics/http/urls/#term-instance-namespace) where the entries will be included into can also be specified.
Usually, the application namespace should be specified by the included module. If an application namespace is set, the `namespace` argument can be used to set a different instance namespace.
`include()` also accepts as an argument either an iterable that returns URL patterns or a 2-tuple containing such iterable plus the names of the application namespaces.

Parameters:

  * **module** – URLconf module (or module name)
  * **namespace** (
  * **pattern_list** – Iterable of [`path()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.path "django.urls.path") and/or [`re_path()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.re_path "django.urls.re_path") instances.
  * **app_namespace** (


See [Including other URLconfs](https://docs.djangoproject.com/en/5.0/topics/http/urls/#including-other-urlconfs) and [URL namespaces and included URLconfs](https://docs.djangoproject.com/en/5.0/topics/http/urls/#namespaces-and-include).
##  `register_converter()`[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#register-converter "Link to this heading")

register_converter(_converter_ , _type_name_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/urls/converters/#register_converter)[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.register_converter "Link to this definition")

The function for registering a converter for use in [`path()`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.path "django.urls.path") `route`s.
The `converter` argument is a converter class, and `type_name` is the converter name to use in path patterns. See [Registering custom path converters](https://docs.djangoproject.com/en/5.0/topics/http/urls/#registering-custom-path-converters) for an example.
#  `django.conf.urls` functions for use in URLconfs[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#module-django.conf.urls "Link to this heading")
##  `static()`[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#static "Link to this heading")

static.static(_prefix_ , _view =django.views.static.serve_, _** kwargs_)[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#django.conf.urls.static.static "Link to this definition")

Helper function to return a URL pattern for serving files in debug mode:
```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

##  `handler400`[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#handler400 "Link to this heading")

handler400[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#django.conf.urls.handler400 "Link to this definition")

A callable, or a string representing the full Python import path to the view that should be called if the HTTP client has sent a request that caused an error condition and a response with a status code of 400.
By default, this is [`django.views.defaults.bad_request()`](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.defaults.bad_request "django.views.defaults.bad_request"). If you implement a custom view, be sure it accepts `request` and `exception` arguments and returns an [`HttpResponseBadRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseBadRequest "django.http.HttpResponseBadRequest").
##  `handler403`[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#handler403 "Link to this heading")

handler403[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#django.conf.urls.handler403 "Link to this definition")

A callable, or a string representing the full Python import path to the view that should be called if the user doesn’t have the permissions required to access a resource.
By default, this is [`django.views.defaults.permission_denied()`](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.defaults.permission_denied "django.views.defaults.permission_denied"). If you implement a custom view, be sure it accepts `request` and `exception` arguments and returns an [`HttpResponseForbidden`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseForbidden "django.http.HttpResponseForbidden").
##  `handler404`[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#handler404 "Link to this heading")

handler404[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#django.conf.urls.handler404 "Link to this definition")

A callable, or a string representing the full Python import path to the view that should be called if none of the URL patterns match.
By default, this is [`django.views.defaults.page_not_found()`](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.defaults.page_not_found "django.views.defaults.page_not_found"). If you implement a custom view, be sure it accepts `request` and `exception` arguments and returns an [`HttpResponseNotFound`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseNotFound "django.http.HttpResponseNotFound").
##  `handler500`[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#handler500 "Link to this heading")

handler500[¶](https://docs.djangoproject.com/en/5.0/ref/urls/#django.conf.urls.handler500 "Link to this definition")

A callable, or a string representing the full Python import path to the view that should be called in case of server errors. Server errors happen when you have runtime errors in view code.
By default, this is [`django.views.defaults.server_error()`](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.defaults.server_error "django.views.defaults.server_error"). If you implement a custom view, be sure it accepts a `request` argument and returns an [`HttpResponseServerError`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseServerError "django.http.HttpResponseServerError").
Previous page and next page
[`django.urls` utility functions](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/)
[Django Utils ](https://docs.djangoproject.com/en/5.0/ref/utils/)
[](https://docs.djangoproject.com/en/5.0/ref/urls/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Jonathan McKenzie donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [`django.urls` functions for use in URLconfs](https://docs.djangoproject.com/en/5.0/ref/urls/)
    * [`path()`](https://docs.djangoproject.com/en/5.0/ref/urls/#path)
    * [`re_path()`](https://docs.djangoproject.com/en/5.0/ref/urls/#re-path)
    * [`include()`](https://docs.djangoproject.com/en/5.0/ref/urls/#include)
    * [`register_converter()`](https://docs.djangoproject.com/en/5.0/ref/urls/#register-converter)
  * [`django.conf.urls` functions for use in URLconfs](https://docs.djangoproject.com/en/5.0/ref/urls/#module-django.conf.urls)
    * [`static()`](https://docs.djangoproject.com/en/5.0/ref/urls/#static)
    * [`handler400`](https://docs.djangoproject.com/en/5.0/ref/urls/#handler400)
    * [`handler403`](https://docs.djangoproject.com/en/5.0/ref/urls/#handler403)
    * [`handler404`](https://docs.djangoproject.com/en/5.0/ref/urls/#handler404)
    * [`handler500`](https://docs.djangoproject.com/en/5.0/ref/urls/#handler500)


### Browse
  * Prev: [`django.urls` utility functions](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/)
  * Next: [Django Utils](https://docs.djangoproject.com/en/5.0/ref/utils/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * `django.urls` functions for use in URLconfs


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
