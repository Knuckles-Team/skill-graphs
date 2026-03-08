This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/howto/custom-management-commands/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/howto/custom-management-commands/)
  * [pl](https://docs.djangoproject.com/pl/5.0/howto/custom-management-commands/)
  * [ko](https://docs.djangoproject.com/ko/5.0/howto/custom-management-commands/)
  * [ja](https://docs.djangoproject.com/ja/5.0/howto/custom-management-commands/)
  * [it](https://docs.djangoproject.com/it/5.0/howto/custom-management-commands/)
  * [id](https://docs.djangoproject.com/id/5.0/howto/custom-management-commands/)
  * [fr](https://docs.djangoproject.com/fr/5.0/howto/custom-management-commands/)
  * [es](https://docs.djangoproject.com/es/5.0/howto/custom-management-commands/)
  * [el](https://docs.djangoproject.com/el/5.0/howto/custom-management-commands/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/)
  * [6.0](https://docs.djangoproject.com/en/6.0/howto/custom-management-commands/)
  * [5.2](https://docs.djangoproject.com/en/5.2/howto/custom-management-commands/)
  * [5.1](https://docs.djangoproject.com/en/5.1/howto/custom-management-commands/)
  * [4.2](https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/)
  * [4.1](https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/)
  * [4.0](https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/)
  * [3.2](https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/)
  * [3.1](https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/)
  * [3.0](https://docs.djangoproject.com/en/3.0/howto/custom-management-commands/)
  * [2.2](https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/)
  * [2.1](https://docs.djangoproject.com/en/2.1/howto/custom-management-commands/)
  * [2.0](https://docs.djangoproject.com/en/2.0/howto/custom-management-commands/)
  * [1.11](https://docs.djangoproject.com/en/1.11/howto/custom-management-commands/)
  * [1.10](https://docs.djangoproject.com/en/1.10/howto/custom-management-commands/)
  * [1.8](https://docs.djangoproject.com/en/1.8/howto/custom-management-commands/)


  * [](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#top)


# How to create custom `django-admin` commands[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#module-django.core.management "Link to this heading")
Applications can register their own actions with `manage.py`. For example, you might want to add a `manage.py` action for a Django app that you’re distributing. In this document, we will be building a custom `closepoll` command for the `polls` application from the [tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial01/).
To do this, add a `management/commands` directory to the application. Django will register a `manage.py` command for each Python module in that directory whose name doesn’t begin with an underscore. For example:
```
polls/
    __init__.py
    models.py
    management/
        __init__.py
        commands/
            __init__.py
            _private.py
            closepoll.py
    tests.py
    views.py

```

In this example, the `closepoll` command will be made available to any project that includes the `polls` application in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS).
The `_private.py` module will not be available as a management command.
The `closepoll.py` module has only one requirement – it must define a class `Command` that extends [`BaseCommand`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand "django.core.management.BaseCommand") or one of its [subclasses](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#ref-basecommand-subclasses).
Standalone scripts
Custom management commands are especially useful for running standalone scripts or for scripts that are periodically executed from the UNIX crontab or from Windows scheduled tasks control panel.
To implement the command, edit `polls/management/commands/closepoll.py` to look like this:
```
from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        for poll_id in options["poll_ids"]:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(
                self.style.SUCCESS('Successfully closed poll "%s"' % poll_id)
            )

```

Note
When you are using management commands and wish to provide console output, you should write to `self.stdout` and `self.stderr`, instead of printing to `stdout` and `stderr` directly. By using these proxies, it becomes much easier to test your custom command. Note also that you don’t need to end messages with a newline character, it will be added automatically, unless you specify the `ending` parameter:
```
self.stdout.write("Unterminated line", ending="")

```

The new custom command can be called using `python manage.py closepoll <poll_ids>`.
The `handle()` method takes one or more `poll_ids` and sets `poll.opened` to `False` for each one. If the user referenced any nonexistent polls, a [`CommandError`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.CommandError "django.core.management.CommandError") is raised. The `poll.opened` attribute does not exist in the [tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial02/) and was added to `polls.models.Question` for this example.
## Accepting optional arguments[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#accepting-optional-arguments "Link to this heading")
The same `closepoll` could be easily modified to delete a given poll instead of closing it by accepting additional command line options. These custom options can be added in the [`add_arguments()`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.add_arguments "django.core.management.BaseCommand.add_arguments") method like this:
```
class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("poll_ids", nargs="+", type=int)

        # Named (optional) arguments
        parser.add_argument(
            "--delete",
            action="store_true",
            help="Delete poll instead of closing it",
        )

    def handle(self, *args, **options):
        # ...
        if options["delete"]:
            poll.delete()
        # ...

```

The option (`delete` in our example) is available in the options dict parameter of the handle method. See the `add_argument` usage.
In addition to being able to add custom command line options, all [management commands](https://docs.djangoproject.com/en/5.0/ref/django-admin/) can accept some default options such as [`--verbosity`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-verbosity) and [`--traceback`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-traceback).
## Management commands and locales[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#management-commands-and-locales "Link to this heading")
By default, management commands are executed with the current active locale.
If, for some reason, your custom management command must run without an active locale (for example, to prevent translated content from being inserted into the database), deactivate translations using the `@no_translations` decorator on your [`handle()`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.handle "django.core.management.BaseCommand.handle") method:
```
from django.core.management.base import BaseCommand, no_translations


class Command(BaseCommand):
    ...

    @no_translations
    def handle(self, *args, **options): ...

```

Since translation deactivation requires access to configured settings, the decorator can’t be used for commands that work without configured settings.
## Testing[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#testing "Link to this heading")
Information on how to test custom management commands can be found in the [testing docs](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#topics-testing-management-commands).
## Overriding commands[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#overriding-commands "Link to this heading")
Django registers the built-in commands and then searches for commands in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) in reverse. During the search, if a command name duplicates an already registered command, the newly discovered command overrides the first.
In other words, to override a command, the new command must have the same name and its app must be before the overridden command’s app in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS).
Management commands from third-party apps that have been unintentionally overridden can be made available under a new name by creating a new command in one of your project’s apps (ordered before the third-party app in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS)) which imports the `Command` of the overridden command.
## Command objects[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#command-objects "Link to this heading")

_class_ BaseCommand[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/management/base/#BaseCommand)[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand "Link to this definition")

The base class from which all management commands ultimately derive.
Use this class if you want access to all of the mechanisms which parse the command-line arguments and work out what code to call in response; if you don’t need to change any of that behavior, consider using one of its [subclasses](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#ref-basecommand-subclasses).
Subclassing the [`BaseCommand`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand "django.core.management.BaseCommand") class requires that you implement the [`handle()`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.handle "django.core.management.BaseCommand.handle") method.
### Attributes[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#attributes "Link to this heading")
All attributes can be set in your derived class and can be used in [`BaseCommand`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand "django.core.management.BaseCommand")’s [subclasses](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#ref-basecommand-subclasses).

BaseCommand.help[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.help "Link to this definition")

A short description of the command, which will be printed in the help message when the user runs the command `python manage.py help <command>`.

BaseCommand.missing_args_message[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.missing_args_message "Link to this definition")

If your command defines mandatory positional arguments, you can customize the message error returned in the case of missing arguments. The default is output by

BaseCommand.output_transaction[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.output_transaction "Link to this definition")

A boolean indicating whether the command outputs SQL statements; if `True`, the output will automatically be wrapped with `BEGIN;` and `COMMIT;`. Default value is `False`.

BaseCommand.requires_migrations_checks[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.requires_migrations_checks "Link to this definition")

A boolean; if `True`, the command prints a warning if the set of migrations on disk don’t match the migrations in the database. A warning doesn’t prevent the command from executing. Default value is `False`.

BaseCommand.requires_system_checks[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.requires_system_checks "Link to this definition")

A list or tuple of tags, e.g. `[Tags.staticfiles, Tags.models]`. System checks [registered in the chosen tags](https://docs.djangoproject.com/en/5.0/topics/checks/#registering-labeling-checks) will be checked for errors prior to executing the command. The value `'__all__'` can be used to specify that all system checks should be performed. Default value is `'__all__'`.

BaseCommand.style[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.style "Link to this definition")

An instance attribute that helps create colored output when writing to `stdout` or `stderr`. For example:
```
self.stdout.write(self.style.SUCCESS("..."))

```

See [Syntax coloring](https://docs.djangoproject.com/en/5.0/ref/django-admin/#syntax-coloring) to learn how to modify the color palette and to see the available styles (use uppercased versions of the “roles” described in that section).
If you pass the [`--no-color`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-no-color) option when running your command, all `self.style()` calls will return the original string uncolored.

BaseCommand.suppressed_base_arguments[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.suppressed_base_arguments "Link to this definition")

The default command options to suppress in the help output. This should be a set of option names (e.g. `'--verbosity'`). The default values for the suppressed options are still passed.
### Methods[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#methods "Link to this heading")
[`BaseCommand`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand "django.core.management.BaseCommand") has a few methods that can be overridden but only the [`handle()`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.handle "django.core.management.BaseCommand.handle") method must be implemented.
Implementing a constructor in a subclass
If you implement `__init__` in your subclass of [`BaseCommand`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand "django.core.management.BaseCommand"), you must call [`BaseCommand`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand "django.core.management.BaseCommand")’s `__init__`:
```
class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ...

```


BaseCommand.create_parser(_prog_name_ , _subcommand_ , _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/management/base/#BaseCommand.create_parser)[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.create_parser "Link to this definition")

Returns a `CommandParser` instance, which is an
You can customize the instance by overriding this method and calling `super()` with `kwargs` of

BaseCommand.add_arguments(_parser_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/management/base/#BaseCommand.add_arguments)[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.add_arguments "Link to this definition")

Entry point to add parser arguments to handle command line arguments passed to the command. Custom commands should override this method to add both positional and optional arguments accepted by the command. Calling `super()` is not needed when directly subclassing `BaseCommand`.

BaseCommand.get_version()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/management/base/#BaseCommand.get_version)[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.get_version "Link to this definition")

Returns the Django version, which should be correct for all built-in Django commands. User-supplied commands can override this method to return their own version.

BaseCommand.execute(_* args_, _** options_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/management/base/#BaseCommand.execute)[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.execute "Link to this definition")

Tries to execute this command, performing system checks if needed (as controlled by the [`requires_system_checks`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.requires_system_checks "django.core.management.BaseCommand.requires_system_checks") attribute). If the command raises a [`CommandError`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.CommandError "django.core.management.CommandError"), it’s intercepted and printed to `stderr`.
Calling a management command in your code
`execute()` should not be called directly from your code to execute a command. Use [`call_command()`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django.core.management.call_command "django.core.management.call_command") instead.

BaseCommand.handle(_* args_, _** options_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/management/base/#BaseCommand.handle)[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.handle "Link to this definition")

The actual logic of the command. Subclasses must implement this method.
It may return a string which will be printed to `stdout` (wrapped by `BEGIN;` and `COMMIT;` if [`output_transaction`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.output_transaction "django.core.management.BaseCommand.output_transaction") is `True`).

BaseCommand.check(_app_configs =None_, _tags =None_, _display_num_errors =False_, _include_deployment_checks =False_, _fail_level =checks.ERROR_, _databases =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/management/base/#BaseCommand.check)[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.check "Link to this definition")

Uses the system check framework to inspect the entire Django project for potential problems. Serious problems are raised as a [`CommandError`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.CommandError "django.core.management.CommandError"); warnings are output to `stderr`; minor notifications are output to `stdout`.
If `app_configs` and `tags` are both `None`, all system checks are performed except deployment and database related checks. `tags` can be a list of check tags, like `compatibility` or `models`.
You can pass `include_deployment_checks=True` to also perform deployment checks, and list of database aliases in the `databases` to run database related checks against them.
###  `BaseCommand` subclasses[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#basecommand-subclasses "Link to this heading")

_class_ AppCommand[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.AppCommand "Link to this definition")

A management command which takes one or more installed application labels as arguments, and does something with each of them.
Rather than implementing [`handle()`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.handle "django.core.management.BaseCommand.handle"), subclasses must implement [`handle_app_config()`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.AppCommand.handle_app_config "django.core.management.AppCommand.handle_app_config"), which will be called once for each application.

AppCommand.handle_app_config(_app_config_ , _** options_)[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.AppCommand.handle_app_config "Link to this definition")

Perform the command’s actions for `app_config`, which will be an [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") instance corresponding to an application label given on the command line.

_class_ LabelCommand[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.LabelCommand "Link to this definition")

A management command which takes one or more arbitrary arguments (labels) on the command line, and does something with each of them.
Rather than implementing [`handle()`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.BaseCommand.handle "django.core.management.BaseCommand.handle"), subclasses must implement [`handle_label()`](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.LabelCommand.handle_label "django.core.management.LabelCommand.handle_label"), which will be called once for each label.

LabelCommand.label[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.LabelCommand.label "Link to this definition")

A string describing the arbitrary arguments passed to the command. The string is used in the usage text and error messages of the command. Defaults to `'label'`.

LabelCommand.handle_label(_label_ , _** options_)[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.LabelCommand.handle_label "Link to this definition")

Perform the command’s actions for `label`, which will be the string as given on the command line.
### Command exceptions[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#command-exceptions "Link to this heading")

_exception_ CommandError(_returncode =1_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/core/management/base/#CommandError)[¶](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#django.core.management.CommandError "Link to this definition")

Exception class indicating a problem while executing a management command.
If this exception is raised during the execution of a management command from a command line console, it will be caught and turned into a nicely-printed error message to the appropriate output stream (i.e., `stderr`); as a result, raising this exception (with a sensible description of the error) is the preferred way to indicate that something has gone wrong in the execution of a command. It accepts the optional `returncode` argument to customize the exit status for the management command to exit with, using
If a management command is called from code through [`call_command()`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django.core.management.call_command "django.core.management.call_command"), it’s up to you to catch the exception when needed.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/howto/csrf/)
[How to create custom model fields ](https://docs.djangoproject.com/en/5.0/howto/custom-model-fields/)
[](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ 蔡海滨 donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [How to create custom `django-admin` commands](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/)
    * [Accepting optional arguments](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#accepting-optional-arguments)
    * [Management commands and locales](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#management-commands-and-locales)
    * [Testing](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#testing)
    * [Overriding commands](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#overriding-commands)
    * [Command objects](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#command-objects)
      * [Attributes](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#attributes)
      * [Methods](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#methods)
      * [`BaseCommand` subclasses](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#basecommand-subclasses)
      * [Command exceptions](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/#command-exceptions)


### Browse
  * Prev: [How to use Django’s CSRF protection](https://docs.djangoproject.com/en/5.0/howto/csrf/)
  * Next: [How to create custom model fields](https://docs.djangoproject.com/en/5.0/howto/custom-model-fields/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [“How-to” guides](https://docs.djangoproject.com/en/5.0/howto/)
      * How to create custom `django-admin` commands


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
