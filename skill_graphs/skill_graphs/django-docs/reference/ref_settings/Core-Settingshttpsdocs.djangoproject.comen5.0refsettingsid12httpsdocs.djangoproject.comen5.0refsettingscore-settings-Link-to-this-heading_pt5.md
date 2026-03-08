Make sure ALL of the following are true before setting this (assuming the values from the example above):
  * Your Django app is behind a proxy.
  * Your proxy strips the `X-Forwarded-Proto` header from all incoming requests, even when it contains a comma-separated list of protocols. In other words, if end users include that header in their requests, the proxy will discard it.
  * Your proxy sets the `X-Forwarded-Proto` header and sends it to Django, but only for requests that originally come in via HTTPS.


If any of those are not true, you should keep this setting set to `None` and find another way of determining HTTPS, perhaps via custom middleware.
###  `SECURE_REDIRECT_EXEMPT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#secure-redirect-exempt "Link to this heading")
Default: `[]` (Empty list)
If a URL path matches a regular expression in this list, the request will not be redirected to HTTPS. The [`SecurityMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware") strips leading slashes from URL paths, so patterns shouldn’t include them, e.g. `SECURE_REDIRECT_EXEMPT = [r'^no-ssl/$', …]`. If [`SECURE_SSL_REDIRECT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_SSL_REDIRECT) is `False`, this setting has no effect.
###  `SECURE_REFERRER_POLICY`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#secure-referrer-policy "Link to this heading")
Default: `'same-origin'`
If configured, the [`SecurityMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware") sets the [Referrer Policy](https://docs.djangoproject.com/en/5.0/ref/middleware/#referrer-policy) header on all responses that do not already have it to the value provided.
###  `SECURE_SSL_HOST`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#secure-ssl-host "Link to this heading")
Default: `None`
If a string (e.g. `secure.example.com`), all SSL redirects will be directed to this host rather than the originally-requested host (e.g. `www.example.com`). If [`SECURE_SSL_REDIRECT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_SSL_REDIRECT) is `False`, this setting has no effect.
###  `SECURE_SSL_REDIRECT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#secure-ssl-redirect "Link to this heading")
Default: `False`
If `True`, the [`SecurityMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.security.SecurityMiddleware "django.middleware.security.SecurityMiddleware") [redirects](https://docs.djangoproject.com/en/5.0/ref/middleware/#ssl-redirect) all non-HTTPS requests to HTTPS (except for those URLs matching a regular expression listed in [`SECURE_REDIRECT_EXEMPT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_REDIRECT_EXEMPT)).
Note
If turning this to `True` causes infinite redirects, it probably means your site is running behind a proxy and can’t tell which requests are secure and which are not. Your proxy likely sets a header to indicate secure requests; you can correct the problem by finding out what that header is and configuring the [`SECURE_PROXY_SSL_HEADER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECURE_PROXY_SSL_HEADER) setting accordingly.
###  `SERIALIZATION_MODULES`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#serialization-modules "Link to this heading")
Default: Not defined
A dictionary of modules containing serializer definitions (provided as strings), keyed by a string identifier for that serialization type. For example, to define a YAML serializer, use:
```
SERIALIZATION_MODULES = {"yaml": "path.to.yaml_serializer"}

```

###  `SERVER_EMAIL`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#server-email "Link to this heading")
Default: `'root@localhost'`
The email address that error messages come from, such as those sent to [`ADMINS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ADMINS) and [`MANAGERS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MANAGERS). This address is used in the `From:` header and can take any format valid in the chosen email sending protocol.
Why are my emails sent from a different address?
This address is used only for error messages. It is _not_ the address that regular email messages sent with [`send_mail()`](https://docs.djangoproject.com/en/5.0/topics/email/#django.core.mail.send_mail "django.core.mail.send_mail") come from; for that, see [`DEFAULT_FROM_EMAIL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEFAULT_FROM_EMAIL).
###  `SHORT_DATE_FORMAT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#short-date-format "Link to this heading")
Default: `'m/d/Y'` (e.g. `12/31/2003`)
An available formatting that can be used for displaying date fields on templates. Note that the corresponding locale-dictated format has higher precedence and will be applied instead. See [`allowed date format strings`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatefilter-date).
See also [`DATE_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATE_FORMAT) and [`SHORT_DATETIME_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SHORT_DATETIME_FORMAT).
###  `SHORT_DATETIME_FORMAT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#short-datetime-format "Link to this heading")
Default: `'m/d/Y P'` (e.g. `12/31/2003 4 p.m.`)
An available formatting that can be used for displaying datetime fields on templates. Note that the corresponding locale-dictated format has higher precedence and will be applied instead. See [`allowed date format strings`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatefilter-date).
See also [`DATE_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATE_FORMAT) and [`SHORT_DATE_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SHORT_DATE_FORMAT).
###  `SIGNING_BACKEND`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#signing-backend "Link to this heading")
Default: `'django.core.signing.TimestampSigner'`
The backend used for signing cookies and other data.
See also the [Cryptographic signing](https://docs.djangoproject.com/en/5.0/topics/signing/) documentation.
###  `SILENCED_SYSTEM_CHECKS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#silenced-system-checks "Link to this heading")
Default: `[]` (Empty list)
A list of identifiers of messages generated by the system check framework (i.e. `["models.W001"]`) that you wish to permanently acknowledge and ignore. Silenced checks will not be output to the console.
See also the [System check framework](https://docs.djangoproject.com/en/5.0/ref/checks/) documentation.
###  `STORAGES`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#storages "Link to this heading")
New in Django 4.2.
Default:
```
{
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

```

A dictionary containing the settings for all storages to be used with Django. It is a nested dictionary whose contents map a storage alias to a dictionary containing the options for an individual storage.
Storages can have any alias you choose. However, there are two aliases with special significance:
  * `default` for [managing files](https://docs.djangoproject.com/en/5.0/topics/files/). `'`[`django.core.files.storage.FileSystemStorage`](https://docs.djangoproject.com/en/5.0/ref/files/storage/#django.core.files.storage.FileSystemStorage "django.core.files.storage.FileSystemStorage")`'` is the default storage engine.
  * `staticfiles` for [managing static files](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/). `'`[`django.contrib.staticfiles.storage.StaticFilesStorage`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django.contrib.staticfiles.storage.StaticFilesStorage "django.contrib.staticfiles.storage.StaticFilesStorage")`'` is the default storage engine.


The following is an example `settings.py` snippet defining a custom file storage called `example`:
```
STORAGES = {
    # ...
    "example": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
        "OPTIONS": {
            "location": "/example",
            "base_url": "/example/",
        },
    },
}

```

`OPTIONS` are passed to the `BACKEND` on initialization in `**kwargs`.
A ready-to-use instance of the storage backends can be retrieved from [`django.core.files.storage.storages`](https://docs.djangoproject.com/en/5.0/ref/files/storage/#django.core.files.storage.storages "django.core.files.storage.storages"). Use a key corresponding to the backend definition in [`STORAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES).
Is my value merged with the default value?
Defining this setting overrides the default value and is _not_ merged with it.
###  `TEMPLATES`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#templates "Link to this heading")
Default: `[]` (Empty list)
A list containing the settings for all template engines to be used with Django. Each item of the list is a dictionary containing the options for an individual engine.
Here’s a setup that tells the Django template engine to load templates from the `templates` subdirectory inside each installed application:
```
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    },
]

```

The following options are available for all backends.
####  `BACKEND`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-BACKEND "Link to this heading")
Default: Not defined
The template backend to use. The built-in template backends are:
  * `'django.template.backends.django.DjangoTemplates'`
  * `'django.template.backends.jinja2.Jinja2'`


You can use a template backend that doesn’t ship with Django by setting `BACKEND` to a fully-qualified path (i.e. `'mypackage.whatever.Backend'`).
####  `NAME`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-NAME "Link to this heading")
Default: see below
The alias for this particular template engine. It’s an identifier that allows selecting an engine for rendering. Aliases must be unique across all configured template engines.
It defaults to the name of the module defining the engine class, i.e. the next to last piece of [`BACKEND`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-BACKEND), when it isn’t provided. For example if the backend is `'mypackage.whatever.Backend'` then its default name is `'whatever'`.
####  `DIRS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#dirs "Link to this heading")
Default: `[]` (Empty list)
Directories where the engine should look for template source files, in search order.
####  `APP_DIRS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#app-dirs "Link to this heading")
Default: `False`
Whether the engine should look for template source files inside installed applications.
Note
The default `settings.py` file created by [`django-admin startproject`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startproject) sets `'APP_DIRS': True`.
####  `OPTIONS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-OPTIONS "Link to this heading")
Default: `{}` (Empty dict)
Extra parameters to pass to the template backend. Available parameters vary depending on the template backend. See [`DjangoTemplates`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.backends.django.DjangoTemplates "django.template.backends.django.DjangoTemplates") and [`Jinja2`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.backends.jinja2.Jinja2 "django.template.backends.jinja2.Jinja2") for the options of the built-in backends.
###  `TEST_RUNNER`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#test-runner "Link to this heading")
Default: `'django.test.runner.DiscoverRunner'`
The name of the class to use for starting the test suite. See [Using different testing frameworks](https://docs.djangoproject.com/en/5.0/topics/testing/advanced/#other-testing-frameworks).
###  `TEST_NON_SERIALIZED_APPS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#test-non-serialized-apps "Link to this heading")
Default: `[]` (Empty list)
In order to restore the database state between tests for `TransactionTestCase`s and database backends without transactions, Django will [serialize the contents of all apps](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#test-case-serialized-rollback) when it starts the test run so it can then reload from that copy before running tests that need it.
This slows down the startup time of the test runner; if you have apps that you know don’t need this feature, you can add their full names in here (e.g. `'django.contrib.contenttypes'`) to exclude them from this serialization process.
###  `THOUSAND_SEPARATOR`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#thousand-separator "Link to this heading")
Default: `','` (Comma)
Default thousand separator used when formatting numbers. This setting is used only when [`USE_THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_THOUSAND_SEPARATOR) is `True` and [`NUMBER_GROUPING`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-NUMBER_GROUPING) is greater than `0`.
Note that the locale-dictated format has higher precedence and will be applied instead.
See also [`NUMBER_GROUPING`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-NUMBER_GROUPING), [`DECIMAL_SEPARATOR`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DECIMAL_SEPARATOR) and [`USE_THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_THOUSAND_SEPARATOR).
###  `TIME_FORMAT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#time-format "Link to this heading")
Default: `'P'` (e.g. `4 p.m.`)
The default formatting to use for displaying time fields in any part of the system. Note that the locale-dictated format has higher precedence and will be applied instead. See [`allowed date format strings`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatefilter-date).
See also [`DATE_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATE_FORMAT) and [`DATETIME_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATETIME_FORMAT).
###  `TIME_INPUT_FORMATS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#time-input-formats "Link to this heading")
Default:
```
[
    "%H:%M:%S",  # '14:30:59'
    "%H:%M:%S.%f",  # '14:30:59.000200'
    "%H:%M",  # '14:30'
]

```

A list of formats that will be accepted when inputting data on a time field. Formats will be tried in order, using the first valid one. Note that these format strings use Python’s [`date`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatefilter-date) template filter.
The locale-dictated format has higher precedence and will be applied instead.
See also [`DATE_INPUT_FORMATS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATE_INPUT_FORMATS) and [`DATETIME_INPUT_FORMATS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATETIME_INPUT_FORMATS).
###  `TIME_ZONE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_ZONE "Link to this heading")
Default: `'America/Chicago'`
A string representing the time zone for this installation. See the
Note
Since Django was first released with the [`TIME_ZONE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_ZONE) set to `'America/Chicago'`, the global setting (used if nothing is defined in your project’s `settings.py`) remains `'America/Chicago'` for backwards compatibility. New project templates default to `'UTC'`.
Note that this isn’t necessarily the time zone of the server. For example, one server may serve multiple Django-powered sites, each with a separate time zone setting.
When [`USE_TZ`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_TZ) is `False`, this is the time zone in which Django will store all datetimes. When [`USE_TZ`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_TZ) is `True`, this is the default time zone that Django will use to display datetimes in templates and to interpret datetimes entered in forms.
On Unix environments (where `os.environ['TZ']` variable to the time zone you specify in the [`TIME_ZONE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_ZONE) setting. Thus, all your views and models will automatically operate in this time zone. However, Django won’t set the `TZ` environment variable if you’re using the manual configuration option as described in [manually configuring settings](https://docs.djangoproject.com/en/5.0/topics/settings/#settings-without-django-settings-module). If Django doesn’t set the `TZ` environment variable, it’s up to you to ensure your processes are running in the correct environment.
Note
Django cannot reliably use alternate time zones in a Windows environment. If you’re running Django on Windows, [`TIME_ZONE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_ZONE) must be set to match the system time zone.
###  `USE_I18N`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#use-i18n "Link to this heading")
Default: `True`
A boolean that specifies whether Django’s translation system should be enabled. This provides a way to turn it off, for performance. If this is set to `False`, Django will make some optimizations so as not to load the translation machinery.
See also [`LANGUAGE_CODE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LANGUAGE_CODE) and [`USE_TZ`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_TZ).
Note
The default `settings.py` file created by [`django-admin startproject`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startproject) includes `USE_I18N = True` for convenience.
###  `USE_THOUSAND_SEPARATOR`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#use-thousand-separator "Link to this heading")
Default: `False`
A boolean that specifies whether to display numbers using a thousand separator. When set to `True`, Django will format numbers using the [`NUMBER_GROUPING`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-NUMBER_GROUPING) and [`THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-THOUSAND_SEPARATOR) settings. The latter two settings may also be dictated by the locale, which takes precedence.
See also [`DECIMAL_SEPARATOR`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DECIMAL_SEPARATOR), [`NUMBER_GROUPING`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-NUMBER_GROUPING) and [`THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-THOUSAND_SEPARATOR).
###  `USE_TZ`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#use-tz "Link to this heading")
Default: `True`
A boolean that specifies if datetimes will be timezone-aware by default or not. If this is set to `True`, Django will use timezone-aware datetimes internally.
When `USE_TZ` is False, Django will use naive datetimes in local time, except when parsing ISO 8601 formatted strings, where timezone information will always be retained if present.
See also [`TIME_ZONE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_ZONE) and [`USE_I18N`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_I18N).
Changed in Django 5.0:
In older versions, the default value is `False`.
###  `USE_X_FORWARDED_HOST`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#use-x-forwarded-host "Link to this heading")
Default: `False`
A boolean that specifies whether to use the `X-Forwarded-Host` header in preference to the `Host` header. This should only be enabled if a proxy which sets this header is in use.
This setting takes priority over [`USE_X_FORWARDED_PORT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_X_FORWARDED_PORT). Per `X-Forwarded-Host` header can include the port number, in which case you shouldn’t use [`USE_X_FORWARDED_PORT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_X_FORWARDED_PORT).
###  `USE_X_FORWARDED_PORT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#use-x-forwarded-port "Link to this heading")
Default: `False`
A boolean that specifies whether to use the `X-Forwarded-Port` header in preference to the `SERVER_PORT` `META` variable. This should only be enabled if a proxy which sets this header is in use.
[`USE_X_FORWARDED_HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_X_FORWARDED_HOST) takes priority over this setting.
###  `WSGI_APPLICATION`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#wsgi-application "Link to this heading")
Default: `None`
The full Python path of the WSGI application object that Django’s built-in servers (e.g. [`runserver`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-runserver)) will use. The [`django-admin startproject`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startproject) management command will create a standard `wsgi.py` file with an `application` callable in it, and point this setting to that `application`.
If not set, the return value of `django.core.wsgi.get_wsgi_application()` will be used. In this case, the behavior of [`runserver`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-runserver) will be identical to previous Django versions.
###  `YEAR_MONTH_FORMAT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#year-month-format "Link to this heading")
Default: `'F Y'`
The default formatting to use for date fields on Django admin change-list pages – and, possibly, by other parts of the system – in cases when only the year and month are displayed.
For example, when a Django admin change-list page is being filtered by a date drilldown, the header for a given month displays the month and the year. Different locales have different formats. For example, U.S. English would say “January 2006,” whereas another locale might say “2006/January.”
Note that the corresponding locale-dictated format has higher precedence and will be applied instead.
See [`allowed date format strings`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatefilter-date). See also [`DATE_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATE_FORMAT), [`DATETIME_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATETIME_FORMAT), [`TIME_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_FORMAT) and [`MONTH_DAY_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MONTH_DAY_FORMAT).
###  `X_FRAME_OPTIONS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#x-frame-options "Link to this heading")
Default: `'DENY'`
The default value for the X-Frame-Options header used by [`XFrameOptionsMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.clickjacking.XFrameOptionsMiddleware "django.middleware.clickjacking.XFrameOptionsMiddleware"). See the [clickjacking protection](https://docs.djangoproject.com/en/5.0/ref/clickjacking/) documentation.
