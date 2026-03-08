## Builtin tags[¶](https://docs.djangoproject.com/en/5.0/ref/checks/#builtin-tags "Link to this heading")
Django’s system checks are organized using the following tags:
  * `admin`: Checks of any admin site declarations.
  * `async_support`: Checks asynchronous-related configuration.
  * `caches`: Checks cache related configuration.
  * `compatibility`: Flags potential problems with version upgrades.
  * `database`: Checks database-related configuration issues. Database checks are not run by default because they do more than static code analysis as regular checks do. They are only run by the [`migrate`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-migrate) command or if you specify configured database aliases using the `--database` option when calling the [`check`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-check) command.
  * `files`: Checks files related configuration.
  * `models`: Checks of model, field, and manager definitions.
  * `security`: Checks security related configuration.
  * `signals`: Checks on signal declarations and handler registrations.
  * `sites`: Checks [`django.contrib.sites`](https://docs.djangoproject.com/en/5.0/ref/contrib/sites/#module-django.contrib.sites "django.contrib.sites: Lets you operate multiple websites from the same database and Django project") configuration.
  * `staticfiles`: Checks [`django.contrib.staticfiles`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files.") configuration.
  * `templates`: Checks template related configuration.
  * `translation`: Checks translation related configuration.
  * `urls`: Checks URL configuration.


Some checks may be registered with multiple tags.
