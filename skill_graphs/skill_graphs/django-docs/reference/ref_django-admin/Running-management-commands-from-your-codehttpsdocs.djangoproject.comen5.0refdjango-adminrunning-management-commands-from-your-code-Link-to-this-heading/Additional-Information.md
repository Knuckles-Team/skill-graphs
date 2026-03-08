## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Markus Holtermann donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [`django-admin` and `manage.py`](https://docs.djangoproject.com/en/5.0/ref/django-admin/)
    * [Usage](https://docs.djangoproject.com/en/5.0/ref/django-admin/#usage)
      * [Getting runtime help](https://docs.djangoproject.com/en/5.0/ref/django-admin/#getting-runtime-help)
      * [App names](https://docs.djangoproject.com/en/5.0/ref/django-admin/#app-names)
      * [Determining the version](https://docs.djangoproject.com/en/5.0/ref/django-admin/#determining-the-version)
      * [Displaying debug output](https://docs.djangoproject.com/en/5.0/ref/django-admin/#displaying-debug-output)
    * [Available commands](https://docs.djangoproject.com/en/5.0/ref/django-admin/#available-commands)
      * [`check`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#check)
      * [`compilemessages`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#compilemessages)
      * [`createcachetable`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#createcachetable)
      * [`dbshell`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#dbshell)
      * [`diffsettings`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#diffsettings)
      * [`dumpdata`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#dumpdata)
        * [Fixtures compression](https://docs.djangoproject.com/en/5.0/ref/django-admin/#fixtures-compression)
      * [`flush`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#flush)
      * [`inspectdb`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#inspectdb)
        * [Database-specific notes](https://docs.djangoproject.com/en/5.0/ref/django-admin/#database-specific-notes)
          * [Oracle](https://docs.djangoproject.com/en/5.0/ref/django-admin/#oracle)
          * [PostgreSQL](https://docs.djangoproject.com/en/5.0/ref/django-admin/#postgresql)
      * [`loaddata`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#loaddata)
        * [Loading fixtures from `stdin`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#loading-fixtures-from-stdin)
      * [`makemessages`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#makemessages)
      * [`makemigrations`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#makemigrations)
      * [`migrate`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#migrate)
      * [`optimizemigration`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#optimizemigration)
      * [`runserver`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#runserver)
        * [Examples of using different ports and addresses](https://docs.djangoproject.com/en/5.0/ref/django-admin/#examples-of-using-different-ports-and-addresses)
        * [Serving static files with the development server](https://docs.djangoproject.com/en/5.0/ref/django-admin/#serving-static-files-with-the-development-server)
        * [Serving with ASGI in development](https://docs.djangoproject.com/en/5.0/ref/django-admin/#serving-with-asgi-in-development)
      * [`sendtestemail`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#sendtestemail)
      * [`shell`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#shell)
      * [`showmigrations`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#showmigrations)
      * [`sqlflush`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#sqlflush)
      * [`sqlmigrate`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#sqlmigrate)
      * [`sqlsequencereset`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#sqlsequencereset)
      * [`squashmigrations`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#squashmigrations)
      * [`startapp`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#startapp)
      * [`startproject`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#startproject)
      * [`test`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#test)
        * [Test runner options](https://docs.djangoproject.com/en/5.0/ref/django-admin/#test-runner-options)
      * [`testserver`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#testserver)
    * [Commands provided by applications](https://docs.djangoproject.com/en/5.0/ref/django-admin/#commands-provided-by-applications)
      * [`django.contrib.auth`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-contrib-auth)
        * [`changepassword`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#changepassword)
        * [`createsuperuser`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#createsuperuser)
      * [`django.contrib.contenttypes`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-contrib-contenttypes)
        * [`remove_stale_contenttypes`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#remove-stale-contenttypes)
      * [`django.contrib.gis`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-contrib-gis)
        * [`ogrinspect`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#ogrinspect)
      * [`django.contrib.sessions`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-contrib-sessions)
        * [`clearsessions`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#clearsessions)
      * [`django.contrib.staticfiles`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-contrib-staticfiles)
        * [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#collectstatic)
        * [`findstatic`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#findstatic)
    * [Default options](https://docs.djangoproject.com/en/5.0/ref/django-admin/#default-options)
    * [Extra niceties](https://docs.djangoproject.com/en/5.0/ref/django-admin/#extra-niceties)
      * [Syntax coloring](https://docs.djangoproject.com/en/5.0/ref/django-admin/#syntax-coloring)
        * [Windows support](https://docs.djangoproject.com/en/5.0/ref/django-admin/#windows-support)
        * [Custom colors](https://docs.djangoproject.com/en/5.0/ref/django-admin/#custom-colors)
      * [Bash completion](https://docs.djangoproject.com/en/5.0/ref/django-admin/#bash-completion)
      * [Black formatting](https://docs.djangoproject.com/en/5.0/ref/django-admin/#black-formatting)
  * [Running management commands from your code](https://docs.djangoproject.com/en/5.0/ref/django-admin/#running-management-commands-from-your-code)
    * [Output redirection](https://docs.djangoproject.com/en/5.0/ref/django-admin/#output-redirection)


### Browse
  * Prev: [Databases](https://docs.djangoproject.com/en/5.0/ref/databases/)
  * Next: [Django Exceptions](https://docs.djangoproject.com/en/5.0/ref/exceptions/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * `django-admin` and `manage.py`


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
