This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/security/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/security/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/security/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/security/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/security/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/security/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/security/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/security/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/security/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/security/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/security/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/security/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/security/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/security/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/security/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/security/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/security/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/security/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/security/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/security/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/security/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/security/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/security/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/security/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/security/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/security/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/security/)


  * [](https://docs.djangoproject.com/en/5.0/topics/security/#top)


# Security in Django[¶](https://docs.djangoproject.com/en/5.0/topics/security/#security-in-django "Link to this heading")
This document is an overview of Django’s security features. It includes advice on securing a Django-powered site.
## Cross site scripting (XSS) protection[¶](https://docs.djangoproject.com/en/5.0/topics/security/#cross-site-scripting-xss-protection "Link to this heading")
XSS attacks allow a user to inject client side scripts into the browsers of other users. This is usually achieved by storing the malicious scripts in the database where it will be retrieved and displayed to other users, or by getting users to click a link which will cause the attacker’s JavaScript to be executed by the user’s browser. However, XSS attacks can originate from any untrusted source of data, such as cookies or web services, whenever the data is not sufficiently sanitized before including in a page.
Using Django templates protects you against the majority of XSS attacks. However, it is important to understand what protections it provides and its limitations.
Django templates [escape specific characters](https://docs.djangoproject.com/en/5.0/ref/templates/language/#automatic-html-escaping) which are particularly dangerous to HTML. While this protects users from most malicious input, it is not entirely foolproof. For example, it will not protect the following:
```
<style class={{ var }}>...</style>

```

If `var` is set to `'class1 onmouseover=javascript:func()'`, this can result in unauthorized JavaScript execution, depending on how the browser renders imperfect HTML. (Quoting the attribute value would fix this case.)
It is also important to be particularly careful when using `is_safe` with custom template tags, the [`safe`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatefilter-safe) template tag, [`mark_safe`](https://docs.djangoproject.com/en/5.0/ref/utils/#module-django.utils.safestring "django.utils.safestring: Functions and classes for working with strings that can be displayed safely without further escaping in HTML."), and when autoescape is turned off.
In addition, if you are using the template system to output something other than HTML, there may be entirely separate characters and words which require escaping.
You should also be very careful when storing HTML in the database, especially when that HTML is retrieved and displayed.
## Cross site request forgery (CSRF) protection[¶](https://docs.djangoproject.com/en/5.0/topics/security/#cross-site-request-forgery-csrf-protection "Link to this heading")
CSRF attacks allow a malicious user to execute actions using the credentials of another user without that user’s knowledge or consent.
Django has built-in protection against most types of CSRF attacks, providing you have [enabled and used it](https://docs.djangoproject.com/en/5.0/howto/csrf/#using-csrf) where appropriate. However, as with any mitigation technique, there are limitations. For example, it is possible to disable the CSRF module globally or for particular views. You should only do this if you know what you are doing. There are other [limitations](https://docs.djangoproject.com/en/5.0/ref/csrf/#csrf-limitations) if your site has subdomains that are outside of your control.
[CSRF protection works](https://docs.djangoproject.com/en/5.0/ref/csrf/#how-csrf-works) by checking for a secret in each POST request. This ensures that a malicious user cannot “replay” a form POST to your website and have another logged in user unwittingly submit that form. The malicious user would have to know the secret, which is user specific (using a cookie).
When deployed with [HTTPS](https://docs.djangoproject.com/en/5.0/topics/security/#security-recommendation-ssl), `CsrfViewMiddleware` will check that the HTTP referer header is set to a URL on the same origin (including subdomain and port). Because HTTPS provides additional security, it is imperative to ensure connections use HTTPS where it is available by forwarding insecure connection requests and using HSTS for supported browsers.
Be very careful with marking views with the `csrf_exempt` decorator unless it is absolutely necessary.
## SQL injection protection[¶](https://docs.djangoproject.com/en/5.0/topics/security/#sql-injection-protection "Link to this heading")
SQL injection is a type of attack where a malicious user is able to execute arbitrary SQL code on a database. This can result in records being deleted or data leakage.
Django’s querysets are protected from SQL injection since their queries are constructed using query parameterization. A query’s SQL code is defined separately from the query’s parameters. Since parameters may be user-provided and therefore unsafe, they are escaped by the underlying database driver.
Django also gives developers power to write [raw queries](https://docs.djangoproject.com/en/5.0/topics/db/sql/#executing-raw-queries) or execute [custom sql](https://docs.djangoproject.com/en/5.0/topics/db/sql/#executing-custom-sql). These capabilities should be used sparingly and you should always be careful to properly escape any parameters that the user can control. In addition, you should exercise caution when using [`extra()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.extra "django.db.models.query.QuerySet.extra") and [`RawSQL`](https://docs.djangoproject.com/en/5.0/ref/models/expressions/#django.db.models.expressions.RawSQL "django.db.models.expressions.RawSQL").
## Clickjacking protection[¶](https://docs.djangoproject.com/en/5.0/topics/security/#clickjacking-protection "Link to this heading")
Clickjacking is a type of attack where a malicious site wraps another site in a frame. This attack can result in an unsuspecting user being tricked into performing unintended actions on the target site.
Django contains [clickjacking protection](https://docs.djangoproject.com/en/5.0/ref/clickjacking/#clickjacking-prevention) in the form of the [`X-Frame-Options middleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.clickjacking.XFrameOptionsMiddleware "django.middleware.clickjacking.XFrameOptionsMiddleware") which in a supporting browser can prevent a site from being rendered inside a frame. It is possible to disable the protection on a per view basis or to configure the exact header value sent.
The middleware is strongly recommended for any site that does not need to have its pages wrapped in a frame by third party sites, or only needs to allow that for a small section of the site.
## SSL/HTTPS[¶](https://docs.djangoproject.com/en/5.0/topics/security/#ssl-https "Link to this heading")
It is always better for security to deploy your site behind HTTPS. Without this, it is possible for malicious network users to sniff authentication credentials or any other information transferred between client and server, and in some cases – **active** network attackers – to alter data that is sent in either direction.
If you want the protection that HTTPS provides, and have enabled it on your server, there are some additional steps you may need:
  * If necessary, set [`SECURE_PROXY_SSL_HEADER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_PROXY_SSL_HEADER), ensuring that you have understood the warnings there thoroughly. Failure to do this can result in CSRF vulnerabilities, and failure to do it correctly can also be dangerous!
  * Set [`SECURE_SSL_REDIRECT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_SSL_REDIRECT) to `True`, so that requests over HTTP are redirected to HTTPS.
Please note the caveats under [`SECURE_PROXY_SSL_HEADER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_PROXY_SSL_HEADER). For the case of a reverse proxy, it may be easier or more secure to configure the main web server to do the redirect to HTTPS.
  * Use ‘secure’ cookies.
If a browser connects initially via HTTP, which is the default for most browsers, it is possible for existing cookies to be leaked. For this reason, you should set your [`SESSION_COOKIE_SECURE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_SECURE) and [`CSRF_COOKIE_SECURE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CSRF_COOKIE_SECURE) settings to `True`. This instructs the browser to only send these cookies over HTTPS connections. Note that this will mean that sessions will not work over HTTP, and the CSRF protection will prevent any POST data being accepted over HTTP (which will be fine if you are redirecting all HTTP traffic to HTTPS).
  * Use [HTTP Strict Transport Security](https://docs.djangoproject.com/en/5.0/ref/middleware/#http-strict-transport-security) (HSTS)
HSTS is an HTTP header that informs a browser that all future connections to a particular site should always use HTTPS. Combined with redirecting requests over HTTP to HTTPS, this will ensure that connections always enjoy the added security of SSL provided one successful connection has occurred. HSTS may either be configured with [`SECURE_HSTS_SECONDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_SECONDS), [`SECURE_HSTS_INCLUDE_SUBDOMAINS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_INCLUDE_SUBDOMAINS), and [`SECURE_HSTS_PRELOAD`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_PRELOAD), or on the web server.


## Host header validation[¶](https://docs.djangoproject.com/en/5.0/topics/security/#host-header-validation "Link to this heading")
Django uses the `Host` header provided by the client to construct URLs in certain cases. While these values are sanitized to prevent Cross Site Scripting attacks, a fake `Host` value can be used for Cross-Site Request Forgery, cache poisoning attacks, and poisoning links in emails.
Because even seemingly-secure web server configurations are susceptible to fake `Host` headers, Django validates `Host` headers against the [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ALLOWED_HOSTS) setting in the [`django.http.HttpRequest.get_host()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.get_host "django.http.HttpRequest.get_host") method.
This validation only applies via [`get_host()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.get_host "django.http.HttpRequest.get_host"); if your code accesses the `Host` header directly from `request.META` you are bypassing this security protection.
For more details see the full [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ALLOWED_HOSTS) documentation.
Warning
Previous versions of this document recommended configuring your web server to ensure it validates incoming HTTP `Host` headers. While this is still recommended, in many common web servers a configuration that seems to validate the `Host` header may not in fact do so. For instance, even if Apache is configured such that your Django site is served from a non-default virtual host with the `ServerName` set, it is still possible for an HTTP request to match this virtual host and supply a fake `Host` header. Thus, Django now requires that you set [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ALLOWED_HOSTS) explicitly rather than relying on web server configuration.
Additionally, Django requires you to explicitly enable support for the `X-Forwarded-Host` header (via the [`USE_X_FORWARDED_HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_X_FORWARDED_HOST) setting) if your configuration requires it.
## Referrer policy[¶](https://docs.djangoproject.com/en/5.0/topics/security/#referrer-policy "Link to this heading")
Browsers use the `Referer` header as a way to send information to a site about how users got there. By setting a _Referrer Policy_ you can help to protect the privacy of your users, restricting under which circumstances the `Referer` header is set. See [the referrer policy section of the security middleware reference](https://docs.djangoproject.com/en/5.0/ref/middleware/#referrer-policy) for details.
## Cross-origin opener policy[¶](https://docs.djangoproject.com/en/5.0/topics/security/#cross-origin-opener-policy "Link to this heading")
The cross-origin opener policy (COOP) header allows browsers to isolate a top-level window from other documents by putting them in a different context group so that they cannot directly interact with the top-level window. If a document protected by COOP opens a cross-origin popup window, the popup’s `window.opener` property will be `null`. COOP protects against cross-origin attacks. See [the cross-origin opener policy section of the security middleware reference](https://docs.djangoproject.com/en/5.0/ref/middleware/#cross-origin-opener-policy) for details.
## Session security[¶](https://docs.djangoproject.com/en/5.0/topics/security/#session-security "Link to this heading")
Similar to the [CSRF limitations](https://docs.djangoproject.com/en/5.0/ref/csrf/#csrf-limitations) requiring a site to be deployed such that untrusted users don’t have access to any subdomains, [`django.contrib.sessions`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#module-django.contrib.sessions "django.contrib.sessions: Provides session management for Django projects.") also has limitations. See [the session topic guide section on security](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#topics-session-security) for details.
## User-uploaded content[¶](https://docs.djangoproject.com/en/5.0/topics/security/#user-uploaded-content "Link to this heading")
Note
Consider [serving static files from a cloud service or CDN](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/#staticfiles-from-cdn) to avoid some of these issues.
  * If your site accepts file uploads, it is strongly advised that you limit these uploads in your web server configuration to a reasonable size in order to prevent denial of service (DOS) attacks. In Apache, this can be easily set using the
  * If you are serving your own static files, be sure that handlers like Apache’s `mod_php`, which would execute static files as code, are disabled. You don’t want users to be able to execute arbitrary code by uploading and requesting a specially crafted file.
  * Django’s media upload handling poses some vulnerabilities when that media is served in ways that do not follow security best practices. Specifically, an HTML file can be uploaded as an image if that file contains a valid PNG header followed by malicious HTML. This file will pass verification of the library that Django uses for [`ImageField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ImageField "django.db.models.ImageField") image processing (Pillow). When this file is subsequently displayed to a user, it may be displayed as HTML depending on the type and configuration of your web server.
No bulletproof technical solution exists at the framework level to safely validate all user uploaded file content, however, there are some other steps you can take to mitigate these attacks:
    1. One class of attacks can be prevented by always serving user uploaded content from a distinct top-level or second-level domain. This prevents any exploit blocked by `example.com`, you would want to serve uploaded content (the [`MEDIA_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_URL) setting) from something like `usercontent-example.com`. It’s _not_ sufficient to serve content from a subdomain like `usercontent.example.com`.
    2. Beyond this, applications may choose to define a list of allowable file extensions for user uploaded files and configure the web server to only serve such files.


## Additional security topics[¶](https://docs.djangoproject.com/en/5.0/topics/security/#additional-security-topics "Link to this heading")
While Django provides good security protection out of the box, it is still important to properly deploy your application and take advantage of the security protection of the web server, operating system and other components.
  * Make sure that your Python code is outside of the web server’s root. This will ensure that your Python code is not accidentally served as plain text (or accidentally executed).
  * Take care with any [user uploaded files](https://docs.djangoproject.com/en/5.0/ref/models/fields/#file-upload-security).
  * Django does not throttle requests to authenticate users. To protect against brute-force attacks against the authentication system, you may consider deploying a Django plugin or web server module to throttle these requests.
  * Keep your [`SECRET_KEY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY), and [`SECRET_KEY_FALLBACKS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY_FALLBACKS) if in use, secret.
  * It is a good idea to limit the accessibility of your caching system and database using a firewall.
  * Take a look at the Open Web Application Security Project (OWASP)
  * Mozilla discusses various topics regarding

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/pagination/)
[Performance and optimization ](https://docs.djangoproject.com/en/5.0/topics/performance/)
[](https://docs.djangoproject.com/en/5.0/topics/security/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ 王文沛 donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Security in Django](https://docs.djangoproject.com/en/5.0/topics/security/)
    * [Cross site scripting (XSS) protection](https://docs.djangoproject.com/en/5.0/topics/security/#cross-site-scripting-xss-protection)
    * [Cross site request forgery (CSRF) protection](https://docs.djangoproject.com/en/5.0/topics/security/#cross-site-request-forgery-csrf-protection)
    * [SQL injection protection](https://docs.djangoproject.com/en/5.0/topics/security/#sql-injection-protection)
    * [Clickjacking protection](https://docs.djangoproject.com/en/5.0/topics/security/#clickjacking-protection)
    * [SSL/HTTPS](https://docs.djangoproject.com/en/5.0/topics/security/#ssl-https)
    * [Host header validation](https://docs.djangoproject.com/en/5.0/topics/security/#host-header-validation)
    * [Referrer policy](https://docs.djangoproject.com/en/5.0/topics/security/#referrer-policy)
    * [Cross-origin opener policy](https://docs.djangoproject.com/en/5.0/topics/security/#cross-origin-opener-policy)
    * [Session security](https://docs.djangoproject.com/en/5.0/topics/security/#session-security)
    * [User-uploaded content](https://docs.djangoproject.com/en/5.0/topics/security/#user-uploaded-content)
    * [Additional security topics](https://docs.djangoproject.com/en/5.0/topics/security/#additional-security-topics)


### Browse
  * Prev: [Pagination](https://docs.djangoproject.com/en/5.0/topics/pagination/)
  * Next: [Performance and optimization](https://docs.djangoproject.com/en/5.0/topics/performance/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * Security in Django


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
