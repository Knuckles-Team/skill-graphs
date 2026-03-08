This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/csrf/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/csrf/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/csrf/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/csrf/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/csrf/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/csrf/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/csrf/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/csrf/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/csrf/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/csrf/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/csrf/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/csrf/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/csrf/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/csrf/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/csrf/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/csrf/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/csrf/)


  * [](https://docs.djangoproject.com/en/5.0/howto/csrf/#top)


# How to use Django’s CSRF protection[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#how-to-use-django-s-csrf-protection "Link to this heading")
To take advantage of CSRF protection in your views, follow these steps:
  1. The CSRF middleware is activated by default in the [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) setting. If you override that setting, remember that `'django.middleware.csrf.CsrfViewMiddleware'` should come before any view middleware that assume that CSRF attacks have been dealt with.
If you disabled it, which is not recommended, you can use [`csrf_protect()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.csrf_protect "django.views.decorators.csrf.csrf_protect") on particular views you want to protect (see below).
  2. In any template that uses a POST form, use the [`csrf_token`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-csrf_token) tag inside the `<form>` element if the form is for an internal URL, e.g.:
```
<form method="post">{% csrf_token %}

```

This should not be done for POST forms that target external URLs, since that would cause the CSRF token to be leaked, leading to a vulnerability.
  3. In the corresponding view functions, ensure that [`RequestContext`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.RequestContext "django.template.RequestContext") is used to render the response so that `{% csrf_token %}` will work properly. If you’re using the [`render()`](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#django.shortcuts.render "django.shortcuts.render") function, generic views, or contrib apps, you are covered already since these all use `RequestContext`.


## Using CSRF protection with AJAX[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#using-csrf-protection-with-ajax "Link to this heading")
While the above method can be used for AJAX POST requests, it has some inconveniences: you have to remember to pass the CSRF token in as POST data with every POST request. For this reason, there is an alternative method: on each XMLHttpRequest, set a custom `X-CSRFToken` header (as specified by the [`CSRF_HEADER_NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_HEADER_NAME) setting) to the value of the CSRF token. This is often easier because many JavaScript frameworks provide hooks that allow headers to be set on every request.
First, you must get the CSRF token. How to do that depends on whether or not the [`CSRF_USE_SESSIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_USE_SESSIONS) and [`CSRF_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_HTTPONLY) settings are enabled.
### Acquiring the token if [`CSRF_USE_SESSIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_USE_SESSIONS) and [`CSRF_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_HTTPONLY) are `False`[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#acquiring-the-token-if-csrf-use-sessions-and-csrf-cookie-httponly-are-false "Link to this heading")
The recommended source for the token is the `csrftoken` cookie, which will be set if you’ve enabled CSRF protection for your views as outlined above.
The CSRF token cookie is named `csrftoken` by default, but you can control the cookie name via the [`CSRF_COOKIE_NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_NAME) setting.
You can acquire the token like this:
```
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

```

The above code could be simplified by using the `getCookie`:
```
const csrftoken = Cookies.get('csrftoken');

```

Note
The CSRF token is also present in the DOM in a masked form, but only if explicitly included using [`csrf_token`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-csrf_token) in a template. The cookie contains the canonical, unmasked token. The [`CsrfViewMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.csrf.CsrfViewMiddleware "django.middleware.csrf.CsrfViewMiddleware") will accept either. However, in order to protect against
Warning
If your view is not rendering a template containing the [`csrf_token`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-csrf_token) template tag, Django might not set the CSRF token cookie. This is common in cases where forms are dynamically added to the page. To address this case, Django provides a view decorator which forces setting of the cookie: [`ensure_csrf_cookie()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.ensure_csrf_cookie "django.views.decorators.csrf.ensure_csrf_cookie").
### Acquiring the token if [`CSRF_USE_SESSIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_USE_SESSIONS) or [`CSRF_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_HTTPONLY) is `True`[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#acquiring-the-token-if-csrf-use-sessions-or-csrf-cookie-httponly-is-true "Link to this heading")
If you activate [`CSRF_USE_SESSIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_USE_SESSIONS) or [`CSRF_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_HTTPONLY), you must include the CSRF token in your HTML and read the token from the DOM with JavaScript:
```
{% csrf_token %}
<script>
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
</script>

```

### Setting the token on the AJAX request[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#setting-the-token-on-the-ajax-request "Link to this heading")
Finally, you’ll need to set the header on your AJAX request. Using the
```
const request = new Request(
    /* URL */,
    {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin' // Do not send CSRF token to another domain.
    }
);
fetch(request).then(function(response) {
    // ...
});

```

## Using CSRF protection in Jinja2 templates[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#using-csrf-protection-in-jinja2-templates "Link to this heading")
Django’s [`Jinja2`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.backends.jinja2.Jinja2 "django.template.backends.jinja2.Jinja2") template backend adds `{{ csrf_input }}` to the context of all templates which is equivalent to `{% csrf_token %}` in the Django template language. For example:
```
<form method="post">{{ csrf_input }}

```

## Using the decorator method[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#using-the-decorator-method "Link to this heading")
Rather than adding `CsrfViewMiddleware` as a blanket protection, you can use the [`csrf_protect()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.csrf_protect "django.views.decorators.csrf.csrf_protect") decorator, which has exactly the same functionality, on particular views that need the protection. It must be used **both** on views that insert the CSRF token in the output, and on those that accept the POST form data. (These are often the same view function, but not always).
Use of the decorator by itself is **not recommended** , since if you forget to use it, you will have a security hole. The ‘belt and braces’ strategy of using both is fine, and will incur minimal overhead.
## Handling rejected requests[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#handling-rejected-requests "Link to this heading")
By default, a ‘403 Forbidden’ response is sent to the user if an incoming request fails the checks performed by `CsrfViewMiddleware`. This should usually only be seen when there is a genuine Cross Site Request Forgery, or when, due to a programming error, the CSRF token has not been included with a POST form.
The error page, however, is not very friendly, so you may want to provide your own view for handling this condition. To do this, set the [`CSRF_FAILURE_VIEW`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_FAILURE_VIEW) setting.
CSRF failures are logged as warnings to the [django.security.csrf](https://docs.djangoproject.com/en/5.0/ref/logging/#django-security-logger) logger.
## Using CSRF protection with caching[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#using-csrf-protection-with-caching "Link to this heading")
If the [`csrf_token`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-csrf_token) template tag is used by a template (or the `get_token` function is called some other way), `CsrfViewMiddleware` will add a cookie and a `Vary: Cookie` header to the response. This means that the middleware will play well with the cache middleware if it is used as instructed (`UpdateCacheMiddleware` goes before all other middleware).
However, if you use cache decorators on individual views, the CSRF middleware will not yet have been able to set the Vary header or the CSRF cookie, and the response will be cached without either one. In this case, on any views that will require a CSRF token to be inserted you should use the [`django.views.decorators.csrf.csrf_protect()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.csrf_protect "django.views.decorators.csrf.csrf_protect") decorator first:
```
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect


@cache_page(60 * 15)
@csrf_protect
def my_view(request): ...

```

If you are using class-based views, you can refer to [Decorating class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#id1).
## Testing and CSRF protection[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#testing-and-csrf-protection "Link to this heading")
The `CsrfViewMiddleware` will usually be a big hindrance to testing view functions, due to the need for the CSRF token which must be sent with every POST request. For this reason, Django’s HTTP client for tests has been modified to set a flag on requests which relaxes the middleware and the `csrf_protect` decorator so that they no longer rejects requests. In every other respect (e.g. sending cookies etc.), they behave the same.
If, for some reason, you _want_ the test client to perform CSRF checks, you can create an instance of the test client that enforces CSRF checks:
```
>>> from django.test import Client
>>> csrf_client = Client(enforce_csrf_checks=True)

```

## Edge cases[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#edge-cases "Link to this heading")
Certain views can have unusual requirements that mean they don’t fit the normal pattern envisaged here. A number of utilities can be useful in these situations. The scenarios they might be needed in are described in the following section.
### Disabling CSRF protection for just a few views[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#disabling-csrf-protection-for-just-a-few-views "Link to this heading")
Most views requires CSRF protection, but a few do not.
Solution: rather than disabling the middleware and applying `csrf_protect` to all the views that need it, enable the middleware and use [`csrf_exempt()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.csrf_exempt "django.views.decorators.csrf.csrf_exempt").
### Setting the token when `CsrfViewMiddleware.process_view()` is not used[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#setting-the-token-when-csrfviewmiddleware-process-view-is-not-used "Link to this heading")
There are cases when `CsrfViewMiddleware.process_view` may not have run before your view is run - 404 and 500 handlers, for example - but you still need the CSRF token in a form.
Solution: use [`requires_csrf_token()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.requires_csrf_token "django.views.decorators.csrf.requires_csrf_token")
### Including the CSRF token in an unprotected view[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#including-the-csrf-token-in-an-unprotected-view "Link to this heading")
There may be some views that are unprotected and have been exempted by `csrf_exempt`, but still need to include the CSRF token.
Solution: use [`csrf_exempt()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.csrf_exempt "django.views.decorators.csrf.csrf_exempt") followed by [`requires_csrf_token()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.requires_csrf_token "django.views.decorators.csrf.requires_csrf_token"). (i.e. `requires_csrf_token` should be the innermost decorator).
### Protecting a view for only one path[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#protecting-a-view-for-only-one-path "Link to this heading")
A view needs CSRF protection under one set of conditions only, and mustn’t have it for the rest of the time.
Solution: use [`csrf_exempt()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.csrf_exempt "django.views.decorators.csrf.csrf_exempt") for the whole view function, and [`csrf_protect()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.csrf_protect "django.views.decorators.csrf.csrf_protect") for the path within it that needs protection. Example:
```
from django.views.decorators.csrf import csrf_exempt, csrf_protect


@csrf_exempt
def my_view(request):
    @csrf_protect
    def protected_path(request):
        do_something()

    if some_condition():
        return protected_path(request)
    else:
        do_something_else()

```

### Protecting a page that uses AJAX without an HTML form[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#protecting-a-page-that-uses-ajax-without-an-html-form "Link to this heading")
A page makes a POST request via AJAX, and the page does not have an HTML form with a [`csrf_token`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-csrf_token) that would cause the required CSRF cookie to be sent.
Solution: use [`ensure_csrf_cookie()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.ensure_csrf_cookie "django.views.decorators.csrf.ensure_csrf_cookie") on the view that sends the page.
## CSRF protection in reusable applications[¶](https://docs.djangoproject.com/en/5.0/howto/csrf/#csrf-protection-in-reusable-applications "Link to this heading")
Because it is possible for the developer to turn off the `CsrfViewMiddleware`, all relevant views in contrib apps use the `csrf_protect` decorator to ensure the security of these applications against CSRF. It is recommended that the developers of other reusable apps that want the same guarantees also use the `csrf_protect` decorator on their views.
Previous page and next page
[`REMOTE_USER`](https://docs.djangoproject.com/en/5.0/howto/auth-remote-user/)
[How to create custom `django-admin` commands ](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/)
[](https://docs.djangoproject.com/en/5.0/howto/csrf/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Tree Service Rockford, IL donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to use Django’s CSRF protection](https://docs.djangoproject.com/en/5.0/howto/csrf/)
    * [Using CSRF protection with AJAX](https://docs.djangoproject.com/en/5.0/howto/csrf/#using-csrf-protection-with-ajax)
      * [Acquiring the token if `CSRF_USE_SESSIONS` and `CSRF_COOKIE_HTTPONLY` are `False`](https://docs.djangoproject.com/en/5.0/howto/csrf/#acquiring-the-token-if-csrf-use-sessions-and-csrf-cookie-httponly-are-false)
      * [Acquiring the token if `CSRF_USE_SESSIONS` or `CSRF_COOKIE_HTTPONLY` is `True`](https://docs.djangoproject.com/en/5.0/howto/csrf/#acquiring-the-token-if-csrf-use-sessions-or-csrf-cookie-httponly-is-true)
      * [Setting the token on the AJAX request](https://docs.djangoproject.com/en/5.0/howto/csrf/#setting-the-token-on-the-ajax-request)
    * [Using CSRF protection in Jinja2 templates](https://docs.djangoproject.com/en/5.0/howto/csrf/#using-csrf-protection-in-jinja2-templates)
    * [Using the decorator method](https://docs.djangoproject.com/en/5.0/howto/csrf/#using-the-decorator-method)
    * [Handling rejected requests](https://docs.djangoproject.com/en/5.0/howto/csrf/#handling-rejected-requests)
    * [Using CSRF protection with caching](https://docs.djangoproject.com/en/5.0/howto/csrf/#using-csrf-protection-with-caching)
    * [Testing and CSRF protection](https://docs.djangoproject.com/en/5.0/howto/csrf/#testing-and-csrf-protection)
    * [Edge cases](https://docs.djangoproject.com/en/5.0/howto/csrf/#edge-cases)
      * [Disabling CSRF protection for just a few views](https://docs.djangoproject.com/en/5.0/howto/csrf/#disabling-csrf-protection-for-just-a-few-views)
      * [Setting the token when `CsrfViewMiddleware.process_view()` is not used](https://docs.djangoproject.com/en/5.0/howto/csrf/#setting-the-token-when-csrfviewmiddleware-process-view-is-not-used)
      * [Including the CSRF token in an unprotected view](https://docs.djangoproject.com/en/5.0/howto/csrf/#including-the-csrf-token-in-an-unprotected-view)
      * [Protecting a view for only one path](https://docs.djangoproject.com/en/5.0/howto/csrf/#protecting-a-view-for-only-one-path)
      * [Protecting a page that uses AJAX without an HTML form](https://docs.djangoproject.com/en/5.0/howto/csrf/#protecting-a-page-that-uses-ajax-without-an-html-form)
    * [CSRF protection in reusable applications](https://docs.djangoproject.com/en/5.0/howto/csrf/#csrf-protection-in-reusable-applications)


### Browse
  * Prev: [How to authenticate using `REMOTE_USER`](https://docs.djangoproject.com/en/5.0/howto/auth-remote-user/)
  * Next: [How to create custom `django-admin` commands](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to use Django’s CSRF protection


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
