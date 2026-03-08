This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/logging/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/logging/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/logging/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/logging/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/logging/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/logging/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/logging/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/logging/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/logging/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/logging/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/logging/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/logging/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/logging/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/logging/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/logging/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/logging/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/logging/)
  * [4.0](https://docs.djangoproject.com/en/4.0/howto/logging/)


  * [](https://docs.djangoproject.com/en/5.0/howto/logging/#top)


# How to configure and use logging[¶](https://docs.djangoproject.com/en/5.0/howto/logging/#how-to-configure-and-use-logging "Link to this heading")
See also
  * [Django logging reference](https://docs.djangoproject.com/en/5.0/ref/logging/#logging-ref)
  * [Django logging overview](https://docs.djangoproject.com/en/5.0/topics/logging/#logging-explanation)


Django provides a working [default logging configuration](https://docs.djangoproject.com/en/5.0/ref/logging/#default-logging-configuration) that is readily extended.
## Make a basic logging call[¶](https://docs.djangoproject.com/en/5.0/howto/logging/#make-a-basic-logging-call "Link to this heading")
To send a log message from within your code, you place a logging call into it.
Don’t be tempted to use logging calls in `settings.py`.
The way that Django logging is configured as part of the `setup()` function means that logging calls placed in `settings.py` may not work as expected, because _logging will not be set up at that point_. To explore logging, use a view function as suggested in the example below.
First, import the Python logging library, and then obtain a logger instance with `getLogger()` method with a name to identify it and the records it emits. A good option is to use `__name__` (see [Use logger namespacing](https://docs.djangoproject.com/en/5.0/howto/logging/#naming-loggers) below for more on this) which will provide the name of the current Python module as a dotted path:
```
import logging

logger = logging.getLogger(__name__)

```

It’s a good convention to perform this declaration at module level.
And then in a function, for example in a view, send a record to the logger:
```
def some_view(request):
    ...
    if some_risky_state:
        logger.warning("Platform is running at risk")

```

When this code is executed, a
The `WARNING` level used in the example above is one of several [logging severity levels](https://docs.djangoproject.com/en/5.0/topics/logging/#topic-logging-parts-loggers): `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`. So, another example might be:
```
logger.critical("Payment system is not responding")

```

Important
Records with a level lower than `WARNING` will not appear in the console by default. Changing this behavior requires additional configuration.
## Customize logging configuration[¶](https://docs.djangoproject.com/en/5.0/howto/logging/#customize-logging-configuration "Link to this heading")
Although Django’s logging configuration works out of the box, you can control exactly how your logs are sent to various destinations - to log files, external services, email and so on - with some additional configuration.
You can configure:
  * logger mappings, to determine which records are sent to which handlers
  * handlers, to determine what they do with the records they receive
  * filters, to provide additional control over the transfer of records, and even modify records in-place
  * formatters, to convert


There are various ways of configuring logging. In Django, the [`LOGGING`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LOGGING) setting is most commonly used. The setting uses the [default logging configuration](https://docs.djangoproject.com/en/5.0/ref/logging/#default-logging-definition).
See [Configuring logging](https://docs.djangoproject.com/en/5.0/topics/logging/#configuring-logging) for an explanation of how your custom settings are merged with Django’s defaults.
See the `LOGGING` setting.
### Basic logging configuration[¶](https://docs.djangoproject.com/en/5.0/howto/logging/#basic-logging-configuration "Link to this heading")
When configuring logging, it makes sense to
#### Create a `LOGGING` dictionary[¶](https://docs.djangoproject.com/en/5.0/howto/logging/#create-a-logging-dictionary "Link to this heading")
In your `settings.py`:
```
LOGGING = {
    "version": 1,  # the dictConfig format version
    "disable_existing_loggers": False,  # retain the default loggers
}

```

It nearly always makes sense to retain and extend the default logging configuration by setting `disable_existing_loggers` to `False`.
#### Configure a handler[¶](https://docs.djangoproject.com/en/5.0/howto/logging/#configure-a-handler "Link to this heading")
This example configures a single handler named `file`, that uses Python’s `DEBUG` and higher to the file `general.log` (at the project root):
```
LOGGING = {
    # ...
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "general.log",
        },
    },
}

```

Different handler classes take different configuration options. For more information on available handler classes, see the [`AdminEmailHandler`](https://docs.djangoproject.com/en/5.0/ref/logging/#django.utils.log.AdminEmailHandler "django.utils.log.AdminEmailHandler") provided by Django and the various
Logging levels can also be set on the handlers (by default, they accept log messages of all levels). Using the example above, adding:
```
{
    "class": "logging.FileHandler",
    "filename": "general.log",
    "level": "DEBUG",
}

```

would define a handler configuration that only accepts records of level `DEBUG` and higher.
#### Configure a logger mapping[¶](https://docs.djangoproject.com/en/5.0/howto/logging/#configure-a-logger-mapping "Link to this heading")
To send records to this handler, configure a logger mapping to use it for example:
```
LOGGING = {
    # ...
    "loggers": {
        "": {
            "level": "DEBUG",
            "handlers": ["file"],
        },
    },
}

```

The mapping’s name determines which log records it will process. This configuration (`''`) is _unnamed_. That means that it will process records from _all_ loggers (see [Use logger namespacing](https://docs.djangoproject.com/en/5.0/howto/logging/#naming-loggers) below on how to use the mapping name to determine the loggers for which it will process records).
It will forward messages of levels `DEBUG` and higher to the handler named `file`.
Note that a logger can forward messages to multiple handlers, so the relation between loggers and handlers is many-to-many.
If you execute:
```
logger.debug("Attempting to connect to API")

```

in your code, you will find that message in the file `general.log` in the root of the project.
#### Configure a formatter[¶](https://docs.djangoproject.com/en/5.0/howto/logging/#configure-a-formatter "Link to this heading")
By default, the final log output contains the message part of each `verbose` and `simple`:
```
LOGGING = {
    # ...
    "formatters": {
        "verbose": {
            "format": "{name} {levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
}

```

The `style` keyword allows you to specify `{` for `$` for `$`.
See
To apply a formatter to a handler, add a `formatter` entry to the handler’s dictionary referring to the formatter by name, for example:
```
"handlers": {
    "file": {
        "class": "logging.FileHandler",
        "filename": "general.log",
        "formatter": "verbose",
    },
}

```

#### Use logger namespacing[¶](https://docs.djangoproject.com/en/5.0/howto/logging/#use-logger-namespacing "Link to this heading")
The unnamed logging configuration `''` captures logs from any Python application. A named logging configuration will capture logs only from loggers with matching names.
The namespace of a logger instance is defined using `views.py` of `my_app`:
```
logger = logging.getLogger(__name__)

```

will create a logger in the `my_app.views` namespace. `__name__` allows you to organize log messages according to their provenance within your project’s applications automatically. It also ensures that you will not experience name collisions.
A logger mapping named `my_app.views` will capture records from this logger:
```
LOGGING = {
    # ...
    "loggers": {
        "my_app.views": {...},
    },
}

```

A logger mapping named `my_app` will be more permissive, capturing records from loggers anywhere within the `my_app` namespace (including `my_app.views`, `my_app.utils`, and so on):
```
LOGGING = {
    # ...
    "loggers": {
        "my_app": {...},
    },
}

```

You can also define logger namespacing explicitly:
```
logger = logging.getLogger("project.payment")

```

and set up logger mappings accordingly.
##### Using logger hierarchies and propagation[¶](https://docs.djangoproject.com/en/5.0/howto/logging/#using-logger-hierarchies-and-propagation "Link to this heading")
Logger naming is _hierarchical_. `my_app` is the parent of `my_app.views`, which is the parent of `my_app.views.private`. Unless specified otherwise, logger mappings will propagate the records they process to their parents - a record from a logger in the `my_app.views.private` namespace will be handled by a mapping for both `my_app` and `my_app.views`.
To manage this behavior, set the propagation key on the mappings you define:
```
LOGGING = {
    # ...
    "loggers": {
        "my_app": {
            # ...
        },
        "my_app.views": {
            # ...
        },
        "my_app.views.private": {
            # ...
            "propagate": False,
        },
    },
}

```

`propagate` defaults to `True`. In this example, the logs from `my_app.views.private` will not be handled by the parent, but logs from `my_app.views` will.
### Configure responsive logging[¶](https://docs.djangoproject.com/en/5.0/howto/logging/#configure-responsive-logging "Link to this heading")
Logging is most useful when it contains as much information as possible, but not information that you don’t need - and how much you need depends upon what you’re doing. When you’re debugging, you need a level of information that would be excessive and unhelpful if you had to deal with it in production.
You can configure logging to provide you with the level of detail you need, when you need it. Rather than manually change configuration to achieve this, a better way is to apply configuration automatically according to the environment.
For example, you could set an environment variable `DJANGO_LOG_LEVEL` appropriately in your development and staging environments, and make use of it in a logger mapping thus:
```
"level": os.getenv("DJANGO_LOG_LEVEL", "WARNING")

```

- so that unless the environment specifies a lower log level, this configuration will only forward records of severity `WARNING` and above to its handler.
Other options in the configuration (such as the `level` or `formatter` option of handlers) can be similarly managed.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/)
[How to create CSV output ](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/)
[](https://docs.djangoproject.com/en/5.0/howto/logging/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Omar Ghoneim donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to configure and use logging](https://docs.djangoproject.com/en/5.0/howto/logging/)
    * [Make a basic logging call](https://docs.djangoproject.com/en/5.0/howto/logging/#make-a-basic-logging-call)
    * [Customize logging configuration](https://docs.djangoproject.com/en/5.0/howto/logging/#customize-logging-configuration)
      * [Basic logging configuration](https://docs.djangoproject.com/en/5.0/howto/logging/#basic-logging-configuration)
        * [Create a `LOGGING` dictionary](https://docs.djangoproject.com/en/5.0/howto/logging/#create-a-logging-dictionary)
        * [Configure a handler](https://docs.djangoproject.com/en/5.0/howto/logging/#configure-a-handler)
        * [Configure a logger mapping](https://docs.djangoproject.com/en/5.0/howto/logging/#configure-a-logger-mapping)
        * [Configure a formatter](https://docs.djangoproject.com/en/5.0/howto/logging/#configure-a-formatter)
        * [Use logger namespacing](https://docs.djangoproject.com/en/5.0/howto/logging/#use-logger-namespacing)
          * [Using logger hierarchies and propagation](https://docs.djangoproject.com/en/5.0/howto/logging/#using-logger-hierarchies-and-propagation)
      * [Configure responsive logging](https://docs.djangoproject.com/en/5.0/howto/logging/#configure-responsive-logging)


### Browse
  * Prev: [How to integrate Django with a legacy database](https://docs.djangoproject.com/en/5.0/howto/legacy-databases/)
  * Next: [How to create CSV output](https://docs.djangoproject.com/en/5.0/howto/outputting-csv/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to configure and use logging


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
