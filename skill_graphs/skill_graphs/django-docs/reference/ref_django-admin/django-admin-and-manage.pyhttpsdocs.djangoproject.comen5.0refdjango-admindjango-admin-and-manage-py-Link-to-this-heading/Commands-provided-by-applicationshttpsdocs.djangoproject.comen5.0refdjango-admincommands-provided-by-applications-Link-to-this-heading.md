## Commands provided by applications[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#commands-provided-by-applications "Link to this heading")
Some commands are only available when the `django.contrib` application that [implements](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/) them has been [`enabled`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS). This section describes them grouped by their application.
###  `django.contrib.auth`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-contrib-auth "Link to this heading")
####  `changepassword`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#changepassword "Link to this heading")

django-admin changepassword [<username>][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-changepassword "Link to this definition")

This command is only available if Django’s [authentication system](https://docs.djangoproject.com/en/5.0/topics/auth/) (`django.contrib.auth`) is installed.
Allows changing a user’s password. It prompts you to enter a new password twice for the given user. If the entries are identical, this immediately becomes the new password. If you do not supply a user, the command will attempt to change the password whose username matches the current user.

--database DATABASE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-changepassword-database "Link to this definition")

Specifies the database to query for the user. Defaults to `default`.
Example usage:
```
django-admin changepassword ringo

```

####  `createsuperuser`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#createsuperuser "Link to this heading")

django-admin createsuperuser[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-createsuperuser "Link to this definition")


DJANGO_SUPERUSER_PASSWORD[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#envvar-DJANGO_SUPERUSER_PASSWORD "Link to this definition")

This command is only available if Django’s [authentication system](https://docs.djangoproject.com/en/5.0/topics/auth/) (`django.contrib.auth`) is installed.
Creates a superuser account (a user who has all permissions). This is useful if you need to create an initial superuser account or if you need to programmatically generate superuser accounts for your site(s).
When run interactively, this command will prompt for a password for the new superuser account. When run non-interactively, you can provide a password by setting the [`DJANGO_SUPERUSER_PASSWORD`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#envvar-DJANGO_SUPERUSER_PASSWORD) environment variable. Otherwise, no password will be set, and the superuser account will not be able to log in until a password has been manually set for it.
In non-interactive mode, the [`USERNAME_FIELD`](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#django.contrib.auth.models.CustomUser.USERNAME_FIELD "django.contrib.auth.models.CustomUser.USERNAME_FIELD") and required fields (listed in [`REQUIRED_FIELDS`](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#django.contrib.auth.models.CustomUser.REQUIRED_FIELDS "django.contrib.auth.models.CustomUser.REQUIRED_FIELDS")) fall back to `DJANGO_SUPERUSER_<uppercase_field_name>` environment variables, unless they are overridden by a command line argument. For example, to provide an `email` field, you can use `DJANGO_SUPERUSER_EMAIL` environment variable.

--noinput, --no-input[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-createsuperuser-noinput "Link to this definition")

Suppresses all user prompts. If a suppressed prompt cannot be resolved automatically, the command will exit with error code 1.

--username USERNAME[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-createsuperuser-username "Link to this definition")


--email EMAIL[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-createsuperuser-email "Link to this definition")

The username and email address for the new account can be supplied by using the `--username` and `--email` arguments on the command line. If either of those is not supplied, `createsuperuser` will prompt for it when running interactively.

--database DATABASE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-createsuperuser-database "Link to this definition")

Specifies the database into which the superuser object will be saved.
You can subclass the management command and override `get_input_data()` if you want to customize data input and validation. Consult the source code for details on the existing implementation and the method’s parameters. For example, it could be useful if you have a `ForeignKey` in [`REQUIRED_FIELDS`](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#django.contrib.auth.models.CustomUser.REQUIRED_FIELDS "django.contrib.auth.models.CustomUser.REQUIRED_FIELDS") and want to allow creating an instance instead of entering the primary key of an existing instance.
###  `django.contrib.contenttypes`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-contrib-contenttypes "Link to this heading")
####  `remove_stale_contenttypes`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#remove-stale-contenttypes "Link to this heading")

django-admin remove_stale_contenttypes[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-remove_stale_contenttypes "Link to this definition")

This command is only available if Django’s [contenttypes app](https://docs.djangoproject.com/en/5.0/ref/contrib/contenttypes/) ([`django.contrib.contenttypes`](https://docs.djangoproject.com/en/5.0/ref/contrib/contenttypes/#module-django.contrib.contenttypes "django.contrib.contenttypes: Provides generic interface to installed models.")) is installed.
Deletes stale content types (from deleted models) in your database. Any objects that depend on the deleted content types will also be deleted. A list of deleted objects will be displayed before you confirm it’s okay to proceed with the deletion.

--database DATABASE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-remove_stale_contenttypes-database "Link to this definition")

Specifies the database to use. Defaults to `default`.

--include-stale-apps[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-remove_stale_contenttypes-include-stale-apps "Link to this definition")

Deletes stale content types including ones from previously installed apps that have been removed from [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS). Defaults to `False`.
###  `django.contrib.gis`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-contrib-gis "Link to this heading")
####  `ogrinspect`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#ogrinspect "Link to this heading")
This command is only available if [GeoDjango](https://docs.djangoproject.com/en/5.0/ref/contrib/gis/) (`django.contrib.gis`) is installed.
Please refer to its [`description`](https://docs.djangoproject.com/en/5.0/ref/contrib/gis/commands/#django-admin-ogrinspect) in the GeoDjango documentation.
###  `django.contrib.sessions`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-contrib-sessions "Link to this heading")
####  `clearsessions`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#clearsessions "Link to this heading")

django-admin clearsessions[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-clearsessions "Link to this definition")

Can be run as a cron job or directly to clean out expired sessions.
###  `django.contrib.staticfiles`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-contrib-staticfiles "Link to this heading")
####  `collectstatic`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#collectstatic "Link to this heading")
This command is only available if the [static files application](https://docs.djangoproject.com/en/5.0/howto/static-files/) (`django.contrib.staticfiles`) is installed.
Please refer to its [`description`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic) in the [staticfiles](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/) documentation.
####  `findstatic`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#findstatic "Link to this heading")
This command is only available if the [static files application](https://docs.djangoproject.com/en/5.0/howto/static-files/) (`django.contrib.staticfiles`) is installed.
Please refer to its [`description`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-findstatic) in the [staticfiles](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/) documentation.
