This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/auth-remote-user/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/auth-remote-user/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/auth-remote-user/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/auth-remote-user/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/auth-remote-user/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/auth-remote-user/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/auth-remote-user/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/auth-remote-user/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/auth-remote-user/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/auth-remote-user/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/auth-remote-user/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/auth-remote-user/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/auth-remote-user/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/auth-remote-user/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/auth-remote-user/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/auth-remote-user/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/auth-remote-user/)
  * [4.0](https://docs.djangoproject.com/en/4.0/howto/auth-remote-user/)
  * [3.2](https://docs.djangoproject.com/en/3.2/howto/auth-remote-user/)
  * [3.1](https://docs.djangoproject.com/en/3.1/howto/auth-remote-user/)
  * [3.0](https://docs.djangoproject.com/en/3.0/howto/auth-remote-user/)
  * [2.2](https://docs.djangoproject.com/en/2.2/howto/auth-remote-user/)
  * [2.1](https://docs.djangoproject.com/en/2.1/howto/auth-remote-user/)
  * [2.0](https://docs.djangoproject.com/en/2.0/howto/auth-remote-user/)
  * [1.11](https://docs.djangoproject.com/en/1.11/howto/auth-remote-user/)
  * [1.10](https://docs.djangoproject.com/en/1.10/howto/auth-remote-user/)
  * [1.8](https://docs.djangoproject.com/en/1.8/howto/auth-remote-user/)


  * [](https://docs.djangoproject.com/en/5.0/howto/auth-remote-user/#top)


# How to authenticate using `REMOTE_USER`[¶](https://docs.djangoproject.com/en/5.0/howto/auth-remote-user/#how-to-authenticate-using-remote-user "Link to this heading")
This document describes how to make use of external authentication sources (where the web server sets the `REMOTE_USER` environment variable) in your Django applications. This type of authentication solution is typically seen on intranet sites, with single sign-on solutions such as IIS and Integrated Windows Authentication or Apache and
When the web server takes care of authentication it typically sets the `REMOTE_USER` environment variable for use in the underlying application. In Django, `REMOTE_USER` is made available in the [`request.META`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.META "django.http.HttpRequest.META") attribute. Django can be configured to make use of the `REMOTE_USER` value using the `RemoteUserMiddleware` or `PersistentRemoteUserMiddleware`, and [`RemoteUserBackend`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.backends.RemoteUserBackend "django.contrib.auth.backends.RemoteUserBackend") classes found in [`django.contrib.auth`](https://docs.djangoproject.com/en/5.0/topics/auth/#module-django.contrib.auth "django.contrib.auth: Django's authentication framework.").
## Configuration[¶](https://docs.djangoproject.com/en/5.0/howto/auth-remote-user/#configuration "Link to this heading")
First, you must add the [`django.contrib.auth.middleware.RemoteUserMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.auth.middleware.RemoteUserMiddleware "django.contrib.auth.middleware.RemoteUserMiddleware") to the [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) setting **after** the [`django.contrib.auth.middleware.AuthenticationMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.auth.middleware.AuthenticationMiddleware "django.contrib.auth.middleware.AuthenticationMiddleware"):
```
MIDDLEWARE = [
    "...",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.RemoteUserMiddleware",
    "...",
]

```

Next, you must replace the [`ModelBackend`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.backends.ModelBackend "django.contrib.auth.backends.ModelBackend") with [`RemoteUserBackend`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.backends.RemoteUserBackend "django.contrib.auth.backends.RemoteUserBackend") in the [`AUTHENTICATION_BACKENDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-AUTHENTICATION_BACKENDS) setting:
```
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.RemoteUserBackend",
]

```

With this setup, `RemoteUserMiddleware` will detect the username in `request.META['REMOTE_USER']` and will authenticate and auto-login that user using the [`RemoteUserBackend`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.backends.RemoteUserBackend "django.contrib.auth.backends.RemoteUserBackend").
Be aware that this particular setup disables authentication with the default `ModelBackend`. This means that if the `REMOTE_USER` value is not set then the user is unable to log in, even using Django’s admin interface. Adding `'django.contrib.auth.backends.ModelBackend'` to the `AUTHENTICATION_BACKENDS` list will use `ModelBackend` as a fallback if `REMOTE_USER` is absent, which will solve these issues.
Django’s user management, such as the views in `contrib.admin` and the [`createsuperuser`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-createsuperuser) management command, doesn’t integrate with remote users. These interfaces work with users stored in the database regardless of `AUTHENTICATION_BACKENDS`.
Note
Since the `RemoteUserBackend` inherits from `ModelBackend`, you will still have all of the same permissions checking that is implemented in `ModelBackend`.
Users with [`is_active=False`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.User.is_active "django.contrib.auth.models.User.is_active") won’t be allowed to authenticate. Use [`AllowAllUsersRemoteUserBackend`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.backends.AllowAllUsersRemoteUserBackend "django.contrib.auth.backends.AllowAllUsersRemoteUserBackend") if you want to allow them to.
If your authentication mechanism uses a custom HTTP header and not `REMOTE_USER`, you can subclass `RemoteUserMiddleware` and set the `header` attribute to the desired `request.META` key. For example:
```
from django.contrib.auth.middleware import RemoteUserMiddleware


class CustomHeaderMiddleware(RemoteUserMiddleware):
    header = "HTTP_AUTHUSER"

```

Warning
Be very careful if using a `RemoteUserMiddleware` subclass with a custom HTTP header. You must be sure that your front-end web server always sets or strips that header based on the appropriate authentication checks, never permitting an end-user to submit a fake (or “spoofed”) header value. Since the HTTP headers `X-Auth-User` and `X-Auth_User` (for example) both normalize to the `HTTP_X_AUTH_USER` key in `request.META`, you must also check that your web server doesn’t allow a spoofed header using underscores in place of dashes.
This warning doesn’t apply to `RemoteUserMiddleware` in its default configuration with `header = 'REMOTE_USER'`, since a key that doesn’t start with `HTTP_` in `request.META` can only be set by your WSGI server, not directly from an HTTP request header.
If you need more control, you can create your own authentication backend that inherits from [`RemoteUserBackend`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.backends.RemoteUserBackend "django.contrib.auth.backends.RemoteUserBackend") and override one or more of its attributes and methods.
## Using `REMOTE_USER` on login pages only[¶](https://docs.djangoproject.com/en/5.0/howto/auth-remote-user/#using-remote-user-on-login-pages-only "Link to this heading")
The `RemoteUserMiddleware` authentication middleware assumes that the HTTP request header `REMOTE_USER` is present with all authenticated requests. That might be expected and practical when Basic HTTP Auth with `htpasswd` or similar mechanisms are used, but with Negotiate (GSSAPI/Kerberos) or other resource intensive authentication methods, the authentication in the front-end HTTP server is usually only set up for one or a few login URLs, and after successful authentication, the application is supposed to maintain the authenticated session itself.
[`PersistentRemoteUserMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.auth.middleware.PersistentRemoteUserMiddleware "django.contrib.auth.middleware.PersistentRemoteUserMiddleware") provides support for this use case. It will maintain the authenticated session until explicit logout by the user. The class can be used as a drop-in replacement of [`RemoteUserMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.auth.middleware.RemoteUserMiddleware "django.contrib.auth.middleware.RemoteUserMiddleware") in the documentation above.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/howto/)
[How to use Django’s CSRF protection ](https://docs.djangoproject.com/en/5.0/howto/csrf/)
[](https://docs.djangoproject.com/en/5.0/howto/auth-remote-user/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Bors LTD donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to authenticate using `REMOTE_USER`](https://docs.djangoproject.com/en/5.0/howto/auth-remote-user/)
    * [Configuration](https://docs.djangoproject.com/en/5.0/howto/auth-remote-user/#configuration)
    * [Using `REMOTE_USER` on login pages only](https://docs.djangoproject.com/en/5.0/howto/auth-remote-user/#using-remote-user-on-login-pages-only)


### Browse
  * Prev: [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
  * Next: [How to use Django’s CSRF protection](https://docs.djangoproject.com/en/5.0/howto/csrf/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to authenticate using `REMOTE_USER`


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
