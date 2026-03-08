This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/csrf/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/csrf/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/csrf/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/csrf/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/csrf/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/csrf/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/csrf/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/csrf/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/csrf/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/csrf/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/csrf/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/csrf/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/csrf/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/csrf/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/csrf/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/csrf/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/csrf/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/csrf/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/csrf/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/csrf/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/csrf/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/csrf/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/csrf/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/csrf/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/csrf/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/csrf/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/csrf/)


  * [](https://docs.djangoproject.com/en/5.0/ref/csrf/#top)


# Cross Site Request Forgery protection[¶](https://docs.djangoproject.com/en/5.0/ref/csrf/#module-django.middleware.csrf "Link to this heading")
The CSRF middleware and template tag provides easy-to-use protection against
The first defense against CSRF attacks is to ensure that GET requests (and other ‘safe’ methods, as defined by [How to use Django’s CSRF protection](https://docs.djangoproject.com/en/5.0/howto/csrf/#using-csrf).
## How it works[¶](https://docs.djangoproject.com/en/5.0/ref/csrf/#how-it-works "Link to this heading")
The CSRF protection is based on the following things:
  1. A CSRF cookie that is a random secret value, which other sites will not have access to.
`CsrfViewMiddleware` sends this cookie with the response whenever `django.middleware.csrf.get_token()` is called. It can also send it in other cases. For security reasons, the value of the secret is changed each time a user logs in.
  2. A hidden form field with the name ‘csrfmiddlewaretoken’, present in all outgoing POST forms.
In order to protect against `get_token()`, so the form field value is different each time.
This part is done by the template tag.
  3. For all incoming requests that are not using HTTP GET, HEAD, OPTIONS or TRACE, a CSRF cookie must be present, and the ‘csrfmiddlewaretoken’ field must be present and correct. If it isn’t, the user will get a 403 error.
When validating the ‘csrfmiddlewaretoken’ field value, only the secret, not the full token, is compared with the secret in the cookie value. This allows the use of ever-changing tokens. While each request may use its own token, the secret remains common to all.
This check is done by `CsrfViewMiddleware`.
  4. `CsrfViewMiddleware` verifies the [`CSRF_TRUSTED_ORIGINS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_TRUSTED_ORIGINS) setting. This provides protection against cross-subdomain attacks.
  5. In addition, for HTTPS requests, if the `Origin` header isn’t provided, `CsrfViewMiddleware` performs strict referer checking. This means that even if a subdomain can set or modify cookies on your domain, it can’t force a user to post to your application since that request won’t come from your own exact domain.
This also addresses a man-in-the-middle attack that’s possible under HTTPS when using a session independent secret, due to the fact that HTTP `Set-Cookie` headers are (unfortunately) accepted by clients even when they are talking to a site under HTTPS. (Referer checking is not done for HTTP requests because the presence of the `Referer` header isn’t reliable enough under HTTP.)
If the [`CSRF_COOKIE_DOMAIN`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_DOMAIN) setting is set, the referer is compared against it. You can allow cross-subdomain requests by including a leading dot. For example, `CSRF_COOKIE_DOMAIN = '.example.com'` will allow POST requests from `www.example.com` and `api.example.com`. If the setting is not set, then the referer must match the HTTP `Host` header.
Expanding the accepted referers beyond the current host or cookie domain can be done with the [`CSRF_TRUSTED_ORIGINS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_TRUSTED_ORIGINS) setting.


This ensures that only forms that have originated from trusted domains can be used to POST data back.
It deliberately ignores GET requests (and other requests that are defined as ‘safe’ by
The CSRF protection cannot protect against man-in-the-middle attacks, so use [HTTPS](https://docs.djangoproject.com/en/5.0/topics/security/#security-recommendation-ssl) with [HTTP Strict Transport Security](https://docs.djangoproject.com/en/5.0/ref/middleware/#http-strict-transport-security). It also assumes [validation of the HOST header](https://docs.djangoproject.com/en/5.0/topics/security/#host-headers-virtual-hosting) and that there aren’t any [cross-site scripting vulnerabilities](https://docs.djangoproject.com/en/5.0/topics/security/#cross-site-scripting) on your site (because XSS vulnerabilities already let an attacker do anything a CSRF vulnerability allows and much worse).
Removing the `Referer` header
To avoid disclosing the referrer URL to third-party sites, you might want to `<a>` tags. For example, you might use the `<meta name="referrer" content="no-referrer">` tag or include the `Referrer-Policy: no-referrer` header. Due to the CSRF protection’s strict referer checking on HTTPS requests, those techniques cause a CSRF failure on requests with ‘unsafe’ methods. Instead, use alternatives like `<a rel="noreferrer" ...>"` for links to third-party sites.
## Limitations[¶](https://docs.djangoproject.com/en/5.0/ref/csrf/#limitations "Link to this heading")
Subdomains within a site will be able to set cookies on the client for the whole domain. By setting the cookie and using a corresponding token, subdomains will be able to circumvent the CSRF protection. The only way to avoid this is to ensure that subdomains are controlled by trusted users (or, are at least unable to set cookies). Note that even without CSRF, there are other vulnerabilities, such as session fixation, that make giving subdomains to untrusted parties a bad idea, and these vulnerabilities cannot easily be fixed with current browsers.
## Utilities[¶](https://docs.djangoproject.com/en/5.0/ref/csrf/#module-django.views.decorators.csrf "Link to this heading")
The examples below assume you are using function-based views. If you are working with class-based views, you can refer to [Decorating class-based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#id1).

csrf_exempt(_view_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/views/decorators/csrf/#csrf_exempt)[¶](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.csrf_exempt "Link to this definition")

This decorator marks a view as being exempt from the protection ensured by the middleware. Example:
```
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def my_view(request):
    return HttpResponse("Hello world")

```

Changed in Django 5.0:
Support for wrapping asynchronous view functions was added.

csrf_protect(_view_)[¶](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.csrf_protect "Link to this definition")

Decorator that provides the protection of `CsrfViewMiddleware` to a view.
Usage:
```
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def my_view(request):
    c = {}
    # ...
    return render(request, "a_template.html", c)

```

Changed in Django 5.0:
Support for wrapping asynchronous view functions was added.

requires_csrf_token(_view_)[¶](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.requires_csrf_token "Link to this definition")

Normally the [`csrf_token`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-csrf_token) template tag will not work if `CsrfViewMiddleware.process_view` or an equivalent like `csrf_protect` has not run. The view decorator `requires_csrf_token` can be used to ensure the template tag does work. This decorator works similarly to `csrf_protect`, but never rejects an incoming request.
Example:
```
from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token


@requires_csrf_token
def my_view(request):
    c = {}
    # ...
    return render(request, "a_template.html", c)

```

Changed in Django 5.0:
Support for wrapping asynchronous view functions was added.

ensure_csrf_cookie(_view_)[¶](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.ensure_csrf_cookie "Link to this definition")

This decorator forces a view to send the CSRF cookie.
Changed in Django 5.0:
Support for wrapping asynchronous view functions was added.
## Settings[¶](https://docs.djangoproject.com/en/5.0/ref/csrf/#settings "Link to this heading")
A number of settings can be used to control Django’s CSRF behavior:
  * [`CSRF_COOKIE_AGE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_AGE)
  * [`CSRF_COOKIE_DOMAIN`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_DOMAIN)
  * [`CSRF_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_HTTPONLY)
  * [`CSRF_COOKIE_NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_NAME)
  * [`CSRF_COOKIE_PATH`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_PATH)
  * [`CSRF_COOKIE_SAMESITE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_SAMESITE)
  * [`CSRF_COOKIE_SECURE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_SECURE)
  * [`CSRF_FAILURE_VIEW`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_FAILURE_VIEW)
  * [`CSRF_HEADER_NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_HEADER_NAME)
  * [`CSRF_TRUSTED_ORIGINS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_TRUSTED_ORIGINS)
  * [`CSRF_USE_SESSIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_USE_SESSIONS)


## Frequently Asked Questions[¶](https://docs.djangoproject.com/en/5.0/ref/csrf/#frequently-asked-questions "Link to this heading")
### Is posting an arbitrary CSRF token pair (cookie and POST data) a vulnerability?[¶](https://docs.djangoproject.com/en/5.0/ref/csrf/#is-posting-an-arbitrary-csrf-token-pair-cookie-and-post-data-a-vulnerability "Link to this heading")
No, this is by design. Without a man-in-the-middle attack, there is no way for an attacker to send a CSRF token cookie to a victim’s browser, so a successful attack would need to obtain the victim’s browser’s cookie via XSS or similar, in which case an attacker usually doesn’t need CSRF attacks.
Some security audit tools flag this as a problem but as mentioned before, an attacker cannot steal a user’s browser’s CSRF cookie. “Stealing” or modifying _your own_ token using Firebug, Chrome dev tools, etc. isn’t a vulnerability.
### Is it a problem that Django’s CSRF protection isn’t linked to a session by default?[¶](https://docs.djangoproject.com/en/5.0/ref/csrf/#is-it-a-problem-that-django-s-csrf-protection-isn-t-linked-to-a-session-by-default "Link to this heading")
No, this is by design. Not linking CSRF protection to a session allows using the protection on sites such as a _pastebin_ that allow submissions from anonymous users which don’t have a session.
If you wish to store the CSRF token in the user’s session, use the [`CSRF_USE_SESSIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_USE_SESSIONS) setting.
### Why might a user encounter a CSRF validation failure after logging in?[¶](https://docs.djangoproject.com/en/5.0/ref/csrf/#why-might-a-user-encounter-a-csrf-validation-failure-after-logging-in "Link to this heading")
For security reasons, CSRF tokens are rotated each time a user logs in. Any page with a form generated before a login will have an old, invalid CSRF token and need to be reloaded. This might happen if a user uses the back button after a login or if they log in a different browser tab.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/contrib/syndication/)
[Databases ](https://docs.djangoproject.com/en/5.0/ref/databases/)
[](https://docs.djangoproject.com/en/5.0/ref/csrf/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Launch Lab donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Cross Site Request Forgery protection](https://docs.djangoproject.com/en/5.0/ref/csrf/)
    * [How it works](https://docs.djangoproject.com/en/5.0/ref/csrf/#how-it-works)
    * [Limitations](https://docs.djangoproject.com/en/5.0/ref/csrf/#limitations)
    * [Utilities](https://docs.djangoproject.com/en/5.0/ref/csrf/#module-django.views.decorators.csrf)
    * [Settings](https://docs.djangoproject.com/en/5.0/ref/csrf/#settings)
    * [Frequently Asked Questions](https://docs.djangoproject.com/en/5.0/ref/csrf/#frequently-asked-questions)
      * [Is posting an arbitrary CSRF token pair (cookie and POST data) a vulnerability?](https://docs.djangoproject.com/en/5.0/ref/csrf/#is-posting-an-arbitrary-csrf-token-pair-cookie-and-post-data-a-vulnerability)
      * [Is it a problem that Django’s CSRF protection isn’t linked to a session by default?](https://docs.djangoproject.com/en/5.0/ref/csrf/#is-it-a-problem-that-django-s-csrf-protection-isn-t-linked-to-a-session-by-default)
      * [Why might a user encounter a CSRF validation failure after logging in?](https://docs.djangoproject.com/en/5.0/ref/csrf/#why-might-a-user-encounter-a-csrf-validation-failure-after-logging-in)


### Browse
  * Prev: [The syndication feed framework](https://docs.djangoproject.com/en/5.0/ref/contrib/syndication/)
  * Next: [Databases](https://docs.djangoproject.com/en/5.0/ref/databases/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * Cross Site Request Forgery protection


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
