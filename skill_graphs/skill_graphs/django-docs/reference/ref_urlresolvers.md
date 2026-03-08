This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/urlresolvers/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/urlresolvers/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/urlresolvers/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/urlresolvers/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/urlresolvers/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/urlresolvers/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/urlresolvers/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/urlresolvers/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/urlresolvers/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/urlresolvers/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/urlresolvers/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/urlresolvers/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/urlresolvers/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/urlresolvers/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/urlresolvers/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/urlresolvers/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/urlresolvers/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/urlresolvers/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/urlresolvers/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/urlresolvers/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/urlresolvers/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/urlresolvers/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/urlresolvers/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/urlresolvers/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/urlresolvers/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/urlresolvers/)


  * [](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#top)


#  `django.urls` utility functions[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#module-django.urls "Link to this heading")
##  `reverse()`[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#reverse "Link to this heading")
If you need to use something similar to the [`url`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-url) template tag in your code, Django provides the following function:

reverse(_viewname_ , _urlconf =None_, _args =None_, _kwargs =None_, _current_app =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/urls/base/#reverse)[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.reverse "Link to this definition")

`viewname` can be a [URL pattern name](https://docs.djangoproject.com/en/5.0/topics/http/urls/#naming-url-patterns) or the callable view object. For example, given the following `url`:
```
from news import views

path("archive/", views.archive, name="news-archive")

```

you can use any of the following to reverse the URL:
```
# using the named URL
reverse("news-archive")

# passing a callable object
# (This is discouraged because you can't reverse namespaced views this way.)
from news import views

reverse(views.archive)

```

If the URL accepts arguments, you may pass them in `args`. For example:
```
from django.urls import reverse


def myview(request):
    return HttpResponseRedirect(reverse("arch-summary", args=[1945]))

```

You can also pass `kwargs` instead of `args`. For example:
```
>>> reverse("admin:app_list", kwargs={"app_label": "auth"})
'/admin/auth/'

```

`args` and `kwargs` cannot be passed to `reverse()` at the same time.
If no match can be made, `reverse()` raises a [`NoReverseMatch`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.urls.NoReverseMatch "django.urls.NoReverseMatch") exception.
The `reverse()` function can reverse a large variety of regular expression patterns for URLs, but not every possible one. The main restriction at the moment is that the pattern cannot contain alternative choices using the vertical bar (`"|"`) character. You can quite happily use such patterns for matching against incoming URLs and sending them off to views, but you cannot reverse such patterns.
The `current_app` argument allows you to provide a hint to the resolver indicating the application to which the currently executing view belongs. This `current_app` argument is used as a hint to resolve application namespaces into URLs on specific application instances, according to the [namespaced URL resolution strategy](https://docs.djangoproject.com/en/5.0/topics/http/urls/#topics-http-reversing-url-namespaces).
The `urlconf` argument is the URLconf module containing the URL patterns to use for reversing. By default, the root URLconf for the current thread is used.
Note
The string returned by `reverse()` is already [urlquoted](https://docs.djangoproject.com/en/5.0/ref/unicode/#uri-and-iri-handling). For example:
```
>>> reverse("cities", args=["Orléans"])
'.../Orl%C3%A9ans/'

```

Applying further encoding (such as `reverse()` may produce undesirable results.
##  `reverse_lazy()`[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#reverse-lazy "Link to this heading")
A lazily evaluated version of [reverse()](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#reverse).

reverse_lazy(_viewname_ , _urlconf =None_, _args =None_, _kwargs =None_, _current_app =None_)[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.reverse_lazy "Link to this definition")

It is useful for when you need to use a URL reversal before your project’s URLConf is loaded. Some common cases where this function is necessary are:
  * providing a reversed URL as the `url` attribute of a generic class-based view.
  * providing a reversed URL to a decorator (such as the `login_url` argument for the [`django.contrib.auth.decorators.permission_required()`](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.decorators.permission_required "django.contrib.auth.decorators.permission_required") decorator).
  * providing a reversed URL as a default value for a parameter in a function’s signature.


##  `resolve()`[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#resolve "Link to this heading")
The `resolve()` function can be used for resolving URL paths to the corresponding view functions. It has the following signature:

resolve(_path_ , _urlconf =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/urls/base/#resolve)[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.resolve "Link to this definition")

`path` is the URL path you want to resolve. As with [`reverse()`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.reverse "django.urls.reverse"), you don’t need to worry about the `urlconf` parameter. The function returns a [`ResolverMatch`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch "django.urls.ResolverMatch") object that allows you to access various metadata about the resolved URL.
If the URL does not resolve, the function raises a [`Resolver404`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.urls.Resolver404 "django.urls.Resolver404") exception (a subclass of [`Http404`](https://docs.djangoproject.com/en/5.0/topics/http/views/#django.http.Http404 "django.http.Http404")) .

_class_ ResolverMatch[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/urls/resolvers/#ResolverMatch)[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch "Link to this definition")


func[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch.func "Link to this definition")

The view function that would be used to serve the URL

args[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch.args "Link to this definition")

The arguments that would be passed to the view function, as parsed from the URL.

kwargs[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch.kwargs "Link to this definition")

All keyword arguments that would be passed to the view function, i.e. [`captured_kwargs`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch.captured_kwargs "django.urls.ResolverMatch.captured_kwargs") and [`extra_kwargs`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch.extra_kwargs "django.urls.ResolverMatch.extra_kwargs").

captured_kwargs[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch.captured_kwargs "Link to this definition")

The captured keyword arguments that would be passed to the view function, as parsed from the URL.

extra_kwargs[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch.extra_kwargs "Link to this definition")

The additional keyword arguments that would be passed to the view function.

url_name[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch.url_name "Link to this definition")

The name of the URL pattern that matches the URL.

route[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch.route "Link to this definition")

The route of the matching URL pattern.
For example, if `path('users/<id>/', ...)` is the matching pattern, `route` will contain `'users/<id>/'`.

tried[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch.tried "Link to this definition")

The list of URL patterns tried before the URL either matched one or exhausted available patterns.

app_name[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch.app_name "Link to this definition")

The application namespace for the URL pattern that matches the URL.

app_names[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch.app_names "Link to this definition")

The list of individual namespace components in the full application namespace for the URL pattern that matches the URL. For example, if the `app_name` is `'foo:bar'`, then `app_names` will be `['foo', 'bar']`.

namespace[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch.namespace "Link to this definition")

The instance namespace for the URL pattern that matches the URL.

namespaces[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch.namespaces "Link to this definition")

The list of individual namespace components in the full instance namespace for the URL pattern that matches the URL. i.e., if the namespace is `foo:bar`, then namespaces will be `['foo', 'bar']`.

view_name[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch.view_name "Link to this definition")

The name of the view that matches the URL, including the namespace if there is one.
A [`ResolverMatch`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch "django.urls.ResolverMatch") object can then be interrogated to provide information about the URL pattern that matches a URL:
```
# Resolve a URL
match = resolve("/some/path/")
# Print the URL pattern that matches the URL
print(match.url_name)

```

A [`ResolverMatch`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch "django.urls.ResolverMatch") object can also be assigned to a triple:
```
func, args, kwargs = resolve("/some/path/")

```

One possible use of [`resolve()`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.resolve "django.urls.resolve") would be to test whether a view would raise a `Http404` error before redirecting to it:
```
from urllib.parse import urlparse
from django.urls import resolve
from django.http import Http404, HttpResponseRedirect


def myview(request):
    next = request.META.get("HTTP_REFERER", None) or "/"
    response = HttpResponseRedirect(next)

    # modify the request and response as required, e.g. change locale
    # and set corresponding locale cookie

    view, args, kwargs = resolve(urlparse(next)[2])
    kwargs["request"] = request
    try:
        view(*args, **kwargs)
    except Http404:
        return HttpResponseRedirect("/")
    return response

```

##  `get_script_prefix()`[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#get-script-prefix "Link to this heading")

get_script_prefix()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/urls/base/#get_script_prefix)[¶](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.get_script_prefix "Link to this definition")

Normally, you should always use [`reverse()`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.reverse "django.urls.reverse") to define URLs within your application. However, if your application constructs part of the URL hierarchy itself, you may occasionally need to generate URLs. In that case, you need to be able to find the base URL of the Django project within its web server (normally, [`reverse()`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.reverse "django.urls.reverse") takes care of this for you). In that case, you can call `get_script_prefix()`, which will return the script prefix portion of the URL for your Django project. If your Django project is at the root of its web server, this is always `"/"`.
Warning
This function **cannot** be used outside of the request-response cycle since it relies on values initialized during that cycle.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/unicode/)
[`django.urls` functions for use in URLconfs ](https://docs.djangoproject.com/en/5.0/ref/urls/)
[](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Mark H. Wright, PLLC donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [`django.urls` utility functions](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/)
    * [`reverse()`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#reverse)
    * [`reverse_lazy()`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#reverse-lazy)
    * [`resolve()`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#resolve)
    * [`get_script_prefix()`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#get-script-prefix)


### Browse
  * Prev: [Unicode data](https://docs.djangoproject.com/en/5.0/ref/unicode/)
  * Next: [`django.urls` functions for use in URLconfs](https://docs.djangoproject.com/en/5.0/ref/urls/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * `django.urls` utility functions


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
