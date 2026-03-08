This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/deployment/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/deployment/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/deployment/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/deployment/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/deployment/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/deployment/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/deployment/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/deployment/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/deployment/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/deployment/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/deployment/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/deployment/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/deployment/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/deployment/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/deployment/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/deployment/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/deployment/)
  * [4.0](https://docs.djangoproject.com/en/4.0/howto/deployment/)
  * [3.2](https://docs.djangoproject.com/en/3.2/howto/deployment/)
  * [3.1](https://docs.djangoproject.com/en/3.1/howto/deployment/)
  * [3.0](https://docs.djangoproject.com/en/3.0/howto/deployment/)
  * [2.2](https://docs.djangoproject.com/en/2.2/howto/deployment/)
  * [2.1](https://docs.djangoproject.com/en/2.1/howto/deployment/)
  * [2.0](https://docs.djangoproject.com/en/2.0/howto/deployment/)
  * [1.11](https://docs.djangoproject.com/en/1.11/howto/deployment/)
  * [1.10](https://docs.djangoproject.com/en/1.10/howto/deployment/)
  * [1.8](https://docs.djangoproject.com/en/1.8/howto/deployment/)


  * [](https://docs.djangoproject.com/en/5.0/howto/deployment/#top)


# How to deploy Django[¶](https://docs.djangoproject.com/en/5.0/howto/deployment/#how-to-deploy-django "Link to this heading")
Django is full of shortcuts to make web developers’ lives easier, but all those tools are of no use if you can’t easily deploy your sites. Since Django’s inception, ease of deployment has been a major goal.
There are many options for deploying your Django application, based on your architecture or your particular business needs, but that discussion is outside the scope of what Django can give you as guidance.
Django, being a web framework, needs a web server in order to operate. And since most web servers don’t natively speak Python, we need an interface to make that communication happen.
Django currently supports two interfaces: WSGI and ASGI.
You should also consider how you will handle [static files](https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/) for your application, and how to handle [error reporting](https://docs.djangoproject.com/en/5.0/howto/error-reporting/).
Finally, before you deploy your application to production, you should run through our [deployment checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/) to ensure that your configurations are suitable.
  * [How to deploy with WSGI](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/)
    * [How to use Django with Gunicorn](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/gunicorn/)
    * [How to use Django with uWSGI](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/uwsgi/)
    * [How to use Django with Apache and `mod_wsgi`](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/modwsgi/)
    * [How to authenticate against Django’s user database from Apache](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/apache-auth/)
    * [The `application` object](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/#the-application-object)
    * [Configuring the settings module](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/#configuring-the-settings-module)
    * [Applying WSGI middleware](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/#applying-wsgi-middleware)
  * [How to deploy with ASGI](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/)
    * [How to use Django with Daphne](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/daphne/)
    * [How to use Django with Hypercorn](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/hypercorn/)
    * [How to use Django with Uvicorn](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/uvicorn/)
    * [The `application` object](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/#the-application-object)
    * [Configuring the settings module](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/#configuring-the-settings-module)
    * [Applying ASGI middleware](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/#applying-asgi-middleware)
  * [Deployment checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
    * [Run `manage.py check --deploy`](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/#run-manage-py-check-deploy)
    * [Critical settings](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/#critical-settings)
    * [Environment-specific settings](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/#environment-specific-settings)
    * [HTTPS](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/#https)
    * [Performance optimizations](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/#performance-optimizations)
    * [Error reporting](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/#error-reporting)


Previous page and next page
[](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/)
[How to deploy with WSGI ](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/)
[](https://docs.djangoproject.com/en/5.0/howto/deployment/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Kono Analytics donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to deploy Django](https://docs.djangoproject.com/en/5.0/howto/deployment/)


### Browse
  * Prev: [How to write a custom storage class](https://docs.djangoproject.com/en/5.0/howto/custom-file-storage/)
  * Next: [How to deploy with WSGI](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to deploy Django


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
