This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/settings/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/settings/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/settings/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/settings/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/settings/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/settings/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/settings/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/settings/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/settings/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/settings/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/settings/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/settings/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/settings/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/settings/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/settings/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/settings/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/settings/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/settings/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/settings/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/settings/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/settings/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/settings/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/settings/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/settings/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/settings/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/settings/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/settings/)


  * [](https://docs.djangoproject.com/en/5.0/topics/settings/#top)


# Django settings[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#django-settings "Link to this heading")
A Django settings file contains all the configuration of your Django installation. This document explains how settings work and which settings are available.
## The basics[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#the-basics "Link to this heading")
A settings file is just a Python module with module-level variables.
Here are a couple of example settings:
```
ALLOWED_HOSTS = ["www.example.com"]
DEBUG = False
DEFAULT_FROM_EMAIL = "webmaster@example.com"

```

Note
If you set [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) to `False`, you also need to properly set the [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ALLOWED_HOSTS) setting.
Because a settings file is a Python module, the following apply:
  * It doesn’t allow for Python syntax errors.
  * It can assign settings dynamically using normal Python syntax. For example:
```
MY_SETTING = [str(i) for i in range(30)]

```

  * It can import values from other settings files.


## Designating the settings[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#designating-the-settings "Link to this heading")

DJANGO_SETTINGS_MODULE[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE "Link to this definition")

When you use Django, you have to tell it which settings you’re using. Do this by using an environment variable, [`DJANGO_SETTINGS_MODULE`](https://docs.djangoproject.com/en/5.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE).
The value of [`DJANGO_SETTINGS_MODULE`](https://docs.djangoproject.com/en/5.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE) should be in Python path syntax, e.g. `mysite.settings`. Note that the settings module should be on the Python
### The `django-admin` utility[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#the-django-admin-utility "Link to this heading")
When using [django-admin](https://docs.djangoproject.com/en/5.0/ref/django-admin/), you can either set the environment variable once, or explicitly pass in the settings module each time you run the utility.
Example (Unix Bash shell):
```
export DJANGO_SETTINGS_MODULE=mysite.settings
django-admin runserver

```

Example (Windows shell):
```
set DJANGO_SETTINGS_MODULE=mysite.settings
django-admin runserver

```

Use the `--settings` command-line argument to specify the settings manually:
```
django-admin runserver --settings=mysite.settings

```

### On the server (`mod_wsgi`)[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#on-the-server-mod-wsgi "Link to this heading")
In your live server environment, you’ll need to tell your WSGI application what settings file to use. Do that with `os.environ`:
```
import os

os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"

```

Read the [Django mod_wsgi documentation](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/modwsgi/) for more information and other common elements to a Django WSGI application.
## Default settings[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#default-settings "Link to this heading")
A Django settings file doesn’t have to define any settings if it doesn’t need to. Each setting has a sensible default value. These defaults live in the module
Here’s the algorithm Django uses in compiling settings:
  * Load settings from `global_settings.py`.
  * Load settings from the specified settings file, overriding the global settings as necessary.


Note that a settings file should _not_ import from `global_settings`, because that’s redundant.
### Seeing which settings you’ve changed[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#seeing-which-settings-you-ve-changed "Link to this heading")
The command `python manage.py diffsettings` displays differences between the current settings file and Django’s default settings.
For more, see the [`diffsettings`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-diffsettings) documentation.
## Using settings in Python code[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#using-settings-in-python-code "Link to this heading")
In your Django apps, use settings by importing the object `django.conf.settings`. Example:
```
from django.conf import settings

if settings.DEBUG:
    # Do something
    ...

```

Note that `django.conf.settings` isn’t a module – it’s an object. So importing individual settings is not possible:
```
from django.conf.settings import DEBUG  # This won't work.

```

Also note that your code should _not_ import from either `global_settings` or your own settings file. `django.conf.settings` abstracts the concepts of default settings and site-specific settings; it presents a single interface. It also decouples the code that uses settings from the location of your settings.
## Altering settings at runtime[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#altering-settings-at-runtime "Link to this heading")
You shouldn’t alter settings in your applications at runtime. For example, don’t do this in a view:
```
from django.conf import settings

settings.DEBUG = True  # Don't do this!

```

The only place you should assign to settings is in a settings file.
## Security[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#security "Link to this heading")
Because a settings file contains sensitive information, such as the database password, you should make every attempt to limit access to it. For example, change its file permissions so that only you and your web server’s user can read it. This is especially important in a shared-hosting environment.
## Available settings[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#available-settings "Link to this heading")
For a full list of available settings, see the [settings reference](https://docs.djangoproject.com/en/5.0/ref/settings/).
## Creating your own settings[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#creating-your-own-settings "Link to this heading")
There’s nothing stopping you from creating your own settings, for your own Django apps, but follow these guidelines:
  * Setting names must be all uppercase.
  * Don’t reinvent an already-existing setting.


For settings that are sequences, Django itself uses lists, but this is only a convention.
## Using settings without setting [`DJANGO_SETTINGS_MODULE`](https://docs.djangoproject.com/en/5.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE)[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#using-settings-without-setting-django-settings-module "Link to this heading")
In some cases, you might want to bypass the [`DJANGO_SETTINGS_MODULE`](https://docs.djangoproject.com/en/5.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE) environment variable. For example, if you’re using the template system by itself, you likely don’t want to have to set up an environment variable pointing to a settings module.
In these cases, you can configure Django’s settings manually. Do this by calling:

django.conf.settings.configure(_default_settings_ , _** settings_)[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#django.conf.settings.configure "Link to this definition")

Example:
```
from django.conf import settings

settings.configure(DEBUG=True)

```

Pass `configure()` as many keyword arguments as you’d like, with each keyword argument representing a setting and its value. Each argument name should be all uppercase, with the same name as the settings described above. If a particular setting is not passed to `configure()` and is needed at some later point, Django will use the default setting value.
Configuring Django in this fashion is mostly necessary – and, indeed, recommended – when you’re using a piece of the framework inside a larger application.
Consequently, when configured via `settings.configure()`, Django will not make any modifications to the process environment variables (see the documentation of [`TIME_ZONE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_ZONE) for why this would normally occur). It’s assumed that you’re already in full control of your environment in these cases.
### Custom default settings[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#custom-default-settings "Link to this heading")
If you’d like default values to come from somewhere other than `django.conf.global_settings`, you can pass in a module or class that provides the default settings as the `default_settings` argument (or as the first positional argument) in the call to `configure()`.
In this example, default settings are taken from `myapp_defaults`, and the [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) setting is set to `True`, regardless of its value in `myapp_defaults`:
```
from django.conf import settings
from myapp import myapp_defaults

settings.configure(default_settings=myapp_defaults, DEBUG=True)

```

The following example, which uses `myapp_defaults` as a positional argument, is equivalent:
```
settings.configure(myapp_defaults, DEBUG=True)

```

Normally, you will not need to override the defaults in this fashion. The Django defaults are sufficiently tame that you can safely use them. Be aware that if you do pass in a new default module, it entirely _replaces_ the Django defaults, so you must specify a value for every possible setting that might be used in the code you are importing. Check in `django.conf.settings.global_settings` for the full list.
### Either `configure()` or [`DJANGO_SETTINGS_MODULE`](https://docs.djangoproject.com/en/5.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE) is required[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#either-configure-or-django-settings-module-is-required "Link to this heading")
If you’re not setting the [`DJANGO_SETTINGS_MODULE`](https://docs.djangoproject.com/en/5.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE) environment variable, you _must_ call `configure()` at some point before using any code that reads settings.
If you don’t set [`DJANGO_SETTINGS_MODULE`](https://docs.djangoproject.com/en/5.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE) and don’t call `configure()`, Django will raise an `ImportError` exception the first time a setting is accessed.
If you set [`DJANGO_SETTINGS_MODULE`](https://docs.djangoproject.com/en/5.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE), access settings values somehow, _then_ call `configure()`, Django will raise a `RuntimeError` indicating that settings have already been configured. There is a property for this purpose:

django.conf.settings.configured[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#django.conf.settings.configured "Link to this definition")

For example:
```
from django.conf import settings

if not settings.configured:
    settings.configure(myapp_defaults, DEBUG=True)

```

Also, it’s an error to call `configure()` more than once, or to call `configure()` after any setting has been accessed.
It boils down to this: Use exactly one of either `configure()` or [`DJANGO_SETTINGS_MODULE`](https://docs.djangoproject.com/en/5.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE). Not both, and not neither.
### Calling `django.setup()` is required for “standalone” Django usage[¶](https://docs.djangoproject.com/en/5.0/topics/settings/#calling-django-setup-is-required-for-standalone-django-usage "Link to this heading")
If you’re using components of Django “standalone” – for example, writing a Python script which loads some Django templates and renders them, or uses the ORM to fetch some data – there’s one more step you’ll need in addition to configuring settings.
After you’ve either set [`DJANGO_SETTINGS_MODULE`](https://docs.djangoproject.com/en/5.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE) or called `configure()`, you’ll need to call [`django.setup()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.setup "django.setup") to load your settings and populate Django’s application registry. For example:
```
import django
from django.conf import settings
from myapp import myapp_defaults

settings.configure(default_settings=myapp_defaults, DEBUG=True)
django.setup()

# Now this script or any imported module can use any part of Django it needs.
from myapp import models

```

Note that calling `django.setup()` is only necessary if your code is truly standalone. When invoked by your web server, or through [django-admin](https://docs.djangoproject.com/en/5.0/ref/django-admin/), Django will handle this for you.
`django.setup()` may only be called once.
Therefore, avoid putting reusable application logic in standalone scripts so that you have to import from the script elsewhere in your application. If you can’t avoid that, put the call to `django.setup()` inside an `if` block:
```
if __name__ == "__main__":
    import django

    django.setup()

```

See also

[The Settings Reference](https://docs.djangoproject.com/en/5.0/ref/settings/)

Contains the complete list of core and contrib app settings.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/serialization/)
[Signals ](https://docs.djangoproject.com/en/5.0/topics/signals/)
[](https://docs.djangoproject.com/en/5.0/topics/settings/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ AdNabu Inc donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Django settings](https://docs.djangoproject.com/en/5.0/topics/settings/)
    * [The basics](https://docs.djangoproject.com/en/5.0/topics/settings/#the-basics)
    * [Designating the settings](https://docs.djangoproject.com/en/5.0/topics/settings/#designating-the-settings)
      * [The `django-admin` utility](https://docs.djangoproject.com/en/5.0/topics/settings/#the-django-admin-utility)
      * [On the server (`mod_wsgi`)](https://docs.djangoproject.com/en/5.0/topics/settings/#on-the-server-mod-wsgi)
    * [Default settings](https://docs.djangoproject.com/en/5.0/topics/settings/#default-settings)
      * [Seeing which settings you’ve changed](https://docs.djangoproject.com/en/5.0/topics/settings/#seeing-which-settings-you-ve-changed)
    * [Using settings in Python code](https://docs.djangoproject.com/en/5.0/topics/settings/#using-settings-in-python-code)
    * [Altering settings at runtime](https://docs.djangoproject.com/en/5.0/topics/settings/#altering-settings-at-runtime)
    * [Security](https://docs.djangoproject.com/en/5.0/topics/settings/#security)
    * [Available settings](https://docs.djangoproject.com/en/5.0/topics/settings/#available-settings)
    * [Creating your own settings](https://docs.djangoproject.com/en/5.0/topics/settings/#creating-your-own-settings)
    * [Using settings without setting `DJANGO_SETTINGS_MODULE`](https://docs.djangoproject.com/en/5.0/topics/settings/#using-settings-without-setting-django-settings-module)
      * [Custom default settings](https://docs.djangoproject.com/en/5.0/topics/settings/#custom-default-settings)
      * [Either `configure()` or `DJANGO_SETTINGS_MODULE` is required](https://docs.djangoproject.com/en/5.0/topics/settings/#either-configure-or-django-settings-module-is-required)
      * [Calling `django.setup()` is required for “standalone” Django usage](https://docs.djangoproject.com/en/5.0/topics/settings/#calling-django-setup-is-required-for-standalone-django-usage)


### Browse
  * Prev: [Serializing Django objects](https://docs.djangoproject.com/en/5.0/topics/serialization/)
  * Next: [Signals](https://docs.djangoproject.com/en/5.0/topics/signals/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * Django settings


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
