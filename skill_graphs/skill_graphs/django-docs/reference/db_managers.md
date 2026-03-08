This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/db/managers/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/db/managers/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/db/managers/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/db/managers/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/db/managers/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/db/managers/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/db/managers/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/db/managers/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/db/managers/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/db/managers/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/db/managers/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/db/managers/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/db/managers/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/db/managers/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/db/managers/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/db/managers/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/db/managers/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/db/managers/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/db/managers/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/db/managers/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/db/managers/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/db/managers/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/db/managers/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/db/managers/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/db/managers/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/db/managers/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/db/managers/)


  * [](https://docs.djangoproject.com/en/5.0/topics/db/managers/#top)


# Managers[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#managers "Link to this heading")

_class_ Manager[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/models/manager/#Manager)[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Manager "Link to this definition")

A `Manager` is the interface through which database query operations are provided to Django models. At least one `Manager` exists for every model in a Django application.
The way `Manager` classes work is documented in [Making queries](https://docs.djangoproject.com/en/5.0/topics/db/queries/); this document specifically touches on model options that customize `Manager` behavior.
## Manager names[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#manager-names "Link to this heading")
By default, Django adds a `Manager` with the name `objects` to every Django model class. However, if you want to use `objects` as a field name, or if you want to use a name other than `objects` for the `Manager`, you can rename it on a per-model basis. To rename the `Manager` for a given class, define a class attribute of type `models.Manager()` on that model. For example:
```
from django.db import models


class Person(models.Model):
    # ...
    people = models.Manager()

```

Using this example model, `Person.objects` will generate an `AttributeError` exception, but `Person.people.all()` will provide a list of all `Person` objects.
## Custom managers[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#custom-managers "Link to this heading")
You can use a custom `Manager` in a particular model by extending the base `Manager` class and instantiating your custom `Manager` in your model.
There are two reasons you might want to customize a `Manager`: to add extra `Manager` methods, and/or to modify the initial `QuerySet` the `Manager` returns.
### Adding extra manager methods[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#adding-extra-manager-methods "Link to this heading")
Adding extra `Manager` methods is the preferred way to add “table-level” functionality to your models. (For “row-level” functionality – i.e., functions that act on a single instance of a model object – use [Model methods](https://docs.djangoproject.com/en/5.0/topics/db/models/#model-methods), not custom `Manager` methods.)
For example, this custom `Manager` adds a method `with_counts()`:
```
from django.db import models
from django.db.models.functions import Coalesce


class PollManager(models.Manager):
    def with_counts(self):
        return self.annotate(num_responses=Coalesce(models.Count("response"), 0))


class OpinionPoll(models.Model):
    question = models.CharField(max_length=200)
    objects = PollManager()


class Response(models.Model):
    poll = models.ForeignKey(OpinionPoll, on_delete=models.CASCADE)
    # ...

```

With this example, you’d use `OpinionPoll.objects.with_counts()` to get a `QuerySet` of `OpinionPoll` objects with the extra `num_responses` attribute attached.
A custom `Manager` method can return anything you want. It doesn’t have to return a `QuerySet`.
Another thing to note is that `Manager` methods can access `self.model` to get the model class to which they’re attached.
### Modifying a manager’s initial `QuerySet`[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#modifying-a-manager-s-initial-queryset "Link to this heading")
A `Manager`’s base `QuerySet` returns all objects in the system. For example, using this model:
```
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

```

…the statement `Book.objects.all()` will return all books in the database.
You can override a `Manager`’s base `QuerySet` by overriding the `Manager.get_queryset()` method. `get_queryset()` should return a `QuerySet` with the properties you require.
For example, the following model has _two_ `Manager`s – one that returns all objects, and one that returns only the books by Roald Dahl:
```
# First, define the Manager subclass.
class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author="Roald Dahl")


# Then hook it into the Book model explicitly.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    objects = models.Manager()  # The default manager.
    dahl_objects = DahlBookManager()  # The Dahl-specific manager.

```

With this sample model, `Book.objects.all()` will return all books in the database, but `Book.dahl_objects.all()` will only return the ones written by Roald Dahl.
Because `get_queryset()` returns a `QuerySet` object, you can use `filter()`, `exclude()` and all the other `QuerySet` methods on it. So these statements are all legal:
```
Book.dahl_objects.all()
Book.dahl_objects.filter(title="Matilda")
Book.dahl_objects.count()

```

This example also pointed out another interesting technique: using multiple managers on the same model. You can attach as many `Manager()` instances to a model as you’d like. This is a non-repetitive way to define common “filters” for your models.
For example:
```
class AuthorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role="A")


class EditorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role="E")


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices={"A": _("Author"), "E": _("Editor")})
    people = models.Manager()
    authors = AuthorManager()
    editors = EditorManager()

```

This example allows you to request `Person.authors.all()`, `Person.editors.all()`, and `Person.people.all()`, yielding predictable results.
### Default managers[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#default-managers "Link to this heading")

Model._default_manager[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Model._default_manager "Link to this definition")

If you use custom `Manager` objects, take note that the first `Manager` Django encounters (in the order in which they’re defined in the model) has a special status. Django interprets the first `Manager` defined in a class as the “default” `Manager`, and several parts of Django (including [`dumpdata`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-dumpdata)) will use that `Manager` exclusively for that model. As a result, it’s a good idea to be careful in your choice of default manager in order to avoid a situation where overriding `get_queryset()` results in an inability to retrieve objects you’d like to work with.
You can specify a custom default manager using [`Meta.default_manager_name`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.default_manager_name "django.db.models.Options.default_manager_name").
If you’re writing some code that must handle an unknown model, for example, in a third-party app that implements a generic view, use this manager (or [`_base_manager`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Model._base_manager "django.db.models.Model._base_manager")) rather than assuming the model has an `objects` manager.
### Base managers[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#base-managers "Link to this heading")

Model._base_manager[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Model._base_manager "Link to this definition")

#### Using managers for related object access[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#using-managers-for-related-object-access "Link to this heading")
By default, Django uses an instance of the `Model._base_manager` manager class when accessing related objects (i.e. `choice.question`), not the `_default_manager` on the related object. This is because Django needs to be able to retrieve the related object, even if it would otherwise be filtered out (and hence be inaccessible) by the default manager.
If the normal base manager class ([`django.db.models.Manager`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager")) isn’t appropriate for your circumstances, you can tell Django which class to use by setting [`Meta.base_manager_name`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.base_manager_name "django.db.models.Options.base_manager_name").
Base managers aren’t used when querying on related models, or when [accessing a one-to-many or many-to-many relationship](https://docs.djangoproject.com/en/5.0/topics/db/queries/#backwards-related-objects). For example, if the `Question` model [from the tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial02/#creating-models) had a `deleted` field and a base manager that filters out instances with `deleted=True`, a queryset like `Choice.objects.filter(question__name__startswith='What')` would include choices related to deleted questions.
#### Don’t filter away any results in this type of manager subclass[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#don-t-filter-away-any-results-in-this-type-of-manager-subclass "Link to this heading")
This manager is used to access objects that are related to from some other model. In those situations, Django has to be able to see all the objects for the model it is fetching, so that _anything_ which is referred to can be retrieved.
Therefore, you should not override `get_queryset()` to filter out any rows. If you do so, Django will return incomplete results.
### Calling custom `QuerySet` methods from the manager[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#calling-custom-queryset-methods-from-the-manager "Link to this heading")
While most methods from the standard `QuerySet` are accessible directly from the `Manager`, this is only the case for the extra methods defined on a custom `QuerySet` if you also implement them on the `Manager`:
```
class PersonQuerySet(models.QuerySet):
    def authors(self):
        return self.filter(role="A")

    def editors(self):
        return self.filter(role="E")


class PersonManager(models.Manager):
    def get_queryset(self):
        return PersonQuerySet(self.model, using=self._db)

    def authors(self):
        return self.get_queryset().authors()

    def editors(self):
        return self.get_queryset().editors()


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices={"A": _("Author"), "E": _("Editor")})
    people = PersonManager()

```

This example allows you to call both `authors()` and `editors()` directly from the manager `Person.people`.
### Creating a manager with `QuerySet` methods[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#creating-a-manager-with-queryset-methods "Link to this heading")
In lieu of the above approach which requires duplicating methods on both the `QuerySet` and the `Manager`, [`QuerySet.as_manager()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.as_manager "django.db.models.query.QuerySet.as_manager") can be used to create an instance of `Manager` with a copy of a custom `QuerySet`’s methods:
```
class Person(models.Model):
    ...
    people = PersonQuerySet.as_manager()

```

The `Manager` instance created by [`QuerySet.as_manager()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.as_manager "django.db.models.query.QuerySet.as_manager") will be virtually identical to the `PersonManager` from the previous example.
Not every `QuerySet` method makes sense at the `Manager` level; for instance we intentionally prevent the [`QuerySet.delete()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.delete "django.db.models.query.QuerySet.delete") method from being copied onto the `Manager` class.
Methods are copied according to the following rules:
  * Public methods are copied by default.
  * Private methods (starting with an underscore) are not copied by default.
  * Methods with a `queryset_only` attribute set to `False` are always copied.
  * Methods with a `queryset_only` attribute set to `True` are never copied.


For example:
```
class CustomQuerySet(models.QuerySet):
    # Available on both Manager and QuerySet.
    def public_method(self):
        return

    # Available only on QuerySet.
    def _private_method(self):
        return

    # Available only on QuerySet.
    def opted_out_public_method(self):
        return

    opted_out_public_method.queryset_only = True

    # Available on both Manager and QuerySet.
    def _opted_in_private_method(self):
        return

    _opted_in_private_method.queryset_only = False

```

####  `from_queryset()`[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#from-queryset "Link to this heading")

_classmethod_ from_queryset(_queryset_class_)[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.from_queryset "Link to this definition")

For advanced usage you might want both a custom `Manager` and a custom `QuerySet`. You can do that by calling `Manager.from_queryset()` which returns a _subclass_ of your base `Manager` with a copy of the custom `QuerySet` methods:
```
class CustomManager(models.Manager):
    def manager_only_method(self):
        return


class CustomQuerySet(models.QuerySet):
    def manager_and_queryset_method(self):
        return


class MyModel(models.Model):
    objects = CustomManager.from_queryset(CustomQuerySet)()

```

You may also store the generated class into a variable:
```
MyManager = CustomManager.from_queryset(CustomQuerySet)


class MyModel(models.Model):
    objects = MyManager()

```

### Custom managers and model inheritance[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#custom-managers-and-model-inheritance "Link to this heading")
Here’s how Django handles custom managers and [model inheritance](https://docs.djangoproject.com/en/5.0/topics/db/models/#model-inheritance):
  1. Managers from base classes are always inherited by the child class, using Python’s normal name resolution order (names on the child class override all others; then come names on the first parent class, and so on).
  2. If no managers are declared on a model and/or its parents, Django automatically creates the `objects` manager.
  3. The default manager on a class is either the one chosen with [`Meta.default_manager_name`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.default_manager_name "django.db.models.Options.default_manager_name"), or the first manager declared on the model, or the default manager of the first parent model.


These rules provide the necessary flexibility if you want to install a collection of custom managers on a group of models, via an abstract base class, but still customize the default manager. For example, suppose you have this base class:
```
class AbstractBase(models.Model):
    # ...
    objects = CustomManager()

    class Meta:
        abstract = True

```

If you use this directly in a child class, `objects` will be the default manager if you declare no managers in the child class:
```
class ChildA(AbstractBase):
    # ...
    # This class has CustomManager as the default manager.
    pass

```

If you want to inherit from `AbstractBase`, but provide a different default manager, you can provide the default manager on the child class:
```
class ChildB(AbstractBase):
    # ...
    # An explicit default manager.
    default_manager = OtherManager()

```

Here, `default_manager` is the default. The `objects` manager is still available, since it’s inherited, but isn’t used as the default.
Finally for this example, suppose you want to add extra managers to the child class, but still use the default from `AbstractBase`. You can’t add the new manager directly in the child class, as that would override the default and you would have to also explicitly include all the managers from the abstract base class. The solution is to put the extra managers in another base class and introduce it into the inheritance hierarchy _after_ the defaults:
```
class ExtraManager(models.Model):
    extra_manager = OtherManager()

    class Meta:
        abstract = True


class ChildC(AbstractBase, ExtraManager):
    # ...
    # Default manager is CustomManager, but OtherManager is
    # also available via the "extra_manager" attribute.
    pass

```

Note that while you can _define_ a custom manager on the abstract model, you can’t _invoke_ any methods using the abstract model. That is:
```
ClassA.objects.do_something()

```

is legal, but:
```
AbstractBase.objects.do_something()

```

will raise an exception. This is because managers are intended to encapsulate logic for managing collections of objects. Since you can’t have a collection of abstract objects, it doesn’t make sense to be managing them. If you have functionality that applies to the abstract model, you should put that functionality in a `staticmethod` or `classmethod` on the abstract model.
### Implementation concerns[¶](https://docs.djangoproject.com/en/5.0/topics/db/managers/#implementation-concerns "Link to this heading")
Whatever features you add to your custom `Manager`, it must be possible to make a shallow copy of a `Manager` instance; i.e., the following code must work:
```
>>> import copy
>>> manager = MyManager()
>>> my_copy = copy.copy(manager)

```

Django makes shallow copies of manager objects during certain queries; if your Manager cannot be copied, those queries will fail.
This won’t be an issue for most custom managers. If you are just adding simple methods to your `Manager`, it is unlikely that you will inadvertently make instances of your `Manager` uncopyable. However, if you’re overriding `__getattr__` or some other private method of your `Manager` object that controls object state, you should ensure that you don’t affect the ability of your `Manager` to be copied.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/db/search/)
[Performing raw SQL queries ](https://docs.djangoproject.com/en/5.0/topics/db/sql/)
[](https://docs.djangoproject.com/en/5.0/topics/db/managers/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Mathieu Dupuy donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Managers](https://docs.djangoproject.com/en/5.0/topics/db/managers/)
    * [Manager names](https://docs.djangoproject.com/en/5.0/topics/db/managers/#manager-names)
    * [Custom managers](https://docs.djangoproject.com/en/5.0/topics/db/managers/#custom-managers)
      * [Adding extra manager methods](https://docs.djangoproject.com/en/5.0/topics/db/managers/#adding-extra-manager-methods)
      * [Modifying a manager’s initial `QuerySet`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#modifying-a-manager-s-initial-queryset)
      * [Default managers](https://docs.djangoproject.com/en/5.0/topics/db/managers/#default-managers)
      * [Base managers](https://docs.djangoproject.com/en/5.0/topics/db/managers/#base-managers)
        * [Using managers for related object access](https://docs.djangoproject.com/en/5.0/topics/db/managers/#using-managers-for-related-object-access)
        * [Don’t filter away any results in this type of manager subclass](https://docs.djangoproject.com/en/5.0/topics/db/managers/#don-t-filter-away-any-results-in-this-type-of-manager-subclass)
      * [Calling custom `QuerySet` methods from the manager](https://docs.djangoproject.com/en/5.0/topics/db/managers/#calling-custom-queryset-methods-from-the-manager)
      * [Creating a manager with `QuerySet` methods](https://docs.djangoproject.com/en/5.0/topics/db/managers/#creating-a-manager-with-queryset-methods)
        * [`from_queryset()`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#from-queryset)
      * [Custom managers and model inheritance](https://docs.djangoproject.com/en/5.0/topics/db/managers/#custom-managers-and-model-inheritance)
      * [Implementation concerns](https://docs.djangoproject.com/en/5.0/topics/db/managers/#implementation-concerns)


### Browse
  * Prev: [Search](https://docs.djangoproject.com/en/5.0/topics/db/search/)
  * Next: [Performing raw SQL queries](https://docs.djangoproject.com/en/5.0/topics/db/sql/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * [Models and databases](https://docs.djangoproject.com/en/5.0/topics/db/)
        * Managers


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
