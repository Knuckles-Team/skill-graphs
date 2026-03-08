This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/logging/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/logging/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/logging/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/logging/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/logging/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/logging/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/logging/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/logging/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/logging/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/logging/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/logging/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/logging/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/logging/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/logging/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/logging/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/logging/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/logging/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/logging/)


  * [](https://docs.djangoproject.com/en/5.0/ref/logging/#top)


# Logging[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#logging "Link to this heading")
See also
  * [How to configure and use logging](https://docs.djangoproject.com/en/5.0/howto/logging/#logging-how-to)
  * [Django logging overview](https://docs.djangoproject.com/en/5.0/topics/logging/#logging-explanation)


Django’s logging module extends Python’s builtin
Logging is configured as part of the general Django [`django.setup()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.setup "django.setup") function, so it’s always available unless explicitly disabled.
## Django’s default logging configuration[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django-s-default-logging-configuration "Link to this heading")
By default, Django uses Python’s
### Default logging conditions[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#default-logging-conditions "Link to this heading")
The full set of default logging conditions are:
When [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is `True`:
  * The `django` logger sends messages in the `django` hierarchy (except `django.server`) at the `INFO` level or higher to the console.


When [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is `False`:
  * The `django` logger sends messages in the `django` hierarchy (except `django.server`) with `ERROR` or `CRITICAL` level to [`AdminEmailHandler`](https://docs.djangoproject.com/en/5.0/ref/logging/#django.utils.log.AdminEmailHandler "django.utils.log.AdminEmailHandler").


Independently of the value of [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG):
  * The [django.server](https://docs.djangoproject.com/en/5.0/ref/logging/#django-server-logger) logger sends messages at the `INFO` level or higher to the console.


All loggers except [django.server](https://docs.djangoproject.com/en/5.0/ref/logging/#django-server-logger) propagate logging to their parents, up to the root `django` logger. The `console` and `mail_admins` handlers are attached to the root logger to provide the behavior described above.
Python’s own defaults send records of level `WARNING` and higher to the console.
### Default logging definition[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#default-logging-definition "Link to this heading")
Django’s default logging configuration inherits Python’s defaults. It’s available as `django.utils.log.DEFAULT_LOGGING` and defined in
```
{
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "mail_admins"],
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

```

See [Configuring logging](https://docs.djangoproject.com/en/5.0/topics/logging/#configuring-logging) on how to complement or replace this default logging configuration.
## Django logging extensions[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django-logging-extensions "Link to this heading")
Django provides a number of utilities to handle the particular requirements of logging in a web server environment.
### Loggers[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#loggers "Link to this heading")
Django provides several built-in loggers.
####  `django`[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django "Link to this heading")
The parent logger for messages in the `django` [named logger hierarchy](https://docs.djangoproject.com/en/5.0/howto/logging/#naming-loggers-hierarchy). Django does not post messages using this name. Instead, it uses one of the loggers below.
####  `django.request`[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django-request "Link to this heading")
Log messages related to the handling of requests. 5XX responses are raised as `ERROR` messages; 4XX responses are raised as `WARNING` messages. Requests that are logged to the `django.security` logger aren’t logged to `django.request`.
Messages to this logger have the following extra context:
  * `status_code`: The HTTP response code associated with the request.
  * `request`: The request object that generated the logging message.


####  `django.server`[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django-server "Link to this heading")
Log messages related to the handling of requests received by the server invoked by the [`runserver`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-runserver) command. HTTP 5XX responses are logged as `ERROR` messages, 4XX responses are logged as `WARNING` messages, and everything else is logged as `INFO`.
Messages to this logger have the following extra context:
  * `status_code`: The HTTP response code associated with the request.
  * `request`: The request object (a


####  `django.template`[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django-template "Link to this heading")
Log messages related to the rendering of templates.
  * Missing context variables are logged as `DEBUG` messages.


####  `django.db.backends`[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django-db-backends "Link to this heading")
Messages relating to the interaction of code with the database. For example, every application-level SQL statement executed by a request is logged at the `DEBUG` level to this logger.
Messages to this logger have the following extra context:
  * `duration`: The time taken to execute the SQL statement.
  * `sql`: The SQL statement that was executed.
  * `params`: The parameters that were used in the SQL call.
  * `alias`: The alias of the database used in the SQL call.


For performance reasons, SQL logging is only enabled when `settings.DEBUG` is set to `True`, regardless of the logging level or handlers that are installed.
This logging does not include framework-level initialization (e.g. `SET TIMEZONE`). Turn on query logging in your database if you wish to view all database queries.
Changed in Django 4.2:
Support for logging transaction management queries (`BEGIN`, `COMMIT`, and `ROLLBACK`) was added.
####  `django.utils.autoreload`[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django-utils-autoreload "Link to this heading")
Log messages related to automatic code reloading during the execution of the Django development server. This logger generates an `INFO` message upon detecting a modification in a source code file and may produce `WARNING` messages during filesystem inspection and event subscription processes.
####  `django.contrib.auth`[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django-contrib-auth "Link to this heading")
New in Django 4.2.16.
Log messages related to [django.contrib.auth](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/), particularly `ERROR` messages are generated when a [`PasswordResetForm`](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.forms.PasswordResetForm "django.contrib.auth.forms.PasswordResetForm") is successfully submitted but the password reset email cannot be delivered due to a mail sending exception.
####  `django.contrib.gis`[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django-contrib-gis "Link to this heading")
Log messages related to [GeoDjango](https://docs.djangoproject.com/en/5.0/ref/contrib/gis/) at various points: during the loading of external GeoSpatial libraries (GEOS, GDAL, etc.) and when reporting errors. Each `ERROR` log record includes the caught exception and relevant contextual data.
####  `django.dispatch`[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django-dispatch "Link to this heading")
This logger is used in [Signals](https://docs.djangoproject.com/en/5.0/ref/signals/), specifically within the [`Signal`](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal "django.dispatch.Signal") class, to report issues when dispatching a signal to a connected receiver. The `ERROR` log record includes the caught exception as `exc_info` and adds the following extra context:
  * `receiver`: The name of the receiver.
  * `err`: The exception that occurred when calling the receiver.


####  `django.security.*`[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django-security "Link to this heading")
The security loggers will receive messages on any occurrence of [`SuspiciousOperation`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation") and other security-related errors. There is a sub-logger for each subtype of security error, including all `SuspiciousOperation`s. The level of the log event depends on where the exception is handled. Most occurrences are logged as a warning, while any `SuspiciousOperation` that reaches the WSGI handler will be logged as an error. For example, when an HTTP `Host` header is included in a request from a client that does not match [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ALLOWED_HOSTS), Django will return a 400 response, and an error message will be logged to the `django.security.DisallowedHost` logger.
These log events will reach the `django` logger by default, which mails error events to admins when `DEBUG=False`. Requests resulting in a 400 response due to a `SuspiciousOperation` will not be logged to the `django.request` logger, but only to the `django.security` logger.
To silence a particular type of `SuspiciousOperation`, you can override that specific logger following this example:
```
LOGGING = {
    # ...
    "handlers": {
        "null": {
            "class": "logging.NullHandler",
        },
    },
    "loggers": {
        "django.security.DisallowedHost": {
            "handlers": ["null"],
            "propagate": False,
        },
    },
    # ...
}

```

Other `django.security` loggers not based on `SuspiciousOperation` are:
  * `django.security.csrf`: For [CSRF failures](https://docs.djangoproject.com/en/5.0/howto/csrf/#csrf-rejected-requests).


####  `django.db.backends.schema`[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django-db-backends-schema "Link to this heading")
Logs the SQL queries that are executed during schema changes to the database by the [migrations framework](https://docs.djangoproject.com/en/5.0/topics/migrations/). Note that it won’t log the queries executed by [`RunPython`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RunPython "django.db.migrations.operations.RunPython"). Messages to this logger have `params` and `sql` in their extra context (but unlike `django.db.backends`, not duration). The values have the same meaning as explained in [django.db.backends](https://docs.djangoproject.com/en/5.0/ref/logging/#django-db-logger).
### Handlers[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#handlers "Link to this heading")
Django provides one log handler in addition to

_class_ AdminEmailHandler(_include_html =False_, _email_backend =None_, _reporter_class =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/log/#AdminEmailHandler)[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django.utils.log.AdminEmailHandler "Link to this definition")

This handler sends an email to the site [`ADMINS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ADMINS) for each log message it receives.
If the log record contains a `request` attribute, the full details of the request will be included in the email. The email subject will include the phrase “internal IP” if the client’s IP address is in the [`INTERNAL_IPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INTERNAL_IPS) setting; if not, it will include “EXTERNAL IP”.
If the log record contains stack trace information, that stack trace will be included in the email.
The `include_html` argument of `AdminEmailHandler` is used to control whether the traceback email includes an HTML attachment containing the full content of the debug web page that would have been produced if [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) were `True`. To set this value in your configuration, include it in the handler definition for `django.utils.log.AdminEmailHandler`, like this:
```
"handlers": {
    "mail_admins": {
        "level": "ERROR",
        "class": "django.utils.log.AdminEmailHandler",
        "include_html": True,
    },
}

```

Be aware of the [security implications of logging](https://docs.djangoproject.com/en/5.0/topics/logging/#logging-security-implications) when using the `AdminEmailHandler`.
By setting the `email_backend` argument of `AdminEmailHandler`, the [email backend](https://docs.djangoproject.com/en/5.0/topics/email/#topic-email-backends) that is being used by the handler can be overridden, like this:
```
"handlers": {
    "mail_admins": {
        "level": "ERROR",
        "class": "django.utils.log.AdminEmailHandler",
        "email_backend": "django.core.mail.backends.filebased.EmailBackend",
    },
}

```

By default, an instance of the email backend specified in [`EMAIL_BACKEND`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-EMAIL_BACKEND) will be used.
The `reporter_class` argument of `AdminEmailHandler` allows providing an `django.views.debug.ExceptionReporter` subclass to customize the traceback text sent in the email body. You provide a string import path to the class you wish to use, like this:
```
"handlers": {
    "mail_admins": {
        "level": "ERROR",
        "class": "django.utils.log.AdminEmailHandler",
        "include_html": True,
        "reporter_class": "somepackage.error_reporter.CustomErrorReporter",
    },
}

```


send_mail(_subject_ , _message_ , _* args_, _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/log/#AdminEmailHandler.send_mail)[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django.utils.log.AdminEmailHandler.send_mail "Link to this definition")

Sends emails to admin users. To customize this behavior, you can subclass the [`AdminEmailHandler`](https://docs.djangoproject.com/en/5.0/ref/logging/#django.utils.log.AdminEmailHandler "django.utils.log.AdminEmailHandler") class and override this method.
### Filters[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#filters "Link to this heading")
Django provides some log filters in addition to those provided by the Python logging module.

_class_ CallbackFilter(_callback_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/log/#CallbackFilter)[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django.utils.log.CallbackFilter "Link to this definition")

This filter accepts a callback function (which should accept a single argument, the record to be logged), and calls it for each record that passes through the filter. Handling of that record will not proceed if the callback returns False.
For instance, to filter out [`UnreadablePostError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.http.UnreadablePostError "django.http.UnreadablePostError") (raised when a user cancels an upload) from the admin emails, you would create a filter function:
```
from django.http import UnreadablePostError


def skip_unreadable_post(record):
    if record.exc_info:
        exc_type, exc_value = record.exc_info[:2]
        if isinstance(exc_value, UnreadablePostError):
            return False
    return True

```

and then add it to your logging config:
```
LOGGING = {
    # ...
    "filters": {
        "skip_unreadable_posts": {
            "()": "django.utils.log.CallbackFilter",
            "callback": skip_unreadable_post,
        },
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["skip_unreadable_posts"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    # ...
}

```


_class_ RequireDebugFalse[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/log/#RequireDebugFalse)[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django.utils.log.RequireDebugFalse "Link to this definition")

This filter will only pass on records when settings.DEBUG is False.
This filter is used as follows in the default [`LOGGING`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LOGGING) configuration to ensure that the [`AdminEmailHandler`](https://docs.djangoproject.com/en/5.0/ref/logging/#django.utils.log.AdminEmailHandler "django.utils.log.AdminEmailHandler") only sends error emails to admins when [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is `False`:
```
LOGGING = {
    # ...
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    # ...
}

```


_class_ RequireDebugTrue[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/log/#RequireDebugTrue)[¶](https://docs.djangoproject.com/en/5.0/ref/logging/#django.utils.log.RequireDebugTrue "Link to this definition")

This filter is similar to [`RequireDebugFalse`](https://docs.djangoproject.com/en/5.0/ref/logging/#django.utils.log.RequireDebugFalse "django.utils.log.RequireDebugFalse"), except that records are passed only when [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is `True`. Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/forms/validation/)
[Middleware ](https://docs.djangoproject.com/en/5.0/ref/middleware/)
[](https://docs.djangoproject.com/en/5.0/ref/logging/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Tampa Personal Injury Lawyer donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Logging](https://docs.djangoproject.com/en/5.0/ref/logging/)
    * [Django’s default logging configuration](https://docs.djangoproject.com/en/5.0/ref/logging/#django-s-default-logging-configuration)
      * [Default logging conditions](https://docs.djangoproject.com/en/5.0/ref/logging/#default-logging-conditions)
      * [Default logging definition](https://docs.djangoproject.com/en/5.0/ref/logging/#default-logging-definition)
    * [Django logging extensions](https://docs.djangoproject.com/en/5.0/ref/logging/#django-logging-extensions)
      * [Loggers](https://docs.djangoproject.com/en/5.0/ref/logging/#loggers)
        * [`django`](https://docs.djangoproject.com/en/5.0/ref/logging/#django)
        * [`django.request`](https://docs.djangoproject.com/en/5.0/ref/logging/#django-request)
        * [`django.server`](https://docs.djangoproject.com/en/5.0/ref/logging/#django-server)
        * [`django.template`](https://docs.djangoproject.com/en/5.0/ref/logging/#django-template)
        * [`django.db.backends`](https://docs.djangoproject.com/en/5.0/ref/logging/#django-db-backends)
        * [`django.utils.autoreload`](https://docs.djangoproject.com/en/5.0/ref/logging/#django-utils-autoreload)
        * [`django.contrib.auth`](https://docs.djangoproject.com/en/5.0/ref/logging/#django-contrib-auth)
        * [`django.contrib.gis`](https://docs.djangoproject.com/en/5.0/ref/logging/#django-contrib-gis)
        * [`django.dispatch`](https://docs.djangoproject.com/en/5.0/ref/logging/#django-dispatch)
        * [`django.security.*`](https://docs.djangoproject.com/en/5.0/ref/logging/#django-security)
        * [`django.db.backends.schema`](https://docs.djangoproject.com/en/5.0/ref/logging/#django-db-backends-schema)
      * [Handlers](https://docs.djangoproject.com/en/5.0/ref/logging/#handlers)
      * [Filters](https://docs.djangoproject.com/en/5.0/ref/logging/#filters)


### Browse
  * Prev: [Form and field validation](https://docs.djangoproject.com/en/5.0/ref/forms/validation/)
  * Next: [Middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * Logging


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
