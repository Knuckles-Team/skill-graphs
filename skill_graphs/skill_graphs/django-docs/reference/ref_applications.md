This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/applications/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/applications/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/applications/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/applications/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/applications/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/applications/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/applications/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/applications/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/applications/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/applications/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/applications/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/applications/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/applications/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/applications/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/applications/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/applications/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/applications/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/applications/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/applications/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/applications/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/applications/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/applications/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/applications/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/applications/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/applications/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/applications/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/applications/)


  * [](https://docs.djangoproject.com/en/5.0/ref/applications/#top)


# Applications[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#module-django.apps "Link to this heading")
Django contains a registry of installed applications that stores configuration and provides introspection. It also maintains a list of available [models](https://docs.djangoproject.com/en/5.0/topics/db/models/).
This registry is called [`apps`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps "django.apps.apps") and it’s available in [`django.apps`](https://docs.djangoproject.com/en/5.0/ref/applications/#module-django.apps "django.apps"):
```
>>> from django.apps import apps
>>> apps.get_app_config("admin").verbose_name
'Administration'

```

## Projects and applications[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#projects-and-applications "Link to this heading")
The term **project** describes a Django web application. The project Python package is defined primarily by a settings module, but it usually contains other things. For example, when you run `django-admin startproject mysite` you’ll get a `mysite` project directory that contains a `mysite` Python package with `settings.py`, `urls.py`, `asgi.py` and `wsgi.py`. The project package is often extended to include things like fixtures, CSS, and templates which aren’t tied to a particular application.
A **project’s root directory** (the one that contains `manage.py`) is usually the container for all of a project’s applications which aren’t installed separately.
The term **application** describes a Python package that provides some set of features. Applications [may be reused](https://docs.djangoproject.com/en/5.0/intro/reusable-apps/) in various projects.
Applications include some combination of models, views, templates, template tags, static files, URLs, middleware, etc. They’re generally wired into projects with the [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) setting and optionally with other mechanisms such as URLconfs, the [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) setting, or template inheritance.
It is important to understand that a Django application is a set of code that interacts with various parts of the framework. There’s no such thing as an `Application` object. However, there’s a few places where Django needs to interact with installed applications, mainly for configuration and also for introspection. That’s why the application registry maintains metadata in an [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") instance for each installed application.
There’s no restriction that a project package can’t also be considered an application and have models, etc. (which would require adding it to [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS)).
## Configuring applications[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#configuring-applications "Link to this heading")
To configure an application, create an `apps.py` module inside the application, then define a subclass of [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") there.
When [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) contains the dotted path to an application module, by default, if Django finds exactly one [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") subclass in the `apps.py` submodule, it uses that configuration for the application. This behavior may be disabled by setting [`AppConfig.default`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.default "django.apps.AppConfig.default") to `False`.
If the `apps.py` module contains more than one [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") subclass, Django will look for a single one where [`AppConfig.default`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.default "django.apps.AppConfig.default") is `True`.
If no [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") subclass is found, the base [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") class will be used.
Alternatively, [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) may contain the dotted path to a configuration class to specify it explicitly:
```
INSTALLED_APPS = [
    ...,
    "polls.apps.PollsAppConfig",
    ...,
]

```

### For application authors[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#for-application-authors "Link to this heading")
If you’re creating a pluggable app called “Rock ’n’ roll”, here’s how you would provide a proper name for the admin:
```
# rock_n_roll/apps.py

from django.apps import AppConfig


class RockNRollConfig(AppConfig):
    name = "rock_n_roll"
    verbose_name = "Rock ’n’ roll"

```

`RockNRollConfig` will be loaded automatically when [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) contains `'rock_n_roll'`. If you need to prevent this, set [`default`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.default "django.apps.AppConfig.default") to `False` in the class definition.
You can provide several [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") subclasses with different behaviors. To tell Django which one to use by default, set [`default`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.default "django.apps.AppConfig.default") to `True` in its definition. If your users want to pick a non-default configuration, they must replace `'rock_n_roll'` with the dotted path to that specific class in their [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) setting.
The [`AppConfig.name`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.name "django.apps.AppConfig.name") attribute tells Django which application this configuration applies to. You can define any other attribute documented in the [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") API reference.
[`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") subclasses may be defined anywhere. The `apps.py` convention merely allows Django to load them automatically when [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) contains the path to an application module rather than the path to a configuration class.
Note
If your code imports the application registry in an application’s `__init__.py`, the name `apps` will clash with the `apps` submodule. The best practice is to move that code to a submodule and import it. A workaround is to import the registry under a different name:
```
from django.apps import apps as django_apps

```

### For application users[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#for-application-users "Link to this heading")
If you’re using “Rock ’n’ roll” in a project called `anthology`, but you want it to show up as “Jazz Manouche” instead, you can provide your own configuration:
```
# anthology/apps.py

from rock_n_roll.apps import RockNRollConfig


class JazzManoucheConfig(RockNRollConfig):
    verbose_name = "Jazz Manouche"


# anthology/settings.py

INSTALLED_APPS = [
    "anthology.apps.JazzManoucheConfig",
    # ...
]

```

This example shows project-specific configuration classes located in a submodule called `apps.py`. This is a convention, not a requirement. [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") subclasses may be defined anywhere.
In this situation, [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) must contain the dotted path to the configuration class because it lives outside of an application and thus cannot be automatically detected.
## Application configuration[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#application-configuration "Link to this heading")

_class_ AppConfig[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/apps/config/#AppConfig)[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "Link to this definition")

Application configuration objects store metadata for an application. Some attributes can be configured in [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") subclasses. Others are set by Django and read-only.
### Configurable attributes[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#configurable-attributes "Link to this heading")

AppConfig.name[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.name "Link to this definition")

Full Python path to the application, e.g. `'django.contrib.admin'`.
This attribute defines which application the configuration applies to. It must be set in all [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") subclasses.
It must be unique across a Django project.

AppConfig.label[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.label "Link to this definition")

Short name for the application, e.g. `'admin'`
This attribute allows relabeling an application when two applications have conflicting labels. It defaults to the last component of `name`. It should be a valid Python identifier.
It must be unique across a Django project.
Warning
Changing this attribute after migrations have been applied for an application will result in breaking changes to a project or, in the case of a reusable app, any existing installs of that app. This is because `AppConfig.label` is used in database tables and migration files when referencing an app in the dependencies list.

AppConfig.verbose_name[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.verbose_name "Link to this definition")

Human-readable name for the application, e.g. “Administration”.
This attribute defaults to `label.title()`.

AppConfig.path[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.path "Link to this definition")

Filesystem path to the application directory, e.g. `'/usr/lib/pythonX.Y/dist-packages/django/contrib/admin'`.
In most cases, Django can automatically detect and set this, but you can also provide an explicit override as a class attribute on your [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") subclass. In a few situations this is required; for instance if the app package is a [namespace package](https://docs.djangoproject.com/en/5.0/ref/applications/#namespace-package) with multiple paths.

AppConfig.default[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.default "Link to this definition")

Set this attribute to `False` to prevent Django from selecting a configuration class automatically. This is useful when `apps.py` defines only one [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") subclass but you don’t want Django to use it by default.
Set this attribute to `True` to tell Django to select a configuration class automatically. This is useful when `apps.py` defines more than one [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") subclass and you want Django to use one of them by default.
By default, this attribute isn’t set.

AppConfig.default_auto_field[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.default_auto_field "Link to this definition")

The implicit primary key type to add to models within this app. You can use this to keep [`AutoField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.AutoField "django.db.models.AutoField") as the primary key type for third party applications.
By default, this is the value of [`DEFAULT_AUTO_FIELD`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEFAULT_AUTO_FIELD).
### Read-only attributes[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#read-only-attributes "Link to this heading")

AppConfig.module[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.module "Link to this definition")

Root module for the application, e.g. `<module 'django.contrib.admin' from 'django/contrib/admin/__init__.py'>`.

AppConfig.models_module[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.models_module "Link to this definition")

Module containing the models, e.g. `<module 'django.contrib.admin.models' from 'django/contrib/admin/models.py'>`.
It may be `None` if the application doesn’t contain a `models` module. Note that the database related signals such as [`pre_migrate`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.pre_migrate "django.db.models.signals.pre_migrate") and [`post_migrate`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.post_migrate "django.db.models.signals.post_migrate") are only emitted for applications that have a `models` module.
### Methods[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#methods "Link to this heading")

AppConfig.get_models(_include_auto_created =False_, _include_swapped =False_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/apps/config/#AppConfig.get_models)[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.get_models "Link to this definition")

Returns an iterable of [`Model`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model "django.db.models.Model") classes for this application.
Requires the app registry to be fully populated.

AppConfig.get_model(_model_name_ , _require_ready =True_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/apps/config/#AppConfig.get_model)[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.get_model "Link to this definition")

Returns the [`Model`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model "django.db.models.Model") with the given `model_name`. `model_name` is case-insensitive.
Raises
Requires the app registry to be fully populated unless the `require_ready` argument is set to `False`. `require_ready` behaves exactly as in [`apps.get_model()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps.get_model "django.apps.apps.get_model").

AppConfig.ready()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/apps/config/#AppConfig.ready)[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.ready "Link to this definition")

Subclasses can override this method to perform initialization tasks such as registering signals. It is called as soon as the registry is fully populated.
Although you can’t import models at the module-level where [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") classes are defined, you can import them in `ready()`, using either an `import` statement or [`get_model()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.get_model "django.apps.AppConfig.get_model").
If you’re registering [`model signals`](https://docs.djangoproject.com/en/5.0/ref/signals/#module-django.db.models.signals "django.db.models.signals: Signals sent by the model system."), you can refer to the sender by its string label instead of using the model class itself.
Example:
```
from django.apps import AppConfig
from django.db.models.signals import pre_save


class RockNRollConfig(AppConfig):
    # ...

    def ready(self):
        # importing model classes
        from .models import MyModel  # or...

        MyModel = self.get_model("MyModel")

        # registering signals with the model's string label
        pre_save.connect(receiver, sender="app_label.MyModel")

```

Warning
Although you can access model classes as described above, avoid interacting with the database in your [`ready()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.ready "django.apps.AppConfig.ready") implementation. This includes model methods that execute queries ([`save()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save"), [`delete()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.delete "django.db.models.Model.delete"), manager methods etc.), and also raw SQL queries via `django.db.connection`. Your [`ready()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.ready "django.apps.AppConfig.ready") method will run during startup of every management command. For example, even though the test database configuration is separate from the production settings, `manage.py test` would still execute some queries against your **production** database!
Note
In the usual initialization process, the `ready` method is only called once by Django. But in some corner cases, particularly in tests which are fiddling with installed applications, `ready` might be called more than once. In that case, either write idempotent methods, or put a flag on your `AppConfig` classes to prevent rerunning code which should be executed exactly one time.
### Namespace packages as apps[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#namespace-packages-as-apps "Link to this heading")
Python packages without an `__init__.py` file are known as “namespace packages” and may be spread across multiple directories at different locations on `sys.path` (see
Django applications require a single base filesystem path where Django (depending on configuration) will search for templates, static assets, etc. Thus, namespace packages may only be Django applications if one of the following is true:
  1. The namespace package actually has only a single location (i.e. is not spread across more than one directory.)
  2. The [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") class used to configure the application has a [`path`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.path "django.apps.AppConfig.path") class attribute, which is the absolute directory path Django will use as the single base path for the application.


If neither of these conditions is met, Django will raise [`ImproperlyConfigured`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.ImproperlyConfigured "django.core.exceptions.ImproperlyConfigured").
## Application registry[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#application-registry "Link to this heading")

apps[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps "Link to this definition")

The application registry provides the following public API. Methods that aren’t listed below are considered private and may change without notice.

apps.ready[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps.ready "Link to this definition")

Boolean attribute that is set to `True` after the registry is fully populated and all [`AppConfig.ready()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.ready "django.apps.AppConfig.ready") methods are called.

apps.get_app_configs()[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps.get_app_configs "Link to this definition")

Returns an iterable of [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") instances.

apps.get_app_config(_app_label_)[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps.get_app_config "Link to this definition")

Returns an [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") for the application with the given `app_label`. Raises

apps.is_installed(_app_name_)[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps.is_installed "Link to this definition")

Checks whether an application with the given name exists in the registry. `app_name` is the full name of the app, e.g. `'django.contrib.admin'`.

apps.get_model(_app_label_ , _model_name_ , _require_ready =True_)[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps.get_model "Link to this definition")

Returns the [`Model`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model "django.db.models.Model") with the given `app_label` and `model_name`. As a shortcut, this method also accepts a single argument in the form `app_label.model_name`. `model_name` is case-insensitive.
Raises
Requires the app registry to be fully populated unless the `require_ready` argument is set to `False`.
Setting `require_ready` to `False` allows looking up models [while the app registry is being populated](https://docs.djangoproject.com/en/5.0/ref/applications/#app-loading-process), specifically during the second phase where it imports models. Then `get_model()` has the same effect as importing the model. The main use case is to configure model classes with settings, such as [`AUTH_USER_MODEL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-AUTH_USER_MODEL).
When `require_ready` is `False`, `get_model()` returns a model class that may not be fully functional (reverse accessors may be missing, for example) until the app registry is fully populated. For this reason, it’s best to leave `require_ready` to the default value of `True` whenever possible.
## Initialization process[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#initialization-process "Link to this heading")
### How applications are loaded[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#how-applications-are-loaded "Link to this heading")
When Django starts, [`django.setup()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.setup "django.setup") is responsible for populating the application registry.

setup(_set_prefix =True_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/#setup)[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#django.setup "Link to this definition")

Configures Django by:
  * Loading the settings.
  * Setting up logging.
  * If `set_prefix` is True, setting the URL resolver script prefix to [`FORCE_SCRIPT_NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-FORCE_SCRIPT_NAME) if defined, or `/` otherwise.
  * Initializing the application registry.


This function is called automatically:
  * When running an HTTP server via Django’s ASGI or WSGI support.
  * When invoking a management command.


It must be called explicitly in other cases, for instance in plain Python scripts.
Changed in Django 5.0:
Raises a `RuntimeWarning` when apps interact with the database before the app registry has been fully populated.
The application registry is initialized in three stages. At each stage, Django processes all applications in the order of [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS).
  1. First Django imports each item in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS).
If it’s an application configuration class, Django imports the root package of the application, defined by its [`name`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.name "django.apps.AppConfig.name") attribute. If it’s a Python package, Django looks for an application configuration in an `apps.py` submodule, or else creates a default application configuration.
_At this stage, your code shouldn’t import any models!_
In other words, your applications’ root packages and the modules that define your application configuration classes shouldn’t import any models, even indirectly.
Strictly speaking, Django allows importing models once their application configuration is loaded. However, in order to avoid needless constraints on the order of [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS), it’s strongly recommended not import any models at this stage.
Once this stage completes, APIs that operate on application configurations such as [`get_app_config()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps.get_app_config "django.apps.apps.get_app_config") become usable.
  2. Then Django attempts to import the `models` submodule of each application, if there is one.
You must define or import all models in your application’s `models.py` or `models/__init__.py`. Otherwise, the application registry may not be fully populated at this point, which could cause the ORM to malfunction.
Once this stage completes, APIs that operate on models such as [`get_model()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps.get_model "django.apps.apps.get_model") become usable.
  3. Finally Django runs the [`ready()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.ready "django.apps.AppConfig.ready") method of each application configuration.


### Troubleshooting[¶](https://docs.djangoproject.com/en/5.0/ref/applications/#troubleshooting "Link to this heading")
Here are some common problems that you may encounter during initialization:
  * [`AppRegistryNotReady`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.AppRegistryNotReady "django.core.exceptions.AppRegistryNotReady"): This happens when importing an application configuration or a models module triggers code that depends on the app registry.
For example, [`gettext()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.gettext "django.utils.translation.gettext") uses the app registry to look up translation catalogs in applications. To translate at import time, you need [`gettext_lazy()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.gettext_lazy "django.utils.translation.gettext_lazy") instead. (Using [`gettext()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.gettext "django.utils.translation.gettext") would be a bug, because the translation would happen at import time, rather than at each request depending on the active language.)
Executing database queries with the ORM at import time in models modules will also trigger this exception. The ORM cannot function properly until all models are available.
This exception also happens if you forget to call [`django.setup()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.setup "django.setup") in a standalone Python script.
  * `ImportError: cannot import name ...` This happens if the import sequence ends up in a loop.
To eliminate such problems, you should minimize dependencies between your models modules and do as little work as possible at import time. To avoid executing code at import time, you can move it into a function and cache its results. The code will be executed when you first need its results. This concept is known as “lazy evaluation”.
  * `django.contrib.admin` automatically performs autodiscovery of `admin` modules in installed applications. To prevent it, change your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) to contain `'django.contrib.admin.apps.SimpleAdminConfig'` instead of `'django.contrib.admin'`.
  * `RuntimeWarning: Accessing the database during app initialization is discouraged.` This warning is triggered for database queries executed before apps are ready, such as during module imports or in the [`AppConfig.ready()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.ready "django.apps.AppConfig.ready") method. Such premature database queries are discouraged because they will run during the startup of every management command, which will slow down your project startup, potentially cache stale data, and can even fail if migrations are pending.
For example, a common mistake is making a database query to populate form field choices:
```
class LocationForm(forms.Form):
    country = forms.ChoiceField(choices=[c.name for c in Country.objects.all()])

```

In the example above, the query from `Country.objects.all()` is executed during module import, because the `QuerySet` is iterated over. To avoid the warning, the form could use a [`ModelChoiceField`](https://docs.djangoproject.com/en/5.0/ref/forms/fields/#django.forms.ModelChoiceField "django.forms.ModelChoiceField") instead:
```
class LocationForm(forms.Form):
    country = forms.ModelChoiceField(queryset=Country.objects.all())

```

To make it easier to find the code that triggered this warning, you can make Python `python -Werror manage.py shell`.

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/)
[System check framework ](https://docs.djangoproject.com/en/5.0/ref/checks/)
[](https://docs.djangoproject.com/en/5.0/ref/applications/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Hooshyar Naraghi donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Applications](https://docs.djangoproject.com/en/5.0/ref/applications/)
    * [Projects and applications](https://docs.djangoproject.com/en/5.0/ref/applications/#projects-and-applications)
    * [Configuring applications](https://docs.djangoproject.com/en/5.0/ref/applications/#configuring-applications)
      * [For application authors](https://docs.djangoproject.com/en/5.0/ref/applications/#for-application-authors)
      * [For application users](https://docs.djangoproject.com/en/5.0/ref/applications/#for-application-users)
    * [Application configuration](https://docs.djangoproject.com/en/5.0/ref/applications/#application-configuration)
      * [Configurable attributes](https://docs.djangoproject.com/en/5.0/ref/applications/#configurable-attributes)
      * [Read-only attributes](https://docs.djangoproject.com/en/5.0/ref/applications/#read-only-attributes)
      * [Methods](https://docs.djangoproject.com/en/5.0/ref/applications/#methods)
      * [Namespace packages as apps](https://docs.djangoproject.com/en/5.0/ref/applications/#namespace-packages-as-apps)
    * [Application registry](https://docs.djangoproject.com/en/5.0/ref/applications/#application-registry)
    * [Initialization process](https://docs.djangoproject.com/en/5.0/ref/applications/#initialization-process)
      * [How applications are loaded](https://docs.djangoproject.com/en/5.0/ref/applications/#how-applications-are-loaded)
      * [Troubleshooting](https://docs.djangoproject.com/en/5.0/ref/applications/#troubleshooting)


### Browse
  * Prev: [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
  * Next: [System check framework](https://docs.djangoproject.com/en/5.0/ref/checks/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * Applications


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
