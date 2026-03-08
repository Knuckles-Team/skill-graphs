This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/middleware/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/middleware/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/middleware/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/middleware/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/middleware/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/middleware/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/middleware/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/middleware/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/middleware/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/middleware/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/middleware/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/middleware/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/middleware/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/middleware/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/middleware/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/middleware/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/middleware/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/middleware/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/middleware/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/middleware/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/middleware/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/middleware/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/middleware/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/middleware/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/middleware/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/middleware/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/middleware/)


  * [](https://docs.djangoproject.com/en/5.0/ref/middleware/#top)


# Middleware[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.middleware "Link to this heading")
This document explains all middleware components that come with Django. For information on how to use them and how to write your own middleware, see the [middleware usage guide](https://docs.djangoproject.com/en/5.0/topics/http/middleware/).
## Available middleware[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#available-middleware "Link to this heading")
### Cache middleware[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.middleware.cache "Link to this heading")

_class_ UpdateCacheMiddleware[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/middleware/cache/#UpdateCacheMiddleware)[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.cache.UpdateCacheMiddleware "Link to this definition")


_class_ FetchFromCacheMiddleware[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/middleware/cache/#FetchFromCacheMiddleware)[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.cache.FetchFromCacheMiddleware "Link to this definition")

Enable the site-wide cache. If these are enabled, each Django-powered page will be cached for as long as the [`CACHE_MIDDLEWARE_SECONDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHE_MIDDLEWARE_SECONDS) setting defines. See the [cache documentation](https://docs.djangoproject.com/en/5.0/topics/cache/).
### “Common” middleware[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.middleware.common "Link to this heading")

_class_ CommonMiddleware[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/middleware/common/#CommonMiddleware)[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.common.CommonMiddleware "Link to this definition")

Adds a few conveniences for perfectionists:
  * Forbids access to user agents in the [`DISALLOWED_USER_AGENTS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DISALLOWED_USER_AGENTS) setting, which should be a list of compiled regular expression objects.
  * Performs URL rewriting based on the [`APPEND_SLASH`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-APPEND_SLASH) and [`PREPEND_WWW`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-PREPEND_WWW) settings.
If [`APPEND_SLASH`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-APPEND_SLASH) is `True` and the initial URL doesn’t end with a slash, and it is not found in the URLconf, then a new URL is formed by appending a slash at the end. If this new URL is found in the URLconf, then Django redirects the request to this new URL. Otherwise, the initial URL is processed as usual.
For example, `foo.com/bar` will be redirected to `foo.com/bar/` if you don’t have a valid URL pattern for `foo.com/bar` but _do_ have a valid pattern for `foo.com/bar/`.
If [`PREPEND_WWW`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-PREPEND_WWW) is `True`, URLs that lack a leading “www.” will be redirected to the same URL with a leading “www.”
Both of these options are meant to normalize URLs. The philosophy is that each URL should exist in one, and only one, place. Technically a URL `foo.com/bar` is distinct from `foo.com/bar/` – a search-engine indexer would treat them as separate URLs – so it’s best practice to normalize URLs.
If necessary, individual views may be excluded from the `APPEND_SLASH` behavior using the [`no_append_slash()`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.common.no_append_slash "django.views.decorators.common.no_append_slash") decorator:
```
from django.views.decorators.common import no_append_slash


@no_append_slash
def sensitive_fbv(request, *args, **kwargs):
    """View to be excluded from APPEND_SLASH."""
    return HttpResponse()

```

  * Sets the `Content-Length` header for non-streaming responses.



CommonMiddleware.response_redirect_class[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.common.CommonMiddleware.response_redirect_class "Link to this definition")

Defaults to [`HttpResponsePermanentRedirect`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponsePermanentRedirect "django.http.HttpResponsePermanentRedirect"). Subclass `CommonMiddleware` and override the attribute to customize the redirects issued by the middleware.

_class_ BrokenLinkEmailsMiddleware[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/middleware/common/#BrokenLinkEmailsMiddleware)[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.common.BrokenLinkEmailsMiddleware "Link to this definition")

  * Sends broken link notification emails to [`MANAGERS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MANAGERS) (see [How to manage error reporting](https://docs.djangoproject.com/en/5.0/howto/error-reporting/)).


### GZip middleware[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.middleware.gzip "Link to this heading")

_class_ GZipMiddleware[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/middleware/gzip/#GZipMiddleware)[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.gzip.GZipMiddleware "Link to this definition")


max_random_bytes[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.gzip.GZipMiddleware.max_random_bytes "Link to this definition")

Defaults to 100. Subclass `GZipMiddleware` and override the attribute to change the maximum number of random bytes that is included with compressed responses.
Note
Security researchers revealed that when compression techniques (including `GZipMiddleware`) are used on a website, the site may become exposed to a number of possible attacks.
To mitigate attacks, Django implements a technique called _Heal The Breach (HTB)_. It adds up to 100 bytes (see [`max_random_bytes`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.gzip.GZipMiddleware.max_random_bytes "django.middleware.gzip.GZipMiddleware.max_random_bytes")) of random bytes to each response to make the attacks less effective.
For more details, see the
Changed in Django 4.2:
Mitigation for the BREACH attack was added.
The `django.middleware.gzip.GZipMiddleware` compresses content for browsers that understand GZip compression (all modern browsers).
This middleware should be placed before any other middleware that need to read or write the response body so that compression happens afterward.
It will NOT compress content if any of the following are true:
  * The content body is less than 200 bytes long.
  * The response has already set the `Content-Encoding` header.
  * The request (the browser) hasn’t sent an `Accept-Encoding` header containing `gzip`.


If the response has an `ETag` header, the ETag is made weak to comply with
You can apply GZip compression to individual views using the [`gzip_page()`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.gzip.gzip_page "django.views.decorators.gzip.gzip_page") decorator.
### Conditional GET middleware[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.middleware.http "Link to this heading")

_class_ ConditionalGetMiddleware[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/middleware/http/#ConditionalGetMiddleware)[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.http.ConditionalGetMiddleware "Link to this definition")

Handles conditional GET operations. If the response doesn’t have an `ETag` header, the middleware adds one if needed. If the response has an `ETag` or `Last-Modified` header, and the request has `If-None-Match` or `If-Modified-Since`, the response is replaced by an [`HttpResponseNotModified`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseNotModified "django.http.HttpResponseNotModified").
### Locale middleware[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.middleware.locale "Link to this heading")

_class_ LocaleMiddleware[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/middleware/locale/#LocaleMiddleware)[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.locale.LocaleMiddleware "Link to this definition")

Enables language selection based on data from the request. It customizes content for each user. See the [internationalization documentation](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/).

LocaleMiddleware.response_redirect_class[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.locale.LocaleMiddleware.response_redirect_class "Link to this definition")

Defaults to [`HttpResponseRedirect`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseRedirect "django.http.HttpResponseRedirect"). Subclass `LocaleMiddleware` and override the attribute to customize the redirects issued by the middleware.
### Message middleware[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.contrib.messages.middleware "Link to this heading")

_class_ MessageMiddleware[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/contrib/messages/middleware/#MessageMiddleware)[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.messages.middleware.MessageMiddleware "Link to this definition")

Enables cookie- and session-based message support. See the [messages documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/).
### Security middleware[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.middleware.security "Link to this heading")
Warning
If your deployment situation allows, it’s usually a good idea to have your front-end web server perform the functionality provided by the `SecurityMiddleware`. That way, if there are requests that aren’t served by Django (such as static media or user-uploaded files), they will have the same protections as requests to your Django application.

_class_ SecurityMiddleware[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/middleware/security/#SecurityMiddleware)[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.security.SecurityMiddleware "Link to this definition")

The `django.middleware.security.SecurityMiddleware` provides several security enhancements to the request/response cycle. Each one can be independently enabled or disabled with a setting.
  * [`SECURE_CONTENT_TYPE_NOSNIFF`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_CONTENT_TYPE_NOSNIFF)
  * [`SECURE_CROSS_ORIGIN_OPENER_POLICY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_CROSS_ORIGIN_OPENER_POLICY)
  * [`SECURE_HSTS_INCLUDE_SUBDOMAINS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_INCLUDE_SUBDOMAINS)
  * [`SECURE_HSTS_PRELOAD`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_PRELOAD)
  * [`SECURE_HSTS_SECONDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_SECONDS)
  * [`SECURE_REDIRECT_EXEMPT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_REDIRECT_EXEMPT)
  * [`SECURE_REFERRER_POLICY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_REFERRER_POLICY)
  * [`SECURE_SSL_HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_SSL_HOST)
  * [`SECURE_SSL_REDIRECT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_SSL_REDIRECT)


#### HTTP Strict Transport Security[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#http-strict-transport-security "Link to this heading")
For sites that should only be accessed over HTTPS, you can instruct modern browsers to refuse to connect to your domain name via an insecure connection (for a given period of time) by setting the
`SecurityMiddleware` will set this header for you on all HTTPS responses if you set the [`SECURE_HSTS_SECONDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_SECONDS) setting to a non-zero integer value.
When enabling HSTS, it’s a good idea to first use a small value for testing, for example, [`SECURE_HSTS_SECONDS = 3600`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_SECONDS) for one hour. Each time a web browser sees the HSTS header from your site, it will refuse to communicate non-securely (using HTTP) with your domain for the given period of time. Once you confirm that all assets are served securely on your site (i.e. HSTS didn’t break anything), it’s a good idea to increase this value so that infrequent visitors will be protected (31536000 seconds, i.e. 1 year, is common).
Additionally, if you set the [`SECURE_HSTS_INCLUDE_SUBDOMAINS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_INCLUDE_SUBDOMAINS) setting to `True`, `SecurityMiddleware` will add the `includeSubDomains` directive to the `Strict-Transport-Security` header. This is recommended (assuming all subdomains are served exclusively using HTTPS), otherwise your site may still be vulnerable via an insecure connection to a subdomain.
If you wish to submit your site to the [`SECURE_HSTS_PRELOAD`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_PRELOAD) setting to `True`. That appends the `preload` directive to the `Strict-Transport-Security` header.
Warning
The HSTS policy applies to your entire domain, not just the URL of the response that you set the header on. Therefore, you should only use it if your entire domain is served via HTTPS only.
Browsers properly respecting the HSTS header will refuse to allow users to bypass warnings and connect to a site with an expired, self-signed, or otherwise invalid SSL certificate. If you use HSTS, make sure your certificates are in good shape and stay that way!
Note
If you are deployed behind a load-balancer or reverse-proxy server, and the `Strict-Transport-Security` header is not being added to your responses, it may be because Django doesn’t realize that it’s on a secure connection; you may need to set the [`SECURE_PROXY_SSL_HEADER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_PROXY_SSL_HEADER) setting.
#### Referrer Policy[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#referrer-policy "Link to this heading")
Browsers use
Some browsers have the ability to accept hints about whether they should send the HTTP `Referer` header when a user clicks a link; this hint is provided via
  * Full URL: send the entire URL in the `Referer` header. For example, if the user is visiting `https://example.com/page.html`, the `Referer` header would contain `"https://example.com/page.html"`.
  * Origin only: send only the “origin” in the referrer. The origin consists of the scheme, host and (optionally) port number. For example, if the user is visiting `https://example.com/page.html`, the origin would be `https://example.com/`.
  * No referrer: do not send a `Referer` header at all.


There are two types of conditions this header can tell a browser to watch out for:
  * Same-origin versus cross-origin: a link from `https://example.com/1.html` to `https://example.com/2.html` is same-origin. A link from `https://example.com/page.html` to `https://not.example.com/page.html` is cross-origin.
  * Protocol downgrade: a downgrade occurs if the page containing the link is served via HTTPS, but the page being linked to is not served via HTTPS.


Warning
When your site is served via HTTPS, [Django’s CSRF protection system](https://docs.djangoproject.com/en/5.0/ref/csrf/#how-csrf-works) requires the `Referer` header to be present, so completely disabling the `Referer` header will interfere with CSRF protection. To gain most of the benefits of disabling `Referer` headers while also keeping CSRF protection, consider enabling only same-origin referrers.
`SecurityMiddleware` can set the `Referrer-Policy` header for you, based on the [`SECURE_REFERRER_POLICY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_REFERRER_POLICY) setting (note spelling: browsers send a `Referer` header when a user clicks a link, but the header instructing a browser whether to do so is spelled `Referrer-Policy`). The valid values for this setting are:

`no-referrer`

Instructs the browser to send no referrer for links clicked on this site.

`no-referrer-when-downgrade`

Instructs the browser to send a full URL as the referrer, but only when no protocol downgrade occurs.

`origin`

Instructs the browser to send only the origin, not the full URL, as the referrer.

`origin-when-cross-origin`

Instructs the browser to send the full URL as the referrer for same-origin links, and only the origin for cross-origin links.

`same-origin`

Instructs the browser to send a full URL, but only for same-origin links. No referrer will be sent for cross-origin links.

`strict-origin`

Instructs the browser to send only the origin, not the full URL, and to send no referrer when a protocol downgrade occurs.

`strict-origin-when-cross-origin`

Instructs the browser to send the full URL when the link is same-origin and no protocol downgrade occurs; send only the origin when the link is cross-origin and no protocol downgrade occurs; and no referrer when a protocol downgrade occurs.

`unsafe-url`

Instructs the browser to always send the full URL as the referrer.
Unknown Policy Values
Where a policy value is [`SECURE_REFERRER_POLICY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_REFERRER_POLICY).
#### Cross-Origin Opener Policy[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#cross-origin-opener-policy "Link to this heading")
Some browsers have the ability to isolate top-level windows from other documents by putting them in a separate browsing context group based on the value of the `window.opener` property will be `null`. Isolating windows using COOP is a defense-in-depth protection against cross-origin attacks, especially those like Spectre which allowed exfiltration of data loaded into a shared browsing context.
`SecurityMiddleware` can set the `Cross-Origin-Opener-Policy` header for you, based on the [`SECURE_CROSS_ORIGIN_OPENER_POLICY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_CROSS_ORIGIN_OPENER_POLICY) setting. The valid values for this setting are:

`same-origin`

Isolates the browsing context exclusively to same-origin documents. Cross-origin documents are not loaded in the same browsing context. This is the default and most secure option.

`same-origin-allow-popups`

Isolates the browsing context to same-origin documents or those which either don’t set COOP or which opt out of isolation by setting a COOP of `unsafe-none`.

`unsafe-none`

Allows the document to be added to its opener’s browsing context group unless the opener itself has a COOP of `same-origin` or `same-origin-allow-popups`.
####  `X-Content-Type-Options: nosniff`[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#x-content-type-options-nosniff "Link to this heading")
Some browsers will try to guess the content types of the assets that they fetch, overriding the `Content-Type` header. While this can help display sites with improperly configured servers, it can also pose a security risk.
If your site serves user-uploaded files, a malicious user could upload a specially-crafted file that would be interpreted as HTML or JavaScript by the browser when you expected it to be something harmless.
To prevent the browser from guessing the content type and force it to always use the type provided in the `Content-Type` header, you can pass the `SecurityMiddleware` will do this for all responses if the [`SECURE_CONTENT_TYPE_NOSNIFF`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_CONTENT_TYPE_NOSNIFF) setting is `True`.
Note that in most deployment situations where Django isn’t involved in serving user-uploaded files, this setting won’t help you. For example, if your [`MEDIA_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_URL) is served directly by your front-end web server (nginx, Apache, etc.) then you’d want to set this header there. On the other hand, if you are using Django to do something like require authorization in order to download files and you cannot set the header using your web server, this setting will be useful.
#### SSL Redirect[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#ssl-redirect "Link to this heading")
If your site offers both HTTP and HTTPS connections, most users will end up with an unsecured connection by default. For best security, you should redirect all HTTP connections to HTTPS.
If you set the [`SECURE_SSL_REDIRECT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_SSL_REDIRECT) setting to True, `SecurityMiddleware` will permanently (HTTP 301) redirect all HTTP connections to HTTPS.
Note
For performance reasons, it’s preferable to do these redirects outside of Django, in a front-end load balancer or reverse-proxy server such as [`SECURE_SSL_REDIRECT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_SSL_REDIRECT) is intended for the deployment situations where this isn’t an option.
If the [`SECURE_SSL_HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_SSL_HOST) setting has a value, all redirects will be sent to that host instead of the originally-requested host.
If there are a few pages on your site that should be available over HTTP, and not redirected to HTTPS, you can list regular expressions to match those URLs in the [`SECURE_REDIRECT_EXEMPT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_REDIRECT_EXEMPT) setting.
Note
If you are deployed behind a load-balancer or reverse-proxy server and Django can’t seem to tell when a request actually is already secure, you may need to set the [`SECURE_PROXY_SSL_HEADER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_PROXY_SSL_HEADER) setting.
### Session middleware[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.contrib.sessions.middleware "Link to this heading")

_class_ SessionMiddleware[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/contrib/sessions/middleware/#SessionMiddleware)[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.sessions.middleware.SessionMiddleware "Link to this definition")

Enables session support. See the [session documentation](https://docs.djangoproject.com/en/5.0/topics/http/sessions/).
### Site middleware[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.contrib.sites.middleware "Link to this heading")

_class_ CurrentSiteMiddleware[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/contrib/sites/middleware/#CurrentSiteMiddleware)[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.sites.middleware.CurrentSiteMiddleware "Link to this definition")

Adds the `site` attribute representing the current site to every incoming `HttpRequest` object. See the [sites documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/sites/#site-middleware).
### Authentication middleware[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.contrib.auth.middleware "Link to this heading")

_class_ AuthenticationMiddleware[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/contrib/auth/middleware/#AuthenticationMiddleware)[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.auth.middleware.AuthenticationMiddleware "Link to this definition")

Adds the `user` attribute, representing the currently-logged-in user, to every incoming `HttpRequest` object. See [Authentication in web requests](https://docs.djangoproject.com/en/5.0/topics/auth/default/#auth-web-requests).

_class_ RemoteUserMiddleware[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/contrib/auth/middleware/#RemoteUserMiddleware)[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.auth.middleware.RemoteUserMiddleware "Link to this definition")

Middleware for utilizing web server provided authentication. See [How to authenticate using REMOTE_USER](https://docs.djangoproject.com/en/5.0/howto/auth-remote-user/) for usage details.

_class_ PersistentRemoteUserMiddleware[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/contrib/auth/middleware/#PersistentRemoteUserMiddleware)[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.auth.middleware.PersistentRemoteUserMiddleware "Link to this definition")

Middleware for utilizing web server provided authentication when enabled only on the login page. See [Using REMOTE_USER on login pages only](https://docs.djangoproject.com/en/5.0/howto/auth-remote-user/#persistent-remote-user-middleware-howto) for usage details.
### CSRF protection middleware[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#csrf-protection-middleware "Link to this heading")

_class_ CsrfViewMiddleware[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/middleware/csrf/#CsrfViewMiddleware)[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.csrf.CsrfViewMiddleware "Link to this definition")

Adds protection against Cross Site Request Forgeries by adding hidden form fields to POST forms and checking requests for the correct value. See the [Cross Site Request Forgery protection documentation](https://docs.djangoproject.com/en/5.0/ref/csrf/).
###  `X-Frame-Options` middleware[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#x-frame-options-middleware "Link to this heading")

_class_ XFrameOptionsMiddleware[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/middleware/clickjacking/#XFrameOptionsMiddleware)[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.clickjacking.XFrameOptionsMiddleware "Link to this definition")

Simple [clickjacking protection via the X-Frame-Options header](https://docs.djangoproject.com/en/5.0/ref/clickjacking/).
## Middleware ordering[¶](https://docs.djangoproject.com/en/5.0/ref/middleware/#middleware-ordering "Link to this heading")
Here are some hints about the ordering of various Django middleware classes:
  1. [`SecurityMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware")
It should go near the top of the list if you’re going to turn on the SSL redirect as that avoids running through a bunch of other unnecessary middleware.
  2. [`UpdateCacheMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.cache.UpdateCacheMiddleware "django.middleware.cache.UpdateCacheMiddleware")
Before those that modify the `Vary` header (`SessionMiddleware`, `GZipMiddleware`, `LocaleMiddleware`).
  3. [`GZipMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.gzip.GZipMiddleware "django.middleware.gzip.GZipMiddleware")
Before any middleware that may change or use the response body.
After `UpdateCacheMiddleware`: Modifies `Vary` header.
  4. [`SessionMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.sessions.middleware.SessionMiddleware "django.contrib.sessions.middleware.SessionMiddleware")
Before any middleware that may raise an exception to trigger an error view (such as [`PermissionDenied`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.PermissionDenied "django.core.exceptions.PermissionDenied")) if you’re using [`CSRF_USE_SESSIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_USE_SESSIONS).
After `UpdateCacheMiddleware`: Modifies `Vary` header.
  5. [`ConditionalGetMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.http.ConditionalGetMiddleware "django.middleware.http.ConditionalGetMiddleware")
Before any middleware that may change the response (it sets the `ETag` header).
After `GZipMiddleware` so it won’t calculate an `ETag` header on gzipped contents.
  6. [`LocaleMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.locale.LocaleMiddleware "django.middleware.locale.LocaleMiddleware")
One of the topmost, after `SessionMiddleware` (uses session data) and `UpdateCacheMiddleware` (modifies `Vary` header).
  7. [`CommonMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.common.CommonMiddleware "django.middleware.common.CommonMiddleware")
Before any middleware that may change the response (it sets the `Content-Length` header). A middleware that appears before `CommonMiddleware` and changes the response must reset `Content-Length`.
Close to the top: it redirects when [`APPEND_SLASH`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-APPEND_SLASH) or [`PREPEND_WWW`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-PREPEND_WWW) are set to `True`.
After `SessionMiddleware` if you’re using [`CSRF_USE_SESSIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_USE_SESSIONS).
  8. [`CsrfViewMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.csrf.CsrfViewMiddleware "django.middleware.csrf.CsrfViewMiddleware")
Before any view middleware that assumes that CSRF attacks have been dealt with.
Before [`RemoteUserMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.auth.middleware.RemoteUserMiddleware "django.contrib.auth.middleware.RemoteUserMiddleware"), or any other authentication middleware that may perform a login, and hence rotate the CSRF token, before calling down the middleware chain.
After `SessionMiddleware` if you’re using [`CSRF_USE_SESSIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_USE_SESSIONS).
  9. [`AuthenticationMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.auth.middleware.AuthenticationMiddleware "django.contrib.auth.middleware.AuthenticationMiddleware")
After `SessionMiddleware`: uses session storage.
  10. [`MessageMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.messages.middleware.MessageMiddleware "django.contrib.messages.middleware.MessageMiddleware")
After `SessionMiddleware`: can use session-based storage.
  11. [`FetchFromCacheMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.cache.FetchFromCacheMiddleware "django.middleware.cache.FetchFromCacheMiddleware")
After any middleware that modifies the `Vary` header: that header is used to pick a value for the cache hash-key.
  12. [`FlatpageFallbackMiddleware`](https://docs.djangoproject.com/en/5.0/ref/contrib/flatpages/#django.contrib.flatpages.middleware.FlatpageFallbackMiddleware "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware")
Should be near the bottom as it’s a last-resort type of middleware.
  13. [`RedirectFallbackMiddleware`](https://docs.djangoproject.com/en/5.0/ref/contrib/redirects/#django.contrib.redirects.middleware.RedirectFallbackMiddleware "django.contrib.redirects.middleware.RedirectFallbackMiddleware")
Should be near the bottom as it’s a last-resort type of middleware.

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/logging/)
[Migration Operations ](https://docs.djangoproject.com/en/5.0/ref/migration-operations/)
[](https://docs.djangoproject.com/en/5.0/ref/middleware/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Columbia Personal Injury Lawyer donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/)
    * [Available middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/#available-middleware)
      * [Cache middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.middleware.cache)
      * [“Common” middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.middleware.common)
      * [GZip middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.middleware.gzip)
      * [Conditional GET middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.middleware.http)
      * [Locale middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.middleware.locale)
      * [Message middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.contrib.messages.middleware)
      * [Security middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.middleware.security)
        * [HTTP Strict Transport Security](https://docs.djangoproject.com/en/5.0/ref/middleware/#http-strict-transport-security)
        * [Referrer Policy](https://docs.djangoproject.com/en/5.0/ref/middleware/#referrer-policy)
        * [Cross-Origin Opener Policy](https://docs.djangoproject.com/en/5.0/ref/middleware/#cross-origin-opener-policy)
        * [`X-Content-Type-Options: nosniff`](https://docs.djangoproject.com/en/5.0/ref/middleware/#x-content-type-options-nosniff)
        * [SSL Redirect](https://docs.djangoproject.com/en/5.0/ref/middleware/#ssl-redirect)
      * [Session middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.contrib.sessions.middleware)
      * [Site middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.contrib.sites.middleware)
      * [Authentication middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.contrib.auth.middleware)
      * [CSRF protection middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/#csrf-protection-middleware)
      * [`X-Frame-Options` middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/#x-frame-options-middleware)
    * [Middleware ordering](https://docs.djangoproject.com/en/5.0/ref/middleware/#middleware-ordering)


### Browse
  * Prev: [Logging](https://docs.djangoproject.com/en/5.0/ref/logging/)
  * Next: [Migration Operations](https://docs.djangoproject.com/en/5.0/ref/migration-operations/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * Middleware


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
