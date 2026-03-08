This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/static-files/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/static-files/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/static-files/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/static-files/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/static-files/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/static-files/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/static-files/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/static-files/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/static-files/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/static-files/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/static-files/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/static-files/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/static-files/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/static-files/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/static-files/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/static-files/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/static-files/)
  * [4.0](https://docs.djangoproject.com/en/4.0/howto/static-files/)
  * [3.2](https://docs.djangoproject.com/en/3.2/howto/static-files/)
  * [3.1](https://docs.djangoproject.com/en/3.1/howto/static-files/)
  * [3.0](https://docs.djangoproject.com/en/3.0/howto/static-files/)
  * [2.2](https://docs.djangoproject.com/en/2.2/howto/static-files/)
  * [2.1](https://docs.djangoproject.com/en/2.1/howto/static-files/)
  * [2.0](https://docs.djangoproject.com/en/2.0/howto/static-files/)
  * [1.11](https://docs.djangoproject.com/en/1.11/howto/static-files/)
  * [1.10](https://docs.djangoproject.com/en/1.10/howto/static-files/)
  * [1.8](https://docs.djangoproject.com/en/1.8/howto/static-files/)


  * [](https://docs.djangoproject.com/en/5.0/howto/static-files/#top)


# How to manage static files (e.g. images, JavaScript, CSS)[¶](https://docs.djangoproject.com/en/5.0/howto/static-files/#how-to-manage-static-files-e-g-images-javascript-css "Link to this heading")
Websites generally need to serve additional files such as images, JavaScript, or CSS. In Django, we refer to these files as “static files”. Django provides [`django.contrib.staticfiles`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files.") to help you manage them.
This page describes how you can serve these static files.
## Configuring static files[¶](https://docs.djangoproject.com/en/5.0/howto/static-files/#configuring-static-files "Link to this heading")
  1. Make sure that `django.contrib.staticfiles` is included in your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS).
  2. In your settings file, define [`STATIC_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_URL), for example:
```
STATIC_URL = "static/"

```

  3. In your templates, use the [`static`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-static) template tag to build the URL for the given relative path using the configured `staticfiles` [`STORAGES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES) alias.
```
{% load static %}
<img src="{% static 'my_app/example.jpg' %}" alt="My image">

```

  4. Store your static files in a folder called `static` in your app. For example `my_app/static/my_app/example.jpg`.


Serving the files
In addition to these configuration steps, you’ll also need to actually serve the static files.
During development, if you use [`django.contrib.staticfiles`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files."), this will be done automatically by [`runserver`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-runserver) when [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is set to `True` (see [`django.contrib.staticfiles.views.serve()`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django.contrib.staticfiles.views.serve "django.contrib.staticfiles.views.serve")).
This method is **grossly inefficient** and probably **insecure** , so it is **unsuitable for production**.
See [How to deploy static files](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/) for proper strategies to serve static files in production environments.
Your project will probably also have static assets that aren’t tied to a particular app. In addition to using a `static/` directory inside your apps, you can define a list of directories ([`STATICFILES_DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATICFILES_DIRS)) in your settings file where Django will also look for static files. For example:
```
STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/var/www/static/",
]

```

See the documentation for the [`STATICFILES_FINDERS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATICFILES_FINDERS) setting for details on how `staticfiles` finds your files.
Static file namespacing
Now we _might_ be able to get away with putting our static files directly in `my_app/static/` (rather than creating another `my_app` subdirectory), but it would actually be a bad idea. Django will use the first static file it finds whose name matches, and if you had a static file with the same name in a _different_ application, Django would be unable to distinguish between them. We need to be able to point Django at the right one, and the best way to ensure this is by _namespacing_ them. That is, by putting those static files inside _another_ directory named for the application itself.
You can namespace static assets in [`STATICFILES_DIRS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATICFILES_DIRS) by specifying [prefixes](https://docs.djangoproject.com/en/5.0/ref/settings/#staticfiles-dirs-prefixes).
## Serving static files during development[¶](https://docs.djangoproject.com/en/5.0/howto/static-files/#serving-static-files-during-development "Link to this heading")
If you use [`django.contrib.staticfiles`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files.") as explained above, [`runserver`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-runserver) will do this automatically when [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is set to `True`. If you don’t have `django.contrib.staticfiles` in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS), you can still manually serve static files using the [`django.views.static.serve()`](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.static.serve "django.views.static.serve") view.
This is not suitable for production use! For some common deployment strategies, see [How to deploy static files](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/).
For example, if your [`STATIC_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_URL) is defined as `static/`, you can do this by adding the following snippet to your `urls.py`:
```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

```

Note
This helper function works only in debug mode and only if the given prefix is local (e.g. `static/`) and not a URL (e.g. `http://static.example.com/`).
Also this helper function only serves the actual [`STATIC_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_ROOT) folder; it doesn’t perform static files discovery like [`django.contrib.staticfiles`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files.").
Finally, static files are served via a wrapper at the WSGI application layer. As a consequence, static files requests do not pass through the normal [middleware chain](https://docs.djangoproject.com/en/5.0/topics/http/middleware/).
## Serving files uploaded by a user during development[¶](https://docs.djangoproject.com/en/5.0/howto/static-files/#serving-files-uploaded-by-a-user-during-development "Link to this heading")
During development, you can serve user-uploaded media files from [`MEDIA_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_ROOT) using the [`django.views.static.serve()`](https://docs.djangoproject.com/en/5.0/ref/views/#django.views.static.serve "django.views.static.serve") view.
This is not suitable for production use! For some common deployment strategies, see [How to deploy static files](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/).
For example, if your [`MEDIA_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_URL) is defined as `media/`, you can do this by adding the following snippet to your [`ROOT_URLCONF`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ROOT_URLCONF):
```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

Note
This helper function works only in debug mode and only if the given prefix is local (e.g. `media/`) and not a URL (e.g. `http://media.example.com/`).
## Testing[¶](https://docs.djangoproject.com/en/5.0/howto/static-files/#testing "Link to this heading")
When running tests that use actual HTTP requests instead of the built-in testing client (i.e. when using the built-in [`LiveServerTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.LiveServerTestCase "django.test.LiveServerTestCase")) the static assets need to be served along the rest of the content so the test environment reproduces the real one as faithfully as possible, but `LiveServerTestCase` has only very basic static file-serving functionality: It doesn’t know about the finders feature of the `staticfiles` application and assumes the static content has already been collected under [`STATIC_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_ROOT).
Because of this, `staticfiles` ships its own [`django.contrib.staticfiles.testing.StaticLiveServerTestCase`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django.contrib.staticfiles.testing.StaticLiveServerTestCase "django.contrib.staticfiles.testing.StaticLiveServerTestCase"), a subclass of the built-in one that has the ability to transparently serve all the assets during execution of these tests in a way very similar to what we get at development time with `DEBUG = True`, i.e. without having to collect them using [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) first.
## Deployment[¶](https://docs.djangoproject.com/en/5.0/howto/static-files/#deployment "Link to this heading")
[`django.contrib.staticfiles`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files.") provides a convenience management command for gathering static files in a single directory so you can serve them easily.
  1. Set the [`STATIC_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_ROOT) setting to the directory from which you’d like to serve these files, for example:
```
STATIC_ROOT = "/var/www/example.com/static/"

```

  2. Run the [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) management command:
```
$ python manage.py collectstatic

```

This will copy all files from your static folders into the [`STATIC_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_ROOT) directory.
  3. Use a web server of your choice to serve the files. [How to deploy static files](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/) covers some common deployment strategies for static files.


## Learn more[¶](https://docs.djangoproject.com/en/5.0/howto/static-files/#learn-more "Link to this heading")
This document has covered the basics and some common usage patterns. For complete details on all the settings, commands, template tags, and other pieces included in [`django.contrib.staticfiles`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files."), see [the staticfiles reference](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/).
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/howto/overriding-templates/)
[How to deploy static files ](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/)
[](https://docs.djangoproject.com/en/5.0/howto/static-files/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Atlanta Medical Malpractice Lawyer donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to manage static files (e.g. images, JavaScript, CSS)](https://docs.djangoproject.com/en/5.0/howto/static-files/)
    * [Configuring static files](https://docs.djangoproject.com/en/5.0/howto/static-files/#configuring-static-files)
    * [Serving static files during development](https://docs.djangoproject.com/en/5.0/howto/static-files/#serving-static-files-during-development)
    * [Serving files uploaded by a user during development](https://docs.djangoproject.com/en/5.0/howto/static-files/#serving-files-uploaded-by-a-user-during-development)
    * [Testing](https://docs.djangoproject.com/en/5.0/howto/static-files/#testing)
    * [Deployment](https://docs.djangoproject.com/en/5.0/howto/static-files/#deployment)
    * [Learn more](https://docs.djangoproject.com/en/5.0/howto/static-files/#learn-more)


### Browse
  * Prev: [How to override templates](https://docs.djangoproject.com/en/5.0/howto/overriding-templates/)
  * Next: [How to deploy static files](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to manage static files (e.g. images, JavaScript, CSS)


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
