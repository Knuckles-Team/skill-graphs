## Default options[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#default-options "Link to this heading")
Although some commands may allow their own custom options, every command allows for the following options by default:

--pythonpath PYTHONPATH[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-pythonpath "Link to this definition")

Adds the given filesystem path to the Python `django-admin` will use the
This option is unnecessary in `manage.py`, because it takes care of setting the Python path for you.
Example usage:
```
django-admin migrate --pythonpath='/home/djangoprojects/myproject'

```


--settings SETTINGS[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-settings "Link to this definition")

Specifies the settings module to use. The settings module should be in Python package syntax, e.g. `mysite.settings`. If this isn’t provided, `django-admin` will use the [`DJANGO_SETTINGS_MODULE`](https://docs.djangoproject.com/en/5.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE) environment variable.
This option is unnecessary in `manage.py`, because it uses `settings.py` from the current project by default.
Example usage:
```
django-admin migrate --settings=mysite.settings

```


--traceback[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-traceback "Link to this definition")

Displays a full stack trace when a [`CommandError`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.CommandError "django.core.management.CommandError") is raised. By default, `django-admin` will show an error message when a `CommandError` occurs and a full stack trace for any other exception.
This option is ignored by [`runserver`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-runserver).
Example usage:
```
django-admin migrate --traceback

```


--verbosity {0,1,2,3}, -v {0,1,2,3}[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-verbosity "Link to this definition")

Specifies the amount of notification and debug information that a command should print to the console.
  * `0` means no output.
  * `1` means normal output (default).
  * `2` means verbose output.
  * `3` means _very_ verbose output.


This option is ignored by [`runserver`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-runserver).
Example usage:
```
django-admin migrate --verbosity 2

```


--no-color[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-no-color "Link to this definition")

Disables colorized command output. Some commands format their output to be colorized. For example, errors will be printed to the console in red and SQL statements will be syntax highlighted.
Example usage:
```
django-admin runserver --no-color

```


--force-color[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-force-color "Link to this definition")

Forces colorization of the command output if it would otherwise be disabled as discussed in [Syntax coloring](https://docs.djangoproject.com/en/5.0/ref/django-admin/#syntax-coloring). For example, you may want to pipe colored output to another command.

--skip-checks[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-skip-checks "Link to this definition")

Skips running system checks prior to running the command. This option is only available if the [`requires_system_checks`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.requires_system_checks "django.core.management.BaseCommand.requires_system_checks") command attribute is not an empty list or tuple.
Example usage:
```
django-admin migrate --skip-checks

```
