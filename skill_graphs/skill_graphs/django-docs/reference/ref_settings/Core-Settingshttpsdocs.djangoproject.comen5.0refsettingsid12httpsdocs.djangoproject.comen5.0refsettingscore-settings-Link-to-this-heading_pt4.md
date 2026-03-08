See [`SESSION_COOKIE_HTTPONLY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_HTTPONLY) for details on `HttpOnly`.
###  `LANGUAGE_COOKIE_NAME`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#language-cookie-name "Link to this heading")
Default: `'django_language'`
The name of the cookie to use for the language cookie. This can be whatever you want (as long as it’s different from the other cookie names in your application). See [Internationalization and localization](https://docs.djangoproject.com/en/5.0/topics/i18n/).
###  `LANGUAGE_COOKIE_PATH`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#language-cookie-path "Link to this heading")
Default: `'/'`
The path set on the language cookie. This should either match the URL path of your Django installation or be a parent of that path.
This is useful if you have multiple Django instances running under the same hostname. They can use different cookie paths and each instance will only see its own language cookie.
Be cautious when updating this setting on a production site. If you update this setting to use a deeper path than it previously used, existing user cookies that have the old path will not be updated. This will result in site users being unable to switch the language as long as these cookies persist. The only safe and reliable option to perform the switch is to change the language cookie name permanently (via the [`LANGUAGE_COOKIE_NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LANGUAGE_COOKIE_NAME) setting), and to add a middleware that copies the value from the old cookie to a new one and then deletes the one.
###  `LANGUAGE_COOKIE_SAMESITE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#language-cookie-samesite "Link to this heading")
Default: `None`
The value of the
See [`SESSION_COOKIE_SAMESITE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SESSION_COOKIE_SAMESITE) for details about `SameSite`.
###  `LANGUAGE_COOKIE_SECURE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#language-cookie-secure "Link to this heading")
Default: `False`
Whether to use a secure cookie for the language cookie. If this is set to `True`, the cookie will be marked as “secure”, which means browsers may ensure that the cookie is only sent under an HTTPS connection.
###  `LANGUAGES`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#languages "Link to this heading")
Default: A list of all available languages. This list is continually growing and including a copy here would inevitably become rapidly out of date. You can see the current list of translated languages by looking in
The list is a list of 2-tuples in the format ([language code](https://docs.djangoproject.com/en/5.0/topics/i18n/#term-language-code), `language name`) – for example, `('ja', 'Japanese')`. This specifies which languages are available for language selection. See [Internationalization and localization](https://docs.djangoproject.com/en/5.0/topics/i18n/).
Generally, the default value should suffice. Only set this setting if you want to restrict language selection to a subset of the Django-provided languages.
If you define a custom [`LANGUAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LANGUAGES) setting, you can mark the language names as translation strings using the [`gettext_lazy()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.gettext_lazy "django.utils.translation.gettext_lazy") function.
Here’s a sample settings file:
```
from django.utils.translation import gettext_lazy as _

LANGUAGES = [
    ("de", _("German")),
    ("en", _("English")),
]

```

###  `LANGUAGES_BIDI`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#languages-bidi "Link to this heading")
Default: A list of all language codes that are written right-to-left. You can see the current list of these languages by looking in
The list contains [language codes](https://docs.djangoproject.com/en/5.0/topics/i18n/#term-language-code) for languages that are written right-to-left.
Generally, the default value should suffice. Only set this setting if you want to restrict language selection to a subset of the Django-provided languages. If you define a custom [`LANGUAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LANGUAGES) setting, the list of bidirectional languages may contain language codes which are not enabled on a given site.
###  `LOCALE_PATHS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#locale-paths "Link to this heading")
Default: `[]` (Empty list)
A list of directories where Django looks for translation files. See [How Django discovers translations](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/#how-django-discovers-translations).
Example:
```
LOCALE_PATHS = [
    "/home/www/project/common_files/locale",
    "/var/local/translations/locale",
]

```

Django will look within each of these paths for the `<locale_code>/LC_MESSAGES` directories containing the actual translation files.
###  `LOGGING`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#logging "Link to this heading")
Default: A logging configuration dictionary.
A data structure containing configuration information. When not-empty, the contents of this data structure will be passed as the argument to the configuration method described in [`LOGGING_CONFIG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LOGGING_CONFIG).
Among other things, the default logging configuration passes HTTP 500 server errors to an email log handler when [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is `False`. See also [Configuring logging](https://docs.djangoproject.com/en/5.0/topics/logging/#configuring-logging).
You can see the default logging configuration by looking in
###  `LOGGING_CONFIG`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#logging-config "Link to this heading")
Default: `'logging.config.dictConfig'`
A path to a callable that will be used to configure logging in the Django project. Points at an instance of Python’s
If you set [`LOGGING_CONFIG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LOGGING_CONFIG) to `None`, the logging configuration process will be skipped.
###  `MANAGERS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#managers "Link to this heading")
Default: `[]` (Empty list)
A list in the same format as [`ADMINS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ADMINS) that specifies who should get broken link notifications when [`BrokenLinkEmailsMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.common.BrokenLinkEmailsMiddleware "django.middleware.common.BrokenLinkEmailsMiddleware") is enabled.
###  `MEDIA_ROOT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#media-root "Link to this heading")
Default: `''` (Empty string)
Absolute filesystem path to the directory that will hold [user-uploaded files](https://docs.djangoproject.com/en/5.0/topics/files/).
Example: `"/var/www/example.com/media/"`
See also [`MEDIA_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_URL).
Warning
[`MEDIA_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_ROOT) and [`STATIC_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_ROOT) must have different values. Before [`STATIC_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_ROOT) was introduced, it was common to rely or fallback on [`MEDIA_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_ROOT) to also serve static files; however, since this can have serious security implications, there is a validation check to prevent it.
###  `MEDIA_URL`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#media-url "Link to this heading")
Default: `''` (Empty string)
URL that handles the media served from [`MEDIA_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_ROOT), used for [managing stored files](https://docs.djangoproject.com/en/5.0/topics/files/). It must end in a slash if set to a non-empty value. You will need to [configure these files to be served](https://docs.djangoproject.com/en/5.0/howto/static-files/#serving-uploaded-files-in-development) in both development and production environments.
If you want to use `{{ MEDIA_URL }}` in your templates, add `'django.template.context_processors.media'` in the `'context_processors'` option of [`TEMPLATES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES).
Example: `"http://media.example.com/"`
Warning
There are security risks if you are accepting uploaded content from untrusted users! See the security guide’s topic on [User-uploaded content](https://docs.djangoproject.com/en/5.0/topics/security/#user-uploaded-content-security) for mitigation details.
Warning
[`MEDIA_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_URL) and [`STATIC_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_URL) must have different values. See [`MEDIA_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_ROOT) for more details.
Note
If [`MEDIA_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_URL) is a relative path, then it will be prefixed by the server-provided value of `SCRIPT_NAME` (or `/` if not set). This makes it easier to serve a Django application in a subpath without adding an extra configuration to the settings.
###  `MIDDLEWARE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#middleware "Link to this heading")
Default: `None`
A list of middleware to use. See [Middleware](https://docs.djangoproject.com/en/5.0/topics/http/middleware/).
###  `MIGRATION_MODULES`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#migration-modules "Link to this heading")
Default: `{}` (Empty dictionary)
A dictionary specifying the package where migration modules can be found on a per-app basis. The default value of this setting is an empty dictionary, but the default package name for migration modules is `migrations`.
Example:
```
{"blog": "blog.db_migrations"}

```

In this case, migrations pertaining to the `blog` app will be contained in the `blog.db_migrations` package.
If you provide the `app_label` argument, [`makemigrations`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-makemigrations) will automatically create the package if it doesn’t already exist.
When you supply `None` as a value for an app, Django will consider the app as an app without migrations regardless of an existing `migrations` submodule. This can be used, for example, in a test settings file to skip migrations while testing (tables will still be created for the apps’ models). To disable migrations for all apps during tests, you can set the [`MIGRATE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEST_MIGRATE) to `False` instead. If `MIGRATION_MODULES` is used in your general project settings, remember to use the [`migrate --run-syncdb`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-migrate-run-syncdb) option if you want to create tables for the app.
###  `MONTH_DAY_FORMAT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#month-day-format "Link to this heading")
Default: `'F j'`
The default formatting to use for date fields on Django admin change-list pages – and, possibly, by other parts of the system – in cases when only the month and day are displayed.
For example, when a Django admin change-list page is being filtered by a date drilldown, the header for a given day displays the day and month. Different locales have different formats. For example, U.S. English would say “January 1,” whereas Spanish might say “1 Enero.”
Note that the corresponding locale-dictated format has higher precedence and will be applied instead.
See [`allowed date format strings`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatefilter-date). See also [`DATE_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATE_FORMAT), [`DATETIME_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATETIME_FORMAT), [`TIME_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_FORMAT) and [`YEAR_MONTH_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-YEAR_MONTH_FORMAT).
###  `NUMBER_GROUPING`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#number-grouping "Link to this heading")
Default: `0`
Number of digits grouped together on the integer part of a number.
Common use is to display a thousand separator. If this setting is `0`, then no grouping will be applied to the number. If this setting is greater than `0`, then [`THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-THOUSAND_SEPARATOR) will be used as the separator between those groups.
Some locales use non-uniform digit grouping, e.g. `10,00,00,000` in `en_IN`. For this case, you can provide a sequence with the number of digit group sizes to be applied. The first number defines the size of the group preceding the decimal delimiter, and each number that follows defines the size of preceding groups. If the sequence is terminated with `-1`, no further grouping is performed. If the sequence terminates with a `0`, the last group size is used for the remainder of the number.
Example tuple for `en_IN`:
```
NUMBER_GROUPING = (3, 2, 0)

```

Note that the locale-dictated format has higher precedence and will be applied instead.
See also [`DECIMAL_SEPARATOR`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DECIMAL_SEPARATOR), [`THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-THOUSAND_SEPARATOR) and [`USE_THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_THOUSAND_SEPARATOR).
###  `PREPEND_WWW`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#prepend-www "Link to this heading")
Default: `False`
Whether to prepend the “www.” subdomain to URLs that don’t have it. This is only used if [`CommonMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.common.CommonMiddleware "django.middleware.common.CommonMiddleware") is installed (see [Middleware](https://docs.djangoproject.com/en/5.0/topics/http/middleware/)). See also [`APPEND_SLASH`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-APPEND_SLASH).
###  `ROOT_URLCONF`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#root-urlconf "Link to this heading")
Default: Not defined
A string representing the full Python import path to your root URLconf, for example `"mydjangoapps.urls"`. Can be overridden on a per-request basis by setting the attribute `urlconf` on the incoming `HttpRequest` object. See [How Django processes a request](https://docs.djangoproject.com/en/5.0/topics/http/urls/#how-django-processes-a-request) for details.
###  `SECRET_KEY`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#secret-key "Link to this heading")
Default: `''` (Empty string)
A secret key for a particular Django installation. This is used to provide [cryptographic signing](https://docs.djangoproject.com/en/5.0/topics/signing/), and should be set to a unique, unpredictable value.
[`django-admin startproject`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startproject) automatically adds a randomly-generated `SECRET_KEY` to each new project.
Uses of the key shouldn’t assume that it’s text or bytes. Every use should go through [`force_str()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.encoding.force_str "django.utils.encoding.force_str") or [`force_bytes()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.encoding.force_bytes "django.utils.encoding.force_bytes") to convert it to the desired type.
Django will refuse to start if [`SECRET_KEY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY) is not set.
Warning
**Keep this value secret.**
Running Django with a known [`SECRET_KEY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY) defeats many of Django’s security protections, and can lead to privilege escalation and remote code execution vulnerabilities.
The secret key is used for:
  * All [sessions](https://docs.djangoproject.com/en/5.0/topics/http/sessions/) if you are using any other session backend than `django.contrib.sessions.backends.cache`, or are using the default [`get_session_auth_hash()`](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash").
  * All [messages](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/) if you are using [`CookieStorage`](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#django.contrib.messages.storage.cookie.CookieStorage "django.contrib.messages.storage.cookie.CookieStorage") or [`FallbackStorage`](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#django.contrib.messages.storage.fallback.FallbackStorage "django.contrib.messages.storage.fallback.FallbackStorage").
  * All [`PasswordResetView`](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.views.PasswordResetView "django.contrib.auth.views.PasswordResetView") tokens.
  * Any usage of [cryptographic signing](https://docs.djangoproject.com/en/5.0/topics/signing/), unless a different key is provided.


When a secret key is no longer set as [`SECRET_KEY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY) or contained within [`SECRET_KEY_FALLBACKS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY_FALLBACKS) all of the above will be invalidated. When rotating your secret key, you should move the old key to [`SECRET_KEY_FALLBACKS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY_FALLBACKS) temporarily. Secret keys are not used for passwords of users and key rotation will not affect them.
Note
The default `settings.py` file created by [`django-admin startproject`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startproject) creates a unique `SECRET_KEY` for convenience.
###  `SECRET_KEY_FALLBACKS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#secret-key-fallbacks "Link to this heading")
Default: `[]`
A list of fallback secret keys for a particular Django installation. These are used to allow rotation of the `SECRET_KEY`.
In order to rotate your secret keys, set a new `SECRET_KEY` and move the previous value to the beginning of `SECRET_KEY_FALLBACKS`. Then remove the old values from the end of the `SECRET_KEY_FALLBACKS` when you are ready to expire the sessions, password reset tokens, and so on, that make use of them.
Note
Signing operations are computationally expensive. Having multiple old key values in `SECRET_KEY_FALLBACKS` adds additional overhead to all checks that don’t match an earlier key.
As such, fallback values should be removed after an appropriate period, allowing for key rotation.
Uses of the secret key values shouldn’t assume that they are text or bytes. Every use should go through [`force_str()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.encoding.force_str "django.utils.encoding.force_str") or [`force_bytes()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.encoding.force_bytes "django.utils.encoding.force_bytes") to convert it to the desired type.
###  `SECURE_CONTENT_TYPE_NOSNIFF`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#secure-content-type-nosniff "Link to this heading")
Default: `True`
If `True`, the [`SecurityMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware") sets the [X-Content-Type-Options: nosniff](https://docs.djangoproject.com/en/5.0/ref/middleware/#x-content-type-options) header on all responses that do not already have it.
###  `SECURE_CROSS_ORIGIN_OPENER_POLICY`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#secure-cross-origin-opener-policy "Link to this heading")
Default: `'same-origin'`
Unless set to `None`, the [`SecurityMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware") sets the [Cross-Origin Opener Policy](https://docs.djangoproject.com/en/5.0/ref/middleware/#cross-origin-opener-policy) header on all responses that do not already have it to the value provided.
###  `SECURE_HSTS_INCLUDE_SUBDOMAINS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#secure-hsts-include-subdomains "Link to this heading")
Default: `False`
If `True`, the [`SecurityMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware") adds the `includeSubDomains` directive to the [HTTP Strict Transport Security](https://docs.djangoproject.com/en/5.0/ref/middleware/#http-strict-transport-security) header. It has no effect unless [`SECURE_HSTS_SECONDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_SECONDS) is set to a non-zero value.
Warning
Setting this incorrectly can irreversibly (for the value of [`SECURE_HSTS_SECONDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_SECONDS)) break your site. Read the [HTTP Strict Transport Security](https://docs.djangoproject.com/en/5.0/ref/middleware/#http-strict-transport-security) documentation first.
###  `SECURE_HSTS_PRELOAD`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#secure-hsts-preload "Link to this heading")
Default: `False`
If `True`, the [`SecurityMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware") adds the `preload` directive to the [HTTP Strict Transport Security](https://docs.djangoproject.com/en/5.0/ref/middleware/#http-strict-transport-security) header. It has no effect unless [`SECURE_HSTS_SECONDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_HSTS_SECONDS) is set to a non-zero value.
###  `SECURE_HSTS_SECONDS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#secure-hsts-seconds "Link to this heading")
Default: `0`
If set to a non-zero integer value, the [`SecurityMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware") sets the [HTTP Strict Transport Security](https://docs.djangoproject.com/en/5.0/ref/middleware/#http-strict-transport-security) header on all responses that do not already have it.
Warning
Setting this incorrectly can irreversibly (for some time) break your site. Read the [HTTP Strict Transport Security](https://docs.djangoproject.com/en/5.0/ref/middleware/#http-strict-transport-security) documentation first.
###  `SECURE_PROXY_SSL_HEADER`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#secure-proxy-ssl-header "Link to this heading")
Default: `None`
A tuple representing an HTTP header/value combination that signifies a request is secure. This controls the behavior of the request object’s `is_secure()` method.
By default, `is_secure()` determines if a request is secure by confirming that a requested URL uses `https://`. This method is important for Django’s CSRF protection, and it may be used by your own code or third-party apps.
If your Django app is behind a proxy, though, the proxy may be “swallowing” whether the original request uses HTTPS or not. If there is a non-HTTPS connection between the proxy and Django then `is_secure()` would always return `False` – even for requests that were made via HTTPS by the end user. In contrast, if there is an HTTPS connection between the proxy and Django then `is_secure()` would always return `True` – even for requests that were made originally via HTTP.
In this situation, configure your proxy to set a custom HTTP header that tells Django whether the request came in via HTTPS, and set `SECURE_PROXY_SSL_HEADER` so that Django knows what header to look for.
Set a tuple with two elements – the name of the header to look for and the required value. For example:
```
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

```

This tells Django to trust the `X-Forwarded-Proto` header that comes from our proxy and that the request is guaranteed to be secure (i.e., it originally came in via HTTPS) when:
  * the header value is `'https'`, or
  * its initial, leftmost value is `'https'` in the case of a comma-separated list of protocols (e.g. `'https,http,http'`).


You should _only_ set this setting if you control your proxy or have some other guarantee that it sets/strips this header appropriately.
Note that the header needs to be in the format as used by `request.META` – all caps and likely starting with `HTTP_`. (Remember, Django automatically adds `'HTTP_'` to the start of x-header names before making the header available in `request.META`.)
Warning
**Modifying this setting can compromise your site’s security. Ensure you fully understand your setup before changing it.**
