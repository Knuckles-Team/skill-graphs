[Skip to main content](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/#main-content)
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
[Documentation](https://docs.djangoproject.com/en/6.0/)
  * [ Getting Help ](https://docs.djangoproject.com/en/6.0/faq/help/)


  * Language: **en**
  * [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/howto/deployment/wsgi/)
  * [sv](https://docs.djangoproject.com/sv/6.0/howto/deployment/wsgi/)
  * [pt-br](https://docs.djangoproject.com/pt-br/6.0/howto/deployment/wsgi/)
  * [pl](https://docs.djangoproject.com/pl/6.0/howto/deployment/wsgi/)
  * [ko](https://docs.djangoproject.com/ko/6.0/howto/deployment/wsgi/)
  * [ja](https://docs.djangoproject.com/ja/6.0/howto/deployment/wsgi/)
  * [it](https://docs.djangoproject.com/it/6.0/howto/deployment/wsgi/)
  * [id](https://docs.djangoproject.com/id/6.0/howto/deployment/wsgi/)
  * [fr](https://docs.djangoproject.com/fr/6.0/howto/deployment/wsgi/)
  * [es](https://docs.djangoproject.com/es/6.0/howto/deployment/wsgi/)
  * [el](https://docs.djangoproject.com/el/6.0/howto/deployment/wsgi/)


  * Documentation version: **6.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/)
  * [5.0](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/)
  * [4.0](https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/)
  * [3.2](https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/)
  * [3.1](https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/)
  * [3.0](https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/)
  * [2.2](https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/)
  * [2.1](https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/)
  * [2.0](https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/)
  * [1.11](https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/)
  * [1.10](https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/)
  * [1.8](https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/)


  * [](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/#top)


# How to deploy with WSGI[¶](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/#how-to-deploy-with-wsgi "Link to this heading")
Django’s primary deployment platform is
Django’s [`startproject`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-startproject) management command sets up a minimal default WSGI configuration for you, which you can tweak as needed for your project, and direct any WSGI-compliant application server to use.
Django includes getting-started documentation for the following WSGI servers:
  * [How to use Django with Gunicorn](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/gunicorn/)
  * [How to use Django with uWSGI](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/uwsgi/)
  * [How to use Django with Apache and `mod_wsgi`](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/modwsgi/)
  * [How to authenticate against Django’s user database from Apache](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/apache-auth/)


## The `application` object[¶](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/#the-application-object "Link to this heading")
The key concept of deploying with WSGI is the `application` callable which the application server uses to communicate with your code. It’s commonly provided as an object named `application` in a Python module accessible to the server.
The [`startproject`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-startproject) command creates a file `<project_name>/wsgi.py` that contains such an `application` callable.
It’s used both by Django’s development server and in production WSGI deployments.
WSGI servers obtain the path to the `application` callable from their configuration. Django’s built-in server, namely the [`runserver`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-runserver) command, reads it from the [`WSGI_APPLICATION`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-WSGI_APPLICATION) setting. By default, it’s set to `<project_name>.wsgi.application`, which points to the `application` callable in `<project_name>/wsgi.py`.
## Configuring the settings module[¶](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/#configuring-the-settings-module "Link to this heading")
When the WSGI server loads your application, Django needs to import the settings module — that’s where your entire application is defined.
Django uses the [`DJANGO_SETTINGS_MODULE`](https://docs.djangoproject.com/en/6.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE) environment variable to locate the appropriate settings module. It must contain the dotted path to the settings module. You can use a different value for development and production; it all depends on how you organize your settings.
If this variable isn’t set, the default `wsgi.py` sets it to `mysite.settings`, where `mysite` is the name of your project. That’s how [`runserver`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-runserver) discovers the default settings file by default.
Note
Since environment variables are process-wide, this doesn’t work when you run multiple Django sites in the same process. This happens with mod_wsgi.
To avoid this problem, use mod_wsgi’s daemon mode with each site in its own daemon process, or override the value from the environment by enforcing `os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"` in your `wsgi.py`.
## Applying WSGI middleware[¶](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/#applying-wsgi-middleware "Link to this heading")
To apply `wsgi.py`:
```
from helloworld.wsgi import HelloWorldApplication

application = HelloWorldApplication(application)

```

You could also replace the Django WSGI application with a custom WSGI application that later delegates to the Django WSGI application, if you want to combine a Django application with a WSGI application of another framework.
Previous page and next page
[](https://docs.djangoproject.com/en/6.0/howto/deployment/)
[How to use Django with Gunicorn ](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/gunicorn/)
[](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Godscripts donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to deploy with WSGI](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/)
    * [The `application` object](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/#the-application-object)
    * [Configuring the settings module](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/#configuring-the-settings-module)
    * [Applying WSGI middleware](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/#applying-wsgi-middleware)


### Browse
  * Prev: [How to deploy Django](https://docs.djangoproject.com/en/6.0/howto/deployment/)
  * Next: [How to use Django with Gunicorn](https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/gunicorn/)
  * [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)


### You are here:
  * [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    * [How-to guides](https://docs.djangoproject.com/en/6.0/howto/)
      * [How to deploy Django](https://docs.djangoproject.com/en/6.0/howto/deployment/)
        * How to deploy with WSGI


### Getting help

[FAQ](https://docs.djangoproject.com/en/6.0/faq/)
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
Offline (Django 6.0): [HTML](https://media.djangoproject.com/docs/django-docs-6.0-en.zip) |
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
