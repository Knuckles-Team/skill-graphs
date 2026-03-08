Default exception reporter filter class to be used if none has been assigned to the [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") instance yet. See [Filtering error reports](https://docs.djangoproject.com/en/5.0/howto/error-reporting/#filtering-error-reports).
###  `DEFAULT_FILE_STORAGE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#default-file-storage "Link to this heading")
Default: `'`[`django.core.files.storage.FileSystemStorage`](https://docs.djangoproject.com/en/5.0/ref/files/storage/#django.core.files.storage.FileSystemStorage "django.core.files.storage.FileSystemStorage")`'`
Default file storage class to be used for any file-related operations that don’t specify a particular storage system. See [Managing files](https://docs.djangoproject.com/en/5.0/topics/files/).
Deprecated since version 4.2: This setting is deprecated. Starting with Django 4.2, default file storage engine can be configured with the [`STORAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES) setting under the `default` key.
###  `DEFAULT_FROM_EMAIL`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#default-from-email "Link to this heading")
Default: `'webmaster@localhost'`
Default email address for automated correspondence from the site manager(s). This address is used in the `From:` header of outgoing emails and can take any format valid in the chosen email sending protocol.
This doesn’t affect error messages sent to [`ADMINS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ADMINS) and [`MANAGERS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MANAGERS). See [`SERVER_EMAIL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SERVER_EMAIL) for that.
###  `DEFAULT_INDEX_TABLESPACE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#default-index-tablespace "Link to this heading")
Default: `''` (Empty string)
Default tablespace to use for indexes on fields that don’t specify one, if the backend supports it (see [Tablespaces](https://docs.djangoproject.com/en/5.0/topics/db/tablespaces/)).
###  `DEFAULT_TABLESPACE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#default-tablespace "Link to this heading")
Default: `''` (Empty string)
Default tablespace to use for models that don’t specify one, if the backend supports it (see [Tablespaces](https://docs.djangoproject.com/en/5.0/topics/db/tablespaces/)).
###  `DISALLOWED_USER_AGENTS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#disallowed-user-agents "Link to this heading")
Default: `[]` (Empty list)
List of compiled regular expression objects representing User-Agent strings that are not allowed to visit any page, systemwide. Use this for bots/crawlers. This is only used if `CommonMiddleware` is installed (see [Middleware](https://docs.djangoproject.com/en/5.0/topics/http/middleware/)).
###  `EMAIL_BACKEND`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#email-backend "Link to this heading")
Default: `'`[`django.core.mail.backends.smtp.EmailBackend`](https://docs.djangoproject.com/en/5.0/topics/email/#django.core.mail.backends.smtp.EmailBackend "django.core.mail.backends.smtp.EmailBackend")`'`
The backend to use for sending emails. For the list of available backends see [Email backends](https://docs.djangoproject.com/en/5.0/topics/email/#topic-email-backends).
###  `EMAIL_FILE_PATH`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#email-file-path "Link to this heading")
Default: Not defined
The directory used by the [file email backend](https://docs.djangoproject.com/en/5.0/topics/email/#topic-email-file-backend) to store output files.
###  `EMAIL_HOST`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#email-host "Link to this heading")
Default: `'localhost'`
The host to use for sending email.
See also [`EMAIL_PORT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_PORT).
###  `EMAIL_HOST_PASSWORD`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#email-host-password "Link to this heading")
Default: `''` (Empty string)
Password to use for the SMTP server defined in [`EMAIL_HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_HOST). This setting is used in conjunction with [`EMAIL_HOST_USER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_HOST_USER) when authenticating to the SMTP server. If either of these settings is empty, Django won’t attempt authentication.
See also [`EMAIL_HOST_USER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_HOST_USER).
###  `EMAIL_HOST_USER`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#email-host-user "Link to this heading")
Default: `''` (Empty string)
Username to use for the SMTP server defined in [`EMAIL_HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_HOST). If empty, Django won’t attempt authentication.
See also [`EMAIL_HOST_PASSWORD`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_HOST_PASSWORD).
###  `EMAIL_PORT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#email-port "Link to this heading")
Default: `25`
Port to use for the SMTP server defined in [`EMAIL_HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_HOST).
###  `EMAIL_SUBJECT_PREFIX`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#email-subject-prefix "Link to this heading")
Default: `'[Django] '`
Subject-line prefix for email messages sent with `django.core.mail.mail_admins` or `django.core.mail.mail_managers`. You’ll probably want to include the trailing space.
###  `EMAIL_USE_LOCALTIME`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#email-use-localtime "Link to this heading")
Default: `False`
Whether to send the SMTP `Date` header of email messages in the local time zone (`True`) or in UTC (`False`).
###  `EMAIL_USE_TLS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#email-use-tls "Link to this heading")
Default: `False`
Whether to use a TLS (secure) connection when talking to the SMTP server. This is used for explicit TLS connections, generally on port 587. If you are experiencing hanging connections, see the implicit TLS setting [`EMAIL_USE_SSL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_USE_SSL).
###  `EMAIL_USE_SSL`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#email-use-ssl "Link to this heading")
Default: `False`
Whether to use an implicit TLS (secure) connection when talking to the SMTP server. In most email documentation this type of TLS connection is referred to as SSL. It is generally used on port 465. If you are experiencing problems, see the explicit TLS setting [`EMAIL_USE_TLS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_USE_TLS).
Note that [`EMAIL_USE_TLS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_USE_TLS)/[`EMAIL_USE_SSL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_USE_SSL) are mutually exclusive, so only set one of those settings to `True`.
###  `EMAIL_SSL_CERTFILE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#email-ssl-certfile "Link to this heading")
Default: `None`
If [`EMAIL_USE_SSL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_USE_SSL) or [`EMAIL_USE_TLS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_USE_TLS) is `True`, you can optionally specify the path to a PEM-formatted certificate chain file to use for the SSL connection.
###  `EMAIL_SSL_KEYFILE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#email-ssl-keyfile "Link to this heading")
Default: `None`
If [`EMAIL_USE_SSL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_USE_SSL) or [`EMAIL_USE_TLS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_USE_TLS) is `True`, you can optionally specify the path to a PEM-formatted private key file to use for the SSL connection.
Note that setting [`EMAIL_SSL_CERTFILE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_SSL_CERTFILE) and [`EMAIL_SSL_KEYFILE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_SSL_KEYFILE) doesn’t result in any certificate checking. They’re passed to the underlying SSL connection. Please refer to the documentation of Python’s
###  `EMAIL_TIMEOUT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#email-timeout "Link to this heading")
Default: `None`
Specifies a timeout in seconds for blocking operations like the connection attempt.
###  `FILE_UPLOAD_HANDLERS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#file-upload-handlers "Link to this heading")
Default:
```
[
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
]

```

A list of handlers to use for uploading. Changing this setting allows complete customization – even replacement – of Django’s upload process.
See [Managing files](https://docs.djangoproject.com/en/5.0/topics/files/) for details.
###  `FILE_UPLOAD_MAX_MEMORY_SIZE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#file-upload-max-memory-size "Link to this heading")
Default: `2621440` (i.e. 2.5 MB).
The maximum size (in bytes) that an upload will be before it gets streamed to the file system. See [Managing files](https://docs.djangoproject.com/en/5.0/topics/files/) for details.
See also [`DATA_UPLOAD_MAX_MEMORY_SIZE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATA_UPLOAD_MAX_MEMORY_SIZE).
###  `FILE_UPLOAD_DIRECTORY_PERMISSIONS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#file-upload-directory-permissions "Link to this heading")
Default: `None`
The numeric mode to apply to directories created in the process of uploading files.
This setting also determines the default permissions for collected static directories when using the [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) management command. See [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) for details on overriding it.
This value mirrors the functionality and caveats of the [`FILE_UPLOAD_PERMISSIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-FILE_UPLOAD_PERMISSIONS) setting.
###  `FILE_UPLOAD_PERMISSIONS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#file-upload-permissions "Link to this heading")
Default: `0o644`
The numeric mode (i.e. `0o644`) to set newly uploaded files to. For more information about what these modes mean, see the documentation for
If `None`, you’ll get operating-system dependent behavior. On most platforms, temporary files will have a mode of `0o600`, and files saved from memory will be saved using the system’s standard umask.
For security reasons, these permissions aren’t applied to the temporary files that are stored in [`FILE_UPLOAD_TEMP_DIR`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-FILE_UPLOAD_TEMP_DIR).
This setting also determines the default permissions for collected static files when using the [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) management command. See [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) for details on overriding it.
Warning
**Always prefix the mode with** `0o` **.**
If you’re not familiar with file modes, please note that the `0o` prefix is very important: it indicates an octal number, which is the way that modes must be specified. If you try to use `644`, you’ll get totally incorrect behavior.
###  `FILE_UPLOAD_TEMP_DIR`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#file-upload-temp-dir "Link to this heading")
Default: `None`
The directory to store data to (typically files larger than [`FILE_UPLOAD_MAX_MEMORY_SIZE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-FILE_UPLOAD_MAX_MEMORY_SIZE)) temporarily while uploading files. If `None`, Django will use the standard temporary directory for the operating system. For example, this will default to `/tmp` on *nix-style operating systems.
See [Managing files](https://docs.djangoproject.com/en/5.0/topics/files/) for details.
###  `FIRST_DAY_OF_WEEK`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#first-day-of-week "Link to this heading")
Default: `0` (Sunday)
A number representing the first day of the week. This is especially useful when displaying a calendar. This value is only used when not using format internationalization, or when a format cannot be found for the current locale.
The value must be an integer from 0 to 6, where 0 means Sunday, 1 means Monday and so on.
###  `FIXTURE_DIRS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#fixture-dirs "Link to this heading")
Default: `[]` (Empty list)
List of directories searched for [fixture](https://docs.djangoproject.com/en/5.0/topics/db/fixtures/#fixtures-explanation) files, in addition to the `fixtures` directory of each application, in search order.
Note that these paths should use Unix-style forward slashes, even on Windows.
See [Provide data with fixtures](https://docs.djangoproject.com/en/5.0/howto/initial-data/#initial-data-via-fixtures) and [Fixture loading](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#topics-testing-fixtures).
###  `FORCE_SCRIPT_NAME`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#force-script-name "Link to this heading")
Default: `None`
If not `None`, this will be used as the value of the `SCRIPT_NAME` environment variable in any HTTP request. This setting can be used to override the server-provided value of `SCRIPT_NAME`, which may be a rewritten version of the preferred value or not supplied at all. It is also used by [`django.setup()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.setup "django.setup") to set the URL resolver script prefix outside of the request/response cycle (e.g. in management commands and standalone scripts) to generate correct URLs when `FORCE_SCRIPT_NAME` is provided.
###  `FORM_RENDERER`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#form-renderer "Link to this heading")
Default: `'`[`django.forms.renderers.DjangoTemplates`](https://docs.djangoproject.com/en/5.0/ref/forms/renderers/#django.forms.renderers.DjangoTemplates "django.forms.renderers.DjangoTemplates")`'`
The class that renders forms and form widgets. It must implement [the low-level render API](https://docs.djangoproject.com/en/5.0/ref/forms/renderers/#low-level-widget-render-api). Included form renderers are:
  * `'`[`django.forms.renderers.DjangoTemplates`](https://docs.djangoproject.com/en/5.0/ref/forms/renderers/#django.forms.renderers.DjangoTemplates "django.forms.renderers.DjangoTemplates")`'`
  * `'`[`django.forms.renderers.Jinja2`](https://docs.djangoproject.com/en/5.0/ref/forms/renderers/#django.forms.renderers.Jinja2 "django.forms.renderers.Jinja2")`'`
  * `'`[`django.forms.renderers.TemplatesSetting`](https://docs.djangoproject.com/en/5.0/ref/forms/renderers/#django.forms.renderers.TemplatesSetting "django.forms.renderers.TemplatesSetting")`'`


###  `FORMS_URLFIELD_ASSUME_HTTPS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#forms-urlfield-assume-https "Link to this heading")
New in Django 5.0.
Deprecated since version 5.0.
Default: `False`
Set this transitional setting to `True` to opt into using `"https"` as the new default value of [`URLField.assume_scheme`](https://docs.djangoproject.com/en/5.0/ref/forms/fields/#django.forms.URLField.assume_scheme "django.forms.URLField.assume_scheme") during the Django 5.x release cycle.
###  `FORMAT_MODULE_PATH`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#format-module-path "Link to this heading")
Default: `None`
A full Python path to a Python package that contains custom format definitions for project locales. If not `None`, Django will check for a `formats.py` file, under the directory named as the current locale, and will use the formats defined in this file.
The name of the directory containing the format definitions is expected to be named using [locale name](https://docs.djangoproject.com/en/5.0/topics/i18n/#term-locale-name) notation, for example `de`, `pt_BR`, `en_US`, etc.
For example, if [`FORMAT_MODULE_PATH`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-FORMAT_MODULE_PATH) is set to `mysite.formats`, and current language is `en` (English), Django will expect a directory tree like:
```
mysite/
    formats/
        __init__.py
        en/
            __init__.py
            formats.py

```

You can also set this setting to a list of Python paths, for example:
```
FORMAT_MODULE_PATH = [
    "mysite.formats",
    "some_app.formats",
]

```

When Django searches for a certain format, it will go through all given Python paths until it finds a module that actually defines the given format. This means that formats defined in packages farther up in the list will take precedence over the same formats in packages farther down.
Available formats are:
  * [`DATE_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATE_FORMAT)
  * [`DATE_INPUT_FORMATS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATE_INPUT_FORMATS)
  * [`DATETIME_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATETIME_FORMAT),
  * [`DATETIME_INPUT_FORMATS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATETIME_INPUT_FORMATS)
  * [`DECIMAL_SEPARATOR`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DECIMAL_SEPARATOR)
  * [`FIRST_DAY_OF_WEEK`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-FIRST_DAY_OF_WEEK)
  * [`MONTH_DAY_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MONTH_DAY_FORMAT)
  * [`NUMBER_GROUPING`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-NUMBER_GROUPING)
  * [`SHORT_DATE_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SHORT_DATE_FORMAT)
  * [`SHORT_DATETIME_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SHORT_DATETIME_FORMAT)
  * [`THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-THOUSAND_SEPARATOR)
  * [`TIME_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_FORMAT)
  * [`TIME_INPUT_FORMATS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_INPUT_FORMATS)
  * [`YEAR_MONTH_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-YEAR_MONTH_FORMAT)


###  `IGNORABLE_404_URLS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#ignorable-404-urls "Link to this heading")
Default: `[]` (Empty list)
List of compiled regular expression objects describing URLs that should be ignored when reporting HTTP 404 errors via email (see [How to manage error reporting](https://docs.djangoproject.com/en/5.0/howto/error-reporting/)). Regular expressions are matched against [`request's full paths`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.get_full_path "django.http.HttpRequest.get_full_path") (including query string, if any). Use this if your site does not provide a commonly requested file such as `favicon.ico` or `robots.txt`.
This is only used if [`BrokenLinkEmailsMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.common.BrokenLinkEmailsMiddleware "django.middleware.common.BrokenLinkEmailsMiddleware") is enabled (see [Middleware](https://docs.djangoproject.com/en/5.0/topics/http/middleware/)).
###  `INSTALLED_APPS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#installed-apps "Link to this heading")
Default: `[]` (Empty list)
A list of strings designating all applications that are enabled in this Django installation. Each string should be a dotted Python path to:
  * an application configuration class (preferred), or
  * a package containing an application.


[Learn more about application configurations](https://docs.djangoproject.com/en/5.0/ref/applications/).
Use the application registry for introspection
Your code should never access [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) directly. Use [`django.apps.apps`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps "django.apps.apps") instead.
Application names and labels must be unique in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS)
Application [`names`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.name "django.apps.AppConfig.name") — the dotted Python path to the application package — must be unique. There is no way to include the same application twice, short of duplicating its code under another name.
Application [`labels`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.label "django.apps.AppConfig.label") — by default the final part of the name — must be unique too. For example, you can’t include both `django.contrib.auth` and `myproject.auth`. However, you can relabel an application with a custom configuration that defines a different [`label`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.label "django.apps.AppConfig.label").
These rules apply regardless of whether [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) references application configuration classes or application packages.
When several applications provide different versions of the same resource (template, static file, management command, translation), the application listed first in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) has precedence.
###  `INTERNAL_IPS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#internal-ips "Link to this heading")
Default: `[]` (Empty list)
A list of IP addresses, as strings, that:
  * Allow the [`debug()`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.context_processors.debug "django.template.context_processors.debug") context processor to add some variables to the template context.
  * Can use the [admindocs bookmarklets](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/admindocs/#admindocs-bookmarklets) even if not logged in as a staff user.
  * Are marked as “internal” (as opposed to “EXTERNAL”) in [`AdminEmailHandler`](https://docs.djangoproject.com/en/5.0/ref/logging/#django.utils.log.AdminEmailHandler "django.utils.log.AdminEmailHandler") emails.


###  `LANGUAGE_CODE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#language-code "Link to this heading")
Default: `'en-us'`
A string representing the language code for this installation. This should be in standard [language ID format](https://docs.djangoproject.com/en/5.0/topics/i18n/#term-language-code). For example, U.S. English is `"en-us"`. See also the [Internationalization and localization](https://docs.djangoproject.com/en/5.0/topics/i18n/).
[`USE_I18N`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_I18N) must be active for this setting to have any effect.
It serves two purposes:
  * If the locale middleware isn’t in use, it decides which translation is served to all users.
  * If the locale middleware is active, it provides a fallback language in case the user’s preferred language can’t be determined or is not supported by the website. It also provides the fallback translation when a translation for a given literal doesn’t exist for the user’s preferred language.


See [How Django discovers language preference](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/#how-django-discovers-language-preference) for more details.
###  `LANGUAGE_COOKIE_AGE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#language-cookie-age "Link to this heading")
Default: `None` (expires at browser close)
The age of the language cookie, in seconds.
###  `LANGUAGE_COOKIE_DOMAIN`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#language-cookie-domain "Link to this heading")
Default: `None`
The domain to use for the language cookie. Set this to a string such as `"example.com"` for cross-domain cookies, or use `None` for a standard domain cookie.
Be cautious when updating this setting on a production site. If you update this setting to enable cross-domain cookies on a site that previously used standard domain cookies, existing user cookies that have the old domain will not be updated. This will result in site users being unable to switch the language as long as these cookies persist. The only safe and reliable option to perform the switch is to change the language cookie name permanently (via the [`LANGUAGE_COOKIE_NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LANGUAGE_COOKIE_NAME) setting) and to add a middleware that copies the value from the old cookie to a new one and then deletes the old one.
###  `LANGUAGE_COOKIE_HTTPONLY`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#language-cookie-httponly "Link to this heading")
Default: `False`
Whether to use `HttpOnly` flag on the language cookie. If this is set to `True`, client-side JavaScript will not be able to access the language cookie.
