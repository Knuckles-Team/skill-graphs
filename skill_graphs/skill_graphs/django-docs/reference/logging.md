This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/logging/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/logging/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/logging/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/logging/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/logging/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/logging/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/logging/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/logging/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/logging/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/logging/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/logging/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/logging/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/logging/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/logging/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/logging/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/logging/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/logging/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/logging/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/logging/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/logging/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/logging/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/logging/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/logging/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/logging/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/logging/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/logging/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/logging/)


  * [](https://docs.djangoproject.com/en/5.0/topics/logging/#top)


# Logging[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#logging "Link to this heading")
See also
  * [How to configure and use logging](https://docs.djangoproject.com/en/5.0/howto/logging/#logging-how-to)
  * [Django logging reference](https://docs.djangoproject.com/en/5.0/ref/logging/#logging-ref)


Python programmers will often use `print()` in their code as a quick and convenient debugging tool. Using the logging framework is only a little more effort than that, but it’s much more elegant and flexible. As well as being useful for debugging, logging can also provide you with more - and better structured - information about the state and health of your application.
## Overview[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#overview "Link to this heading")
Django uses and extends Python’s builtin
### The cast of players[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#the-cast-of-players "Link to this heading")
A Python logging configuration consists of four parts:
  * [Loggers](https://docs.djangoproject.com/en/5.0/topics/logging/#topic-logging-parts-loggers)
  * [Handlers](https://docs.djangoproject.com/en/5.0/topics/logging/#topic-logging-parts-handlers)
  * [Filters](https://docs.djangoproject.com/en/5.0/topics/logging/#topic-logging-parts-filters)
  * [Formatters](https://docs.djangoproject.com/en/5.0/topics/logging/#topic-logging-parts-formatters)


#### Loggers[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#loggers "Link to this heading")
A _logger_ is the entry point into the logging system. Each logger is a named bucket to which messages can be written for processing.
A logger is configured to have a _log level_. This log level describes the severity of the messages that the logger will handle. Python defines the following log levels:
  * `DEBUG`: Low level system information for debugging purposes
  * `INFO`: General system information
  * `WARNING`: Information describing a minor problem that has occurred.
  * `ERROR`: Information describing a major problem that has occurred.
  * `CRITICAL`: Information describing a critical problem that has occurred.


Each message that is written to the logger is a _Log Record_. Each log record also has a _log level_ indicating the severity of that specific message. A log record can also contain useful metadata that describes the event that is being logged. This can include details such as a stack trace or an error code.
When a message is given to the logger, the log level of the message is compared to the log level of the logger. If the log level of the message meets or exceeds the log level of the logger itself, the message will undergo further processing. If it doesn’t, the message will be ignored.
Once a logger has determined that a message needs to be processed, it is passed to a _Handler_.
#### Handlers[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#handlers "Link to this heading")
The _handler_ is the engine that determines what happens to each message in a logger. It describes a particular logging behavior, such as writing a message to the screen, to a file, or to a network socket.
Like loggers, handlers also have a log level. If the log level of a log record doesn’t meet or exceed the level of the handler, the handler will ignore the message.
A logger can have multiple handlers, and each handler can have a different log level. In this way, it is possible to provide different forms of notification depending on the importance of a message. For example, you could install one handler that forwards `ERROR` and `CRITICAL` messages to a paging service, while a second handler logs all messages (including `ERROR` and `CRITICAL` messages) to a file for later analysis.
#### Filters[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#filters "Link to this heading")
A _filter_ is used to provide additional control over which log records are passed from logger to handler.
By default, any log message that meets log level requirements will be handled. However, by installing a filter, you can place additional criteria on the logging process. For example, you could install a filter that only allows `ERROR` messages from a particular source to be emitted.
Filters can also be used to modify the logging record prior to being emitted. For example, you could write a filter that downgrades `ERROR` log records to `WARNING` records if a particular set of criteria are met.
Filters can be installed on loggers or on handlers; multiple filters can be used in a chain to perform multiple filtering actions.
#### Formatters[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#formatters "Link to this heading")
Ultimately, a log record needs to be rendered as text. _Formatters_ describe the exact format of that text. A formatter usually consists of a Python formatting string containing
## Security implications[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#security-implications "Link to this heading")
The logging system handles potentially sensitive information. For example, the log record may contain information about a web request or a stack trace, while some of the data you collect in your own loggers may also have security implications. You need to be sure you know:
  * what information is collected
  * where it will subsequently be stored
  * how it will be transferred
  * who might have access to it.


To help control the collection of sensitive information, you can explicitly designate certain sensitive information to be filtered out of error reports – read more about how to [filter error reports](https://docs.djangoproject.com/en/5.0/howto/error-reporting/#filtering-error-reports).
###  `AdminEmailHandler`[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#adminemailhandler "Link to this heading")
The built-in [`AdminEmailHandler`](https://docs.djangoproject.com/en/5.0/ref/logging/#django.utils.log.AdminEmailHandler "django.utils.log.AdminEmailHandler") deserves a mention in the context of security. If its `include_html` option is enabled, the email message it sends will contain a full traceback, with names and values of local variables at each level of the stack, plus the values of your Django settings (in other words, the same level of detail that is exposed in a web page when [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is `True`).
It’s generally not considered a good idea to send such potentially sensitive information over email. Consider instead using one of the many third-party services to which detailed logs can be sent to get the best of multiple worlds – the rich information of full tracebacks, clear management of who is notified and has access to the information, and so on.
## Configuring logging[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#configuring-logging "Link to this heading")
Python’s logging library provides several techniques to configure logging, ranging from a programmatic interface to configuration files. By default, Django uses the
In order to configure logging, you use [`LOGGING`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LOGGING) to define a dictionary of logging settings. These settings describe the loggers, handlers, filters and formatters that you want in your logging setup, and the log levels and other properties that you want those components to have.
By default, the [`LOGGING`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LOGGING) setting is merged with [Django’s default logging configuration](https://docs.djangoproject.com/en/5.0/ref/logging/#default-logging-configuration) using the following scheme.
If the `disable_existing_loggers` key in the [`LOGGING`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LOGGING) dictConfig is set to `True` (which is the `dictConfig` default if the key is missing) then all loggers from the default configuration will be disabled. Disabled loggers are not the same as removed; the logger will still exist, but will silently discard anything logged to it, not even propagating entries to a parent logger. Thus you should be very careful using `'disable_existing_loggers': True`; it’s probably not what you want. Instead, you can set `disable_existing_loggers` to `False` and redefine some or all of the default loggers; or you can set [`LOGGING_CONFIG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LOGGING_CONFIG) to `None` and [handle logging config yourself](https://docs.djangoproject.com/en/5.0/topics/logging/#disabling-logging-configuration).
Logging is configured as part of the general Django `setup()` function. Therefore, you can be certain that loggers are always ready for use in your project code.
### Examples[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#examples "Link to this heading")
The full documentation for
To begin, here’s a small configuration that will allow you to output all log messages to the console:
`settings.py`[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#id3 "Link to this code")
```
import os

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}

```

This configures the parent `root` logger to send messages with the `WARNING` level and higher to the console handler. By adjusting the level to `INFO` or `DEBUG` you can display more messages. This may be useful during development.
Next we can add more fine-grained logging. Here’s an example of how to make the logging system print more messages from just the [django](https://docs.djangoproject.com/en/5.0/ref/logging/#django-logger) named logger:
`settings.py`[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#id4 "Link to this code")
```
import os

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}

```

By default, this config sends messages from the `django` logger of level `INFO` or higher to the console. This is the same level as Django’s default logging config, except that the default config only displays log records when `DEBUG=True`. Django does not log many such `INFO` level messages. With this config, however, you can also set the environment variable `DJANGO_LOG_LEVEL=DEBUG` to see all of Django’s debug logging which is very verbose as it includes all database queries.
You don’t have to log to the console. Here’s a configuration which writes all logging from the [django](https://docs.djangoproject.com/en/5.0/ref/logging/#django-logger) named logger to a local file:
`settings.py`[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#id5 "Link to this code")
```
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/path/to/django/debug.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

```

If you use this example, be sure to change the `'filename'` path to a location that’s writable by the user that’s running the Django application.
Finally, here’s an example of a fairly complex logging setup:
`settings.py`[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#id6 "Link to this code")
```
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "filters": {
        "special": {
            "()": "project.logging.SpecialFilter",
            "foo": "bar",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "filters": ["special"],
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "propagate": True,
        },
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
        "myproject.custom": {
            "handlers": ["console", "mail_admins"],
            "level": "INFO",
            "filters": ["special"],
        },
    },
}

```

This logging configuration does the following things:
  * Identifies the configuration as being in ‘dictConfig version 1’ format. At present, this is the only dictConfig format version.
  * Defines two formatters:
    * `simple`, that outputs the log level name (e.g., `DEBUG`) and the log message.
The `format` string is a normal Python formatting string describing the details that are to be output on each logging line. The full list of detail that can be output can be found in
    * `verbose`, that outputs the log level name, the log message, plus the time, process, thread and module that generate the log message.
  * Defines two filters:
    * `project.logging.SpecialFilter`, using the alias `special`. If this filter required additional arguments, they can be provided as additional keys in the filter configuration dictionary. In this case, the argument `foo` will be given a value of `bar` when instantiating `SpecialFilter`.
    * `django.utils.log.RequireDebugTrue`, which passes on records when [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is `True`.
  * Defines two handlers:
    * `console`, a `INFO` (or higher) message to `sys.stderr`. This handler uses the `simple` output format.
    * `mail_admins`, an [`AdminEmailHandler`](https://docs.djangoproject.com/en/5.0/ref/logging/#django.utils.log.AdminEmailHandler "django.utils.log.AdminEmailHandler"), which emails any `ERROR` (or higher) message to the site [`ADMINS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ADMINS). This handler uses the `special` filter.
  * Configures three loggers:
    * `django`, which passes all messages to the `console` handler.
    * `django.request`, which passes all `ERROR` messages to the `mail_admins` handler. In addition, this logger is marked to _not_ propagate messages. This means that log messages written to `django.request` will not be handled by the `django` logger.
    * `myproject.custom`, which passes all messages at `INFO` or higher that also pass the `special` filter to two handlers – the `console`, and `mail_admins`. This means that all `INFO` level messages (or higher) will be printed to the console; `ERROR` and `CRITICAL` messages will also be output via email.


### Custom logging configuration[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#custom-logging-configuration "Link to this heading")
If you don’t want to use Python’s dictConfig format to configure your logger, you can specify your own configuration scheme.
The [`LOGGING_CONFIG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LOGGING_CONFIG) setting defines the callable that will be used to configure Django’s loggers. By default, it points at Python’s [`LOGGING`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LOGGING) will be provided as the value of that argument when logging is configured.
### Disabling logging configuration[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#disabling-logging-configuration "Link to this heading")
If you don’t want to configure logging at all (or you want to manually configure logging using your own approach), you can set [`LOGGING_CONFIG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LOGGING_CONFIG) to `None`. This will disable the configuration process for [Django’s default logging](https://docs.djangoproject.com/en/5.0/ref/logging/#default-logging-configuration).
Setting [`LOGGING_CONFIG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LOGGING_CONFIG) to `None` only means that the automatic configuration process is disabled, not logging itself. If you disable the configuration process, Django will still make logging calls, falling back to whatever default logging behavior is defined.
Here’s an example that disables Django’s logging configuration and then manually configures logging:
`settings.py`[¶](https://docs.djangoproject.com/en/5.0/topics/logging/#id7 "Link to this code")
```
LOGGING_CONFIG = None

import logging.config

logging.config.dictConfig(...)

```

Note that the default configuration process only calls [`LOGGING_CONFIG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LOGGING_CONFIG) once settings are fully-loaded. In contrast, manually configuring the logging in your settings file will load your logging config immediately. As such, your logging config must appear _after_ any settings on which it depends.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/)
[Pagination ](https://docs.djangoproject.com/en/5.0/topics/pagination/)
[](https://docs.djangoproject.com/en/5.0/topics/logging/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Bernhard E. Reiter donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Logging](https://docs.djangoproject.com/en/5.0/topics/logging/)
    * [Overview](https://docs.djangoproject.com/en/5.0/topics/logging/#overview)
      * [The cast of players](https://docs.djangoproject.com/en/5.0/topics/logging/#the-cast-of-players)
        * [Loggers](https://docs.djangoproject.com/en/5.0/topics/logging/#loggers)
        * [Handlers](https://docs.djangoproject.com/en/5.0/topics/logging/#handlers)
        * [Filters](https://docs.djangoproject.com/en/5.0/topics/logging/#filters)
        * [Formatters](https://docs.djangoproject.com/en/5.0/topics/logging/#formatters)
    * [Security implications](https://docs.djangoproject.com/en/5.0/topics/logging/#security-implications)
      * [`AdminEmailHandler`](https://docs.djangoproject.com/en/5.0/topics/logging/#adminemailhandler)
    * [Configuring logging](https://docs.djangoproject.com/en/5.0/topics/logging/#configuring-logging)
      * [Examples](https://docs.djangoproject.com/en/5.0/topics/logging/#examples)
      * [Custom logging configuration](https://docs.djangoproject.com/en/5.0/topics/logging/#custom-logging-configuration)
      * [Disabling logging configuration](https://docs.djangoproject.com/en/5.0/topics/logging/#disabling-logging-configuration)


### Browse
  * Prev: [Time zones](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/)
  * Next: [Pagination](https://docs.djangoproject.com/en/5.0/topics/pagination/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
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
