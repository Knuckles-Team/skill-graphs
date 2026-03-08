This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/signals/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/signals/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/signals/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/signals/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/signals/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/signals/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/signals/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/signals/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/signals/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/signals/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/signals/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/signals/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/signals/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/signals/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/signals/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/signals/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/signals/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/signals/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/signals/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/signals/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/signals/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/signals/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/signals/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/signals/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/signals/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/signals/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/signals/)


  * [](https://docs.djangoproject.com/en/5.0/ref/signals/#top)


# Signals[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#signals "Link to this heading")
A list of all the signals that Django sends. All built-in signals are sent using the [`send()`](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal.send "django.dispatch.Signal.send") method.
See also
See the documentation on the [signal dispatcher](https://docs.djangoproject.com/en/5.0/topics/signals/) for information regarding how to register for and receive signals.
The [authentication framework](https://docs.djangoproject.com/en/5.0/topics/auth/) sends [signals when a user is logged in / out](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#topics-auth-signals).
## Model signals[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#module-django.db.models.signals "Link to this heading")
The [`django.db.models.signals`](https://docs.djangoproject.com/en/5.0/ref/signals/#module-django.db.models.signals "django.db.models.signals: Signals sent by the model system.") module defines a set of signals sent by the model system.
Warning
Signals can make your code harder to maintain. Consider implementing a helper method on a [custom manager](https://docs.djangoproject.com/en/5.0/topics/db/managers/#custom-managers), to both update your models and perform additional logic, or else [overriding model methods](https://docs.djangoproject.com/en/5.0/topics/db/models/#overriding-model-methods) before using model signals.
Warning
Many of these signals are sent by various model methods like `__init__()` or [`save()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") that you can override in your own code.
If you override these methods on your model, you must call the parent class’ methods for these signals to be sent.
Note also that Django stores signal handlers as weak references by default, so if your handler is a local function, it may be garbage collected. To prevent this, pass `weak=False` when you call the signal’s [`connect()`](https://docs.djangoproject.com/en/5.0/topics/signals/#django.dispatch.Signal.connect "django.dispatch.Signal.connect").
Note
Model signals `sender` model can be lazily referenced when connecting a receiver by specifying its full application label. For example, an `Question` model defined in the `polls` application could be referenced as `'polls.Question'`. This sort of reference can be quite handy when dealing with circular import dependencies and swappable models.
###  `pre_init`[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#pre-init "Link to this heading")

django.db.models.signals.pre_init[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.pre_init "Link to this definition")

Whenever you instantiate a Django model, this signal is sent at the beginning of the model’s `__init__()` method.
Arguments sent with this signal:

`sender`

The model class that just had an instance created.

`args`

A list of positional arguments passed to `__init__()`.

`kwargs`

A dictionary of keyword arguments passed to `__init__()`.
For example, the [tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial02/) has this line:
```
q = Question(question_text="What's new?", pub_date=timezone.now())

```

The arguments sent to a [`pre_init`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.pre_init "django.db.models.signals.pre_init") handler would be:
Argument | Value
---|---
`sender` | `Question` (the class itself)
`args` | `[]` (an empty list because there were no positional arguments passed to `__init__()`)
`kwargs` | `{'question_text': "What's new?",` `'pub_date': datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=datetime.timezone.utc)}`
###  `post_init`[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#post-init "Link to this heading")

django.db.models.signals.post_init[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.post_init "Link to this definition")

Like pre_init, but this one is sent when the `__init__()` method finishes.
Arguments sent with this signal:

`sender`

As above: the model class that just had an instance created.

`instance`

The actual instance of the model that’s just been created.
Note
[`instance._state`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model._state "django.db.models.Model._state") isn’t set before sending the `post_init` signal, so `_state` attributes always have their default values. For example, `_state.db` is `None`.
Warning
For performance reasons, you shouldn’t perform queries in receivers of `pre_init` or `post_init` signals because they would be executed for each instance returned during queryset iteration.
###  `pre_save`[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#pre-save "Link to this heading")

django.db.models.signals.pre_save[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.pre_save "Link to this definition")

This is sent at the beginning of a model’s [`save()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") method.
Arguments sent with this signal:

`sender`

The model class.

`instance`

The actual instance being saved.

`raw`

A boolean; `True` if the model is saved exactly as presented (i.e. when loading a [fixture](https://docs.djangoproject.com/en/5.0/topics/db/fixtures/#fixtures-explanation)). One should not query/modify other records in the database as the database might not be in a consistent state yet.

`using`

The database alias being used.

`update_fields`

The set of fields to update as passed to [`Model.save()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save"), or `None` if `update_fields` wasn’t passed to `save()`.
###  `post_save`[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#post-save "Link to this heading")

django.db.models.signals.post_save[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.post_save "Link to this definition")

Like [`pre_save`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.pre_save "django.db.models.signals.pre_save"), but sent at the end of the [`save()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") method.
Arguments sent with this signal:

`sender`

The model class.

`instance`

The actual instance being saved.

`created`

A boolean; `True` if a new record was created.

`raw`

A boolean; `True` if the model is saved exactly as presented (i.e. when loading a [fixture](https://docs.djangoproject.com/en/5.0/topics/db/fixtures/#fixtures-explanation)). One should not query/modify other records in the database as the database might not be in a consistent state yet.

`using`

The database alias being used.

`update_fields`

The set of fields to update as passed to [`Model.save()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save"), or `None` if `update_fields` wasn’t passed to `save()`.
###  `pre_delete`[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#pre-delete "Link to this heading")

django.db.models.signals.pre_delete[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.pre_delete "Link to this definition")

Sent at the beginning of a model’s [`delete()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.delete "django.db.models.Model.delete") method and a queryset’s [`delete()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.delete "django.db.models.query.QuerySet.delete") method.
Arguments sent with this signal:

`sender`

The model class.

`instance`

The actual instance being deleted.

`using`

The database alias being used.
`origin`
> The origin of the deletion being the instance of a `Model` or `QuerySet` class.
###  `post_delete`[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#post-delete "Link to this heading")

django.db.models.signals.post_delete[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.post_delete "Link to this definition")

Like [`pre_delete`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.pre_delete "django.db.models.signals.pre_delete"), but sent at the end of a model’s [`delete()`](https://docs.djangoproject.com/en/5.0/ref/models/instances/#django.db.models.Model.delete "django.db.models.Model.delete") method and a queryset’s [`delete()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.delete "django.db.models.query.QuerySet.delete") method.
Arguments sent with this signal:

`sender`

The model class.

`instance`

The actual instance being deleted.
Note that the object will no longer be in the database, so be very careful what you do with this instance.

`using`

The database alias being used.
`origin`
> The origin of the deletion being the instance of a `Model` or `QuerySet` class.
###  `m2m_changed`[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#m2m-changed "Link to this heading")

django.db.models.signals.m2m_changed[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.m2m_changed "Link to this definition")

Sent when a [`ManyToManyField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") is changed on a model instance. Strictly speaking, this is not a model signal since it is sent by the [`ManyToManyField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField"), but since it complements the [`pre_save`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.pre_save "django.db.models.signals.pre_save")/[`post_save`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.post_save "django.db.models.signals.post_save") and [`pre_delete`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.pre_delete "django.db.models.signals.pre_delete")/[`post_delete`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.post_delete "django.db.models.signals.post_delete") when it comes to tracking changes to models, it is included here.
Arguments sent with this signal:

`sender`

The intermediate model class describing the [`ManyToManyField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField"). This class is automatically created when a many-to-many field is defined; you can access it using the `through` attribute on the many-to-many field.

`instance`

The instance whose many-to-many relation is updated. This can be an instance of the `sender`, or of the class the [`ManyToManyField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") is related to.

`action`

A string indicating the type of update that is done on the relation. This can be one of the following:

`"pre_add"`

Sent _before_ one or more objects are added to the relation.

`"post_add"`

Sent _after_ one or more objects are added to the relation.

`"pre_remove"`

Sent _before_ one or more objects are removed from the relation.

`"post_remove"`

Sent _after_ one or more objects are removed from the relation.

`"pre_clear"`

Sent _before_ the relation is cleared.

`"post_clear"`

Sent _after_ the relation is cleared.

`reverse`

Indicates which side of the relation is updated (i.e., if it is the forward or reverse relation that is being modified).

`model`

The class of the objects that are added to, removed from or cleared from the relation.

`pk_set`

For the `pre_add` and `post_add` actions, this is a set of primary key values that will be, or have been, added to the relation. This may be a subset of the values submitted to be added, since inserts must filter existing values in order to avoid a database `IntegrityError`.
For the `pre_remove` and `post_remove` actions, this is a set of primary key values that was submitted to be removed from the relation. This is not dependent on whether the values actually will be, or have been, removed. In particular, non-existent values may be submitted, and will appear in `pk_set`, even though they have no effect on the database.
For the `pre_clear` and `post_clear` actions, this is `None`.

`using`

The database alias being used.
For example, if a `Pizza` can have multiple `Topping` objects, modeled like this:
```
class Topping(models.Model):
    # ...
    pass


class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)

```

If we connected a handler like this:
```
from django.db.models.signals import m2m_changed


def toppings_changed(sender, **kwargs):
    # Do something
    pass


m2m_changed.connect(toppings_changed, sender=Pizza.toppings.through)

```

and then did something like this:
```
>>> p = Pizza.objects.create(...)
>>> t = Topping.objects.create(...)
>>> p.toppings.add(t)

```

the arguments sent to a [`m2m_changed`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.m2m_changed "django.db.models.signals.m2m_changed") handler (`toppings_changed` in the example above) would be:
Argument | Value
---|---
`sender` | `Pizza.toppings.through` (the intermediate m2m class)
`instance` | `p` (the `Pizza` instance being modified)
`action` | `"pre_add"` (followed by a separate signal with `"post_add"`)
`reverse` | `False` (`Pizza` contains the [`ManyToManyField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField"), so this call modifies the forward relation)
`model` | `Topping` (the class of the objects added to the `Pizza`)
`pk_set` | `{t.id}` (since only `Topping t` was added to the relation)
`using` | `"default"` (since the default router sends writes here)
And if we would then do something like this:
```
>>> t.pizza_set.remove(p)

```

the arguments sent to a [`m2m_changed`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.m2m_changed "django.db.models.signals.m2m_changed") handler would be:
Argument | Value
---|---
`sender` | `Pizza.toppings.through` (the intermediate m2m class)
`instance` | `t` (the `Topping` instance being modified)
`action` | `"pre_remove"` (followed by a separate signal with `"post_remove"`)
`reverse` | `True` (`Pizza` contains the [`ManyToManyField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField"), so this call modifies the reverse relation)
`model` | `Pizza` (the class of the objects removed from the `Topping`)
`pk_set` | `{p.id}` (since only `Pizza p` was removed from the relation)
`using` | `"default"` (since the default router sends writes here)
###  `class_prepared`[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#class-prepared "Link to this heading")

django.db.models.signals.class_prepared[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.class_prepared "Link to this definition")

Sent whenever a model class has been “prepared” – that is, once a model has been defined and registered with Django’s model system. Django uses this signal internally; it’s not generally used in third-party applications.
Since this signal is sent during the app registry population process, and [`AppConfig.ready()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.ready "django.apps.AppConfig.ready") runs after the app registry is fully populated, receivers cannot be connected in that method. One possibility is to connect them `AppConfig.__init__()` instead, taking care not to import models or trigger calls to the app registry.
Arguments that are sent with this signal:

`sender`

The model class which was just prepared.
## Management signals[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#management-signals "Link to this heading")
Signals sent by [django-admin](https://docs.djangoproject.com/en/5.0/ref/django-admin/).
###  `pre_migrate`[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#pre-migrate "Link to this heading")

django.db.models.signals.pre_migrate[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.pre_migrate "Link to this definition")

Sent by the [`migrate`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-migrate) command before it starts to install an application. It’s not emitted for applications that lack a `models` module.
Arguments sent with this signal:

`sender`

An [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") instance for the application about to be migrated/synced.

`app_config`

Same as `sender`.

`verbosity`

Indicates how much information `manage.py` is printing on screen. See the [`--verbosity`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-verbosity) flag for details.
Functions which listen for [`pre_migrate`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.pre_migrate "django.db.models.signals.pre_migrate") should adjust what they output to the screen based on the value of this argument.

`interactive`

If `interactive` is `True`, it’s safe to prompt the user to input things on the command line. If `interactive` is `False`, functions which listen for this signal should not try to prompt for anything.
For example, the [`django.contrib.auth`](https://docs.djangoproject.com/en/5.0/topics/auth/#module-django.contrib.auth "django.contrib.auth: Django's authentication framework.") app only prompts to create a superuser when `interactive` is `True`.

`stdout`

A stream-like object where verbose output should be redirected.

`using`

The alias of database on which a command will operate.

`plan`

The migration plan that is going to be used for the migration run. While the plan is not public API, this allows for the rare cases when it is necessary to know the plan. A plan is a list of 2-tuples with the first item being the instance of a migration class and the second item showing if the migration was rolled back (`True`) or applied (`False`).

`apps`

An instance of [`Apps`](https://docs.djangoproject.com/en/5.0/ref/applications/#module-django.apps "django.apps") containing the state of the project before the migration run. It should be used instead of the global [`apps`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps "django.apps.apps") registry to retrieve the models you want to perform operations on.
###  `post_migrate`[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#post-migrate "Link to this heading")

django.db.models.signals.post_migrate[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.post_migrate "Link to this definition")

Sent at the end of the [`migrate`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-migrate) (even if no migrations are run) and [`flush`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-flush) commands. It’s not emitted for applications that lack a `models` module.
Handlers of this signal must not perform database schema alterations as doing so may cause the [`flush`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-flush) command to fail if it runs during the [`migrate`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-migrate) command.
Arguments sent with this signal:

`sender`

An [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") instance for the application that was just installed.

`app_config`

Same as `sender`.

`verbosity`

Indicates how much information `manage.py` is printing on screen. See the [`--verbosity`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-verbosity) flag for details.
Functions which listen for [`post_migrate`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.post_migrate "django.db.models.signals.post_migrate") should adjust what they output to the screen based on the value of this argument.

`interactive`

If `interactive` is `True`, it’s safe to prompt the user to input things on the command line. If `interactive` is `False`, functions which listen for this signal should not try to prompt for anything.
For example, the [`django.contrib.auth`](https://docs.djangoproject.com/en/5.0/topics/auth/#module-django.contrib.auth "django.contrib.auth: Django's authentication framework.") app only prompts to create a superuser when `interactive` is `True`.

`stdout`

A stream-like object where verbose output should be redirected.

`using`

The database alias used for synchronization. Defaults to the `default` database.

`plan`

The migration plan that was used for the migration run. While the plan is not public API, this allows for the rare cases when it is necessary to know the plan. A plan is a list of 2-tuples with the first item being the instance of a migration class and the second item showing if the migration was rolled back (`True`) or applied (`False`).

`apps`

An instance of [`Apps`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps "django.apps.apps") containing the state of the project after the migration run. It should be used instead of the global [`apps`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps "django.apps.apps") registry to retrieve the models you want to perform operations on.
For example, you could register a callback in an [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") like this:
```
from django.apps import AppConfig
from django.db.models.signals import post_migrate


def my_callback(sender, **kwargs):
    # Your specific logic here
    pass


class MyAppConfig(AppConfig):
    ...

    def ready(self):
        post_migrate.connect(my_callback, sender=self)

```

Note
If you provide an [`AppConfig`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig "django.apps.AppConfig") instance as the sender argument, please ensure that the signal is registered in [`ready()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.ready "django.apps.AppConfig.ready"). `AppConfig`s are recreated for tests that run with a modified set of [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS) (such as when settings are overridden) and such signals should be connected for each new `AppConfig` instance.
## Request/response signals[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#module-django.core.signals "Link to this heading")
Signals sent by the core framework when processing a request.
Warning
Signals can make your code harder to maintain. Consider [using a middleware](https://docs.djangoproject.com/en/5.0/topics/http/middleware/) before using request/response signals.
###  `request_started`[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#request-started "Link to this heading")

django.core.signals.request_started[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#django.core.signals.request_started "Link to this definition")

Sent when Django begins processing an HTTP request.
Arguments sent with this signal:

`sender`

The handler class – e.g. `django.core.handlers.wsgi.WsgiHandler` – that handled the request.

`environ`

The `environ` dictionary provided to the request.
###  `request_finished`[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#request-finished "Link to this heading")

django.core.signals.request_finished[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#django.core.signals.request_finished "Link to this definition")

Sent when Django finishes delivering an HTTP response to the client.
Arguments sent with this signal:

`sender`

The handler class, as above.
###  `got_request_exception`[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#got-request-exception "Link to this heading")

django.core.signals.got_request_exception[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#django.core.signals.got_request_exception "Link to this definition")

This signal is sent whenever Django encounters an exception while processing an incoming HTTP request.
Arguments sent with this signal:

`sender`

Unused (always `None`).

`request`

The [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") object.
## Test signals[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#module-django.test.signals "Link to this heading")
Signals only sent when [running tests](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#running-tests).
###  `setting_changed`[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#setting-changed "Link to this heading")

django.test.signals.setting_changed[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#django.test.signals.setting_changed "Link to this definition")

This signal is sent when the value of a setting is changed through the `django.test.TestCase.settings()` context manager or the [`django.test.override_settings()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.override_settings "django.test.override_settings") decorator/context manager.
It’s actually sent twice: when the new value is applied (“setup”) and when the original value is restored (“teardown”). Use the `enter` argument to distinguish between the two.
You can also import this signal from `django.core.signals` to avoid importing from `django.test` in non-test situations.
Arguments sent with this signal:

`sender`

The settings handler.

`setting`

The name of the setting.

`value`

The value of the setting after the change. For settings that initially don’t exist, in the “teardown” phase, `value` is `None`.

`enter`

A boolean; `True` if the setting is applied, `False` if restored.
###  `template_rendered`[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#template-rendered "Link to this heading")

django.test.signals.template_rendered[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#django.test.signals.template_rendered "Link to this definition")

Sent when the test system renders a template. This signal is not emitted during normal operation of a Django server – it is only available during testing.
Arguments sent with this signal:

`sender`

The [`Template`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.Template "django.template.Template") object which was rendered.

`template`

Same as sender

`context`

The [`Context`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.Context "django.template.Context") with which the template was rendered.
## Database Wrappers[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#module-django.db.backends "Link to this heading")
Signals sent by the database wrapper when a database connection is initiated.
###  `connection_created`[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#connection-created "Link to this heading")

django.db.backends.signals.connection_created[¶](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.backends.signals.connection_created "Link to this definition")

Sent when the database wrapper makes the initial connection to the database. This is particularly useful if you’d like to send any post connection commands to the SQL backend.
Arguments sent with this signal:

`sender`

The database wrapper class – i.e. `django.db.backends.postgresql.DatabaseWrapper` or `django.db.backends.mysql.DatabaseWrapper`, etc.

`connection`

The database connection that was opened. This can be used in a multiple-database configuration to differentiate connection signals from different databases. Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/settings/)
[Templates ](https://docs.djangoproject.com/en/5.0/ref/templates/)
[](https://docs.djangoproject.com/en/5.0/ref/signals/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Henrique Taunay donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Signals](https://docs.djangoproject.com/en/5.0/ref/signals/)
    * [Model signals](https://docs.djangoproject.com/en/5.0/ref/signals/#module-django.db.models.signals)
      * [`pre_init`](https://docs.djangoproject.com/en/5.0/ref/signals/#pre-init)
      * [`post_init`](https://docs.djangoproject.com/en/5.0/ref/signals/#post-init)
      * [`pre_save`](https://docs.djangoproject.com/en/5.0/ref/signals/#pre-save)
      * [`post_save`](https://docs.djangoproject.com/en/5.0/ref/signals/#post-save)
      * [`pre_delete`](https://docs.djangoproject.com/en/5.0/ref/signals/#pre-delete)
      * [`post_delete`](https://docs.djangoproject.com/en/5.0/ref/signals/#post-delete)
      * [`m2m_changed`](https://docs.djangoproject.com/en/5.0/ref/signals/#m2m-changed)
      * [`class_prepared`](https://docs.djangoproject.com/en/5.0/ref/signals/#class-prepared)
    * [Management signals](https://docs.djangoproject.com/en/5.0/ref/signals/#management-signals)
      * [`pre_migrate`](https://docs.djangoproject.com/en/5.0/ref/signals/#pre-migrate)
      * [`post_migrate`](https://docs.djangoproject.com/en/5.0/ref/signals/#post-migrate)
    * [Request/response signals](https://docs.djangoproject.com/en/5.0/ref/signals/#module-django.core.signals)
      * [`request_started`](https://docs.djangoproject.com/en/5.0/ref/signals/#request-started)
      * [`request_finished`](https://docs.djangoproject.com/en/5.0/ref/signals/#request-finished)
      * [`got_request_exception`](https://docs.djangoproject.com/en/5.0/ref/signals/#got-request-exception)
    * [Test signals](https://docs.djangoproject.com/en/5.0/ref/signals/#module-django.test.signals)
      * [`setting_changed`](https://docs.djangoproject.com/en/5.0/ref/signals/#setting-changed)
      * [`template_rendered`](https://docs.djangoproject.com/en/5.0/ref/signals/#template-rendered)
    * [Database Wrappers](https://docs.djangoproject.com/en/5.0/ref/signals/#module-django.db.backends)
      * [`connection_created`](https://docs.djangoproject.com/en/5.0/ref/signals/#connection-created)


### Browse
  * Prev: [Settings](https://docs.djangoproject.com/en/5.0/ref/settings/)
  * Next: [Templates](https://docs.djangoproject.com/en/5.0/ref/templates/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * Signals


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
