[Skip to main content](https://docs.djangoproject.com/en/6.0/ref/models/options/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/ref/models/options/)
  * [sv](https://docs.djangoproject.com/sv/6.0/ref/models/options/)
  * [pt-br](https://docs.djangoproject.com/pt-br/6.0/ref/models/options/)
  * [pl](https://docs.djangoproject.com/pl/6.0/ref/models/options/)
  * [ko](https://docs.djangoproject.com/ko/6.0/ref/models/options/)
  * [ja](https://docs.djangoproject.com/ja/6.0/ref/models/options/)
  * [it](https://docs.djangoproject.com/it/6.0/ref/models/options/)
  * [id](https://docs.djangoproject.com/id/6.0/ref/models/options/)
  * [fr](https://docs.djangoproject.com/fr/6.0/ref/models/options/)
  * [es](https://docs.djangoproject.com/es/6.0/ref/models/options/)
  * [el](https://docs.djangoproject.com/el/6.0/ref/models/options/)


  * Documentation version: **6.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/models/options/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/models/options/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/models/options/)
  * [5.0](https://docs.djangoproject.com/en/5.0/ref/models/options/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/models/options/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/models/options/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/models/options/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/models/options/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/models/options/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/models/options/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/models/options/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/models/options/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/models/options/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/models/options/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/models/options/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/models/options/)


  * [](https://docs.djangoproject.com/en/6.0/ref/models/options/#top)


# Model `Meta` options[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#model-meta-options "Link to this heading")
This document explains all the possible [metadata options](https://docs.djangoproject.com/en/6.0/topics/db/models/#meta-options) that you can give your model in its internal `class Meta`.
## Available `Meta` options[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#available-meta-options "Link to this heading")
###  `abstract`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#abstract "Link to this heading")

Options.abstract[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.abstract "Link to this definition")

If `abstract = True`, this model will be an [abstract base class](https://docs.djangoproject.com/en/6.0/topics/db/models/#abstract-base-classes).
###  `app_label`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#app-label "Link to this heading")

Options.app_label[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.app_label "Link to this definition")

If a model is defined outside of an application in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-INSTALLED_APPS), it must declare which app it belongs to:
```
app_label = "myapp"

```

If you want to represent a model with the format `app_label.object_name` or `app_label.model_name` you can use `model._meta.label` or `model._meta.label_lower` respectively.
###  `base_manager_name`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#base-manager-name "Link to this heading")

Options.base_manager_name[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.base_manager_name "Link to this definition")

The attribute name of the manager, for example, `'objects'`, to use for the model’s [`_base_manager`](https://docs.djangoproject.com/en/6.0/topics/db/managers/#django.db.models.Model._base_manager "django.db.models.Model._base_manager").
###  `db_table`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#db-table "Link to this heading")

Options.db_table[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.db_table "Link to this definition")

The name of the database table to use for the model:
```
db_table = "music_album"

```

#### Table names[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#table-names "Link to this heading")
To save you time, Django automatically derives the name of the database table from the name of your model class and the app that contains it. A model’s database table name is constructed by joining the model’s “app label” – the name you used in [`manage.py startapp`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-startapp) – to the model’s class name, with an underscore between them.
For example, if you have an app `bookstore` (as created by `manage.py startapp bookstore`), a model defined as `class Book` will have a database table named `bookstore_book`.
To override the database table name, use the `db_table` parameter in `class Meta`.
If your database table name is an SQL reserved word, or contains characters that aren’t allowed in Python variable names – notably, the hyphen – that’s OK. Django quotes column and table names behind the scenes.
Use lowercase table names for MariaDB and MySQL
It is strongly advised that you use lowercase table names when you override the table name via `db_table`, particularly if you are using the MySQL backend. See the [MySQL notes](https://docs.djangoproject.com/en/6.0/ref/databases/#mysql-notes) for more details.
Table name quoting for Oracle
In order to meet the 30-char limitation Oracle has on table names, and match the usual conventions for Oracle databases, Django may shorten table names and turn them all-uppercase. To prevent such transformations, use a quoted name as the value for `db_table`:
```
db_table = '"name_left_in_lowercase"'

```

Such quoted names can also be used with Django’s other supported database backends; except for Oracle, however, the quotes have no effect. See the [Oracle notes](https://docs.djangoproject.com/en/6.0/ref/databases/#oracle-notes) for more details.
###  `db_table_comment`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#db-table-comment "Link to this heading")

Options.db_table_comment[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.db_table_comment "Link to this definition")

The comment on the database table to use for this model. It is useful for documenting database tables for individuals with direct database access who may not be looking at your Django code. For example:
```
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()

    class Meta:
        db_table_comment = "Question answers"

```

###  `db_tablespace`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#db-tablespace "Link to this heading")

Options.db_tablespace[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.db_tablespace "Link to this definition")

The name of the [database tablespace](https://docs.djangoproject.com/en/6.0/topics/db/tablespaces/) to use for this model. The default is the project’s [`DEFAULT_TABLESPACE`](https://docs.djangoproject.com/en/6.0/ref/settings/#std-setting-DEFAULT_TABLESPACE) setting, if set. If the backend doesn’t support tablespaces, this option is ignored.
###  `default_manager_name`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#default-manager-name "Link to this heading")

Options.default_manager_name[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.default_manager_name "Link to this definition")

The name of the manager to use for the model’s [`_default_manager`](https://docs.djangoproject.com/en/6.0/topics/db/managers/#django.db.models.Model._default_manager "django.db.models.Model._default_manager").
###  `default_related_name`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#default-related-name "Link to this heading")

Options.default_related_name[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.default_related_name "Link to this definition")

The name that will be used by default for the relation from a related object back to this one. The default is `<model_name>_set`.
This option also sets [`related_query_name`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ForeignKey.related_query_name "django.db.models.ForeignKey.related_query_name").
As the reverse name for a field should be unique, be careful if you intend to subclass your model. To work around name collisions, part of the name should contain `'%(app_label)s'` and `'%(model_name)s'`, which are replaced respectively by the name of the application the model is in, and the name of the model, both lowercased. See the paragraph on [related names for abstract models](https://docs.djangoproject.com/en/6.0/topics/db/models/#abstract-related-name).
###  `get_latest_by`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#get-latest-by "Link to this heading")

Options.get_latest_by[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.get_latest_by "Link to this definition")

The name of a field or a list of field names in the model, typically [`DateField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateField "django.db.models.DateField"), [`DateTimeField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.DateTimeField "django.db.models.DateTimeField"), or [`IntegerField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.IntegerField "django.db.models.IntegerField"). This specifies the default field(s) to use in your model [`Manager`](https://docs.djangoproject.com/en/6.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager")’s [`latest()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.latest "django.db.models.query.QuerySet.latest") and [`earliest()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.earliest "django.db.models.query.QuerySet.earliest") methods.
Example:
```
# Latest by ascending order_date.
get_latest_by = "order_date"

# Latest by priority descending, order_date ascending.
get_latest_by = ["-priority", "order_date"]

```

See the [`latest()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.latest "django.db.models.query.QuerySet.latest") docs for more.
###  `managed`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#managed "Link to this heading")

Options.managed[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.managed "Link to this definition")

Defaults to `True`, meaning Django will create the appropriate database tables in [`migrate`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-migrate) or as part of migrations and remove them as part of a [`flush`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-flush) management command. That is, Django _manages_ the database tables’ lifecycles.
If `False`, no database table creation, modification, or deletion operations will be performed for this model. This is useful if the model represents an existing table or a database view that has been created by some other means. This is the _only_ difference when `managed=False`. All other aspects of model handling are exactly the same as normal. This includes
  1. Adding an automatic primary key field to the model if you don’t declare it. To avoid confusion for later code readers, it’s recommended to specify all the columns from the database table you are modeling when using unmanaged models.
  2. If a model with `managed=False` contains a [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") that points to another unmanaged model, then the intermediate table for the many-to-many join will also not be created. However, the intermediary table between one managed and one unmanaged model _will_ be created.
If you need to change this default behavior, create the intermediary table as an explicit model (with `managed` set as needed) and use the [`ManyToManyField.through`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.through "django.db.models.ManyToManyField.through") attribute to make the relation use your custom model.


For tests involving models with `managed=False`, it’s up to you to ensure the correct tables are created as part of the test setup.
If you’re interested in changing the Python-level behavior of a model class, you _could_ use `managed=False` and create a copy of an existing model. However, there’s a better approach for that situation: [Proxy models](https://docs.djangoproject.com/en/6.0/topics/db/models/#proxy-models).
###  `order_with_respect_to`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#order-with-respect-to "Link to this heading")

Options.order_with_respect_to[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.order_with_respect_to "Link to this definition")

Makes this object orderable with respect to the given field, usually a `ForeignKey`. This can be used to make related objects orderable with respect to a parent object. For example, if an `Answer` relates to a `Question` object, and a question has more than one answer, and the order of answers matters, you’d do this:
```
from django.db import models


class Question(models.Model):
    text = models.TextField()
    # ...


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # ...

    class Meta:
        order_with_respect_to = "question"

```

When `order_with_respect_to` is set, two additional methods are provided to retrieve and to set the order of the related objects: `get_RELATED_order()` and `set_RELATED_order()`, where `RELATED` is the lowercased model name. For example, assuming that a `Question` object has multiple related `Answer` objects, the list returned contains the primary keys of the related `Answer` objects:
```
>>> question = Question.objects.get(id=1)
>>> question.get_answer_order()
[1, 2, 3]

```

The order of a `Question` object’s related `Answer` objects can be set by passing in a list of `Answer` primary keys:
```
>>> question.set_answer_order([3, 1, 2])

```

The related objects also get two methods, `get_next_in_order()` and `get_previous_in_order()`, which can be used to access those objects in their proper order. Assuming the `Answer` objects are ordered by `id`:
```
>>> answer = Answer.objects.get(id=2)
>>> answer.get_next_in_order()
<Answer: 3>
>>> answer.get_previous_in_order()
<Answer: 1>

```

`order_with_respect_to` implicitly sets the `ordering` option
Internally, `order_with_respect_to` adds an additional field/database column named `_order` and sets the model’s [`ordering`](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.ordering "django.db.models.Options.ordering") option to this field. Consequently, `order_with_respect_to` and `ordering` cannot be used together, and the ordering added by `order_with_respect_to` will apply whenever you obtain a list of objects of this model.
Changing `order_with_respect_to`
Because `order_with_respect_to` adds a new database column, be sure to make and apply the appropriate migrations if you add or change `order_with_respect_to` after your initial [`migrate`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-migrate).
###  `ordering`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#ordering "Link to this heading")

Options.ordering[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.ordering "Link to this definition")

The default ordering for the object, for use when obtaining lists of objects:
```
ordering = ["-order_date"]

```

This is a tuple or list of strings and/or query expressions. Each string is a field name with an optional “-” prefix, which indicates descending order. Fields without a leading “-” will be ordered ascending. Use the string “?” to order randomly.
For example, to order by a `pub_date` field ascending, use this:
```
ordering = ["pub_date"]

```

To order by `pub_date` descending, use this:
```
ordering = ["-pub_date"]

```

To order by `pub_date` descending, then by `author` ascending, use this:
```
ordering = ["-pub_date", "author"]

```

You can also use [query expressions](https://docs.djangoproject.com/en/6.0/ref/models/expressions/). To order by `author` ascending and make null values sort last, use this:
```
from django.db.models import F

ordering = [F("author").asc(nulls_last=True)]

```

Default ordering and GROUP BY
In [GROUP BY queries](https://docs.djangoproject.com/en/6.0/topics/db/aggregation/#aggregation-ordering-interaction) (for example, those using [`values()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.values "django.db.models.query.QuerySet.values") and [`annotate()`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.annotate "django.db.models.query.QuerySet.annotate")), the default ordering is not applied.
Warning
Ordering is not a free operation. Each field you add to the ordering incurs a cost to your database. Each foreign key you add will implicitly include all of its default orderings as well.
If a query doesn’t have an ordering specified, results are returned from the database in an unspecified order. A particular ordering is guaranteed only when ordering by a set of fields that uniquely identify each object in the results. For example, if a `name` field isn’t unique, ordering by it won’t guarantee objects with the same name always appear in the same order.
###  `permissions`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#permissions "Link to this heading")

Options.permissions[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.permissions "Link to this definition")

Extra permissions to enter into the permissions table when creating this object. Add, change, delete, and view permissions are automatically created for each model. This example specifies an extra permission, `can_deliver_pizzas`:
```
permissions = [("can_deliver_pizzas", "Can deliver pizzas")]

```

This is a list or tuple of 2-tuples in the format `(permission_code, human_readable_permission_name)`.
###  `default_permissions`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#default-permissions "Link to this heading")

Options.default_permissions[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.default_permissions "Link to this definition")

Defaults to `('add', 'change', 'delete', 'view')`. You may customize this list, for example, by setting this to an empty list if your app doesn’t require any of the default permissions. It must be specified on the model before the model is created by [`migrate`](https://docs.djangoproject.com/en/6.0/ref/django-admin/#django-admin-migrate) in order to prevent any omitted permissions from being created.
###  `proxy`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#proxy "Link to this heading")

Options.proxy[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.proxy "Link to this definition")

If `proxy = True`, a model which subclasses another model will be treated as a [proxy model](https://docs.djangoproject.com/en/6.0/topics/db/models/#proxy-models).
###  `required_db_features`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#required-db-features "Link to this heading")

Options.required_db_features[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.required_db_features "Link to this definition")

List of database features that the current connection should have so that the model is considered during the migration phase. For example, if you set this list to `['gis_enabled']`, the model will only be synchronized on GIS-enabled databases. It’s also useful to skip some models when testing with several database backends. Avoid relations between models that may or may not be created as the ORM doesn’t handle this.
###  `required_db_vendor`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#required-db-vendor "Link to this heading")

Options.required_db_vendor[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.required_db_vendor "Link to this definition")

Name of a supported database vendor that this model is specific to. Current built-in vendor names are: `sqlite`, `postgresql`, `mysql`, `oracle`. If this attribute is not empty and the current connection vendor doesn’t match it, the model will not be synchronized.
###  `select_on_save`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#select-on-save "Link to this heading")

Options.select_on_save[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.select_on_save "Link to this definition")

Determines if Django will use the pre-1.6 [`django.db.models.Model.save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") algorithm. The old algorithm uses `SELECT` to determine if there is an existing row to be updated. The new algorithm tries an `UPDATE` directly. In some rare cases the `UPDATE` of an existing row isn’t visible to Django. An example is the PostgreSQL `ON UPDATE` trigger which returns `NULL`. In such cases the new algorithm will end up doing an `INSERT` even when a row exists in the database.
Usually there is no need to set this attribute. The default is `False`.
See [`django.db.models.Model.save()`](https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.save "django.db.models.Model.save") for more about the old and new saving algorithm.
###  `indexes`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#indexes "Link to this heading")

Options.indexes[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.indexes "Link to this definition")

A list of [indexes](https://docs.djangoproject.com/en/6.0/ref/models/indexes/) that you want to define on the model:
```
from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=["last_name", "first_name"]),
            models.Index(fields=["first_name"], name="first_name_idx"),
        ]

```

###  `unique_together`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#unique-together "Link to this heading")

Options.unique_together[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.unique_together "Link to this definition")

Use [`UniqueConstraint`](https://docs.djangoproject.com/en/6.0/ref/models/constraints/#django.db.models.UniqueConstraint "django.db.models.UniqueConstraint") with the [`constraints`](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.constraints "django.db.models.Options.constraints") option instead.
[`UniqueConstraint`](https://docs.djangoproject.com/en/6.0/ref/models/constraints/#django.db.models.UniqueConstraint "django.db.models.UniqueConstraint") provides more functionality than `unique_together`. `unique_together` may be deprecated in the future.
Sets of field names that, taken together, must be unique:
```
unique_together = [["driver", "restaurant"]]

```

This is a list of lists that must be unique when considered together. It’s used in the Django admin and is enforced at the database level (i.e., the appropriate `UNIQUE` statements are included in the `CREATE TABLE` statement).
For convenience, `unique_together` can be a single list when dealing with a single set of fields:
```
unique_together = ["driver", "restaurant"]

```

A [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField") cannot be included in `unique_together`. (It’s not clear what that would even mean!) If you need to validate uniqueness related to a [`ManyToManyField`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField "django.db.models.ManyToManyField"), try using a signal or an explicit [`through`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.ManyToManyField.through "django.db.models.ManyToManyField.through") model.
The `ValidationError` raised during model validation when the constraint is violated has the `unique_together` error code.
###  `constraints`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#constraints "Link to this heading")

Options.constraints[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.constraints "Link to this definition")

A list of [constraints](https://docs.djangoproject.com/en/6.0/ref/models/constraints/) that you want to define on the model:
```
from django.db import models


class Customer(models.Model):
    age = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(condition=models.Q(age__gte=18), name="age_gte_18"),
        ]

```

###  `verbose_name`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#verbose-name "Link to this heading")

Options.verbose_name[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.verbose_name "Link to this definition")

A human-readable name for the object, singular:
```
verbose_name = "pizza"

```

If this isn’t given, Django will use a munged version of the class name: `CamelCase` becomes `camel case`.
###  `verbose_name_plural`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#verbose-name-plural "Link to this heading")

Options.verbose_name_plural[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.verbose_name_plural "Link to this definition")

The plural name for the object:
```
verbose_name_plural = "stories"

```

If this isn’t given, Django will use [`verbose_name`](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.verbose_name "django.db.models.Options.verbose_name") + `"s"`.
## Read-only `Meta` attributes[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#read-only-meta-attributes "Link to this heading")
###  `label`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#label "Link to this heading")

Options.label[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.label "Link to this definition")

Representation of the object, returns `app_label.object_name`, e.g. `'polls.Question'`.
###  `label_lower`[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#label-lower "Link to this heading")

Options.label_lower[¶](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.label_lower "Link to this definition")

Representation of the model, returns `app_label.model_name`, e.g. `'polls.question'`. Previous page and next page
[](https://docs.djangoproject.com/en/6.0/ref/models/class/)
[Model instance reference ](https://docs.djangoproject.com/en/6.0/ref/models/instances/)
[](https://docs.djangoproject.com/en/6.0/ref/models/options/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Carlos Parrilla donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Model `Meta` options](https://docs.djangoproject.com/en/6.0/ref/models/options/)
    * [Available `Meta` options](https://docs.djangoproject.com/en/6.0/ref/models/options/#available-meta-options)
      * [`abstract`](https://docs.djangoproject.com/en/6.0/ref/models/options/#abstract)
      * [`app_label`](https://docs.djangoproject.com/en/6.0/ref/models/options/#app-label)
      * [`base_manager_name`](https://docs.djangoproject.com/en/6.0/ref/models/options/#base-manager-name)
      * [`db_table`](https://docs.djangoproject.com/en/6.0/ref/models/options/#db-table)
        * [Table names](https://docs.djangoproject.com/en/6.0/ref/models/options/#table-names)
      * [`db_table_comment`](https://docs.djangoproject.com/en/6.0/ref/models/options/#db-table-comment)
      * [`db_tablespace`](https://docs.djangoproject.com/en/6.0/ref/models/options/#db-tablespace)
      * [`default_manager_name`](https://docs.djangoproject.com/en/6.0/ref/models/options/#default-manager-name)
      * [`default_related_name`](https://docs.djangoproject.com/en/6.0/ref/models/options/#default-related-name)
      * [`get_latest_by`](https://docs.djangoproject.com/en/6.0/ref/models/options/#get-latest-by)
      * [`managed`](https://docs.djangoproject.com/en/6.0/ref/models/options/#managed)
      * [`order_with_respect_to`](https://docs.djangoproject.com/en/6.0/ref/models/options/#order-with-respect-to)
      * [`ordering`](https://docs.djangoproject.com/en/6.0/ref/models/options/#ordering)
      * [`permissions`](https://docs.djangoproject.com/en/6.0/ref/models/options/#permissions)
      * [`default_permissions`](https://docs.djangoproject.com/en/6.0/ref/models/options/#default-permissions)
      * [`proxy`](https://docs.djangoproject.com/en/6.0/ref/models/options/#proxy)
      * [`required_db_features`](https://docs.djangoproject.com/en/6.0/ref/models/options/#required-db-features)
      * [`required_db_vendor`](https://docs.djangoproject.com/en/6.0/ref/models/options/#required-db-vendor)
      * [`select_on_save`](https://docs.djangoproject.com/en/6.0/ref/models/options/#select-on-save)
      * [`indexes`](https://docs.djangoproject.com/en/6.0/ref/models/options/#indexes)
      * [`unique_together`](https://docs.djangoproject.com/en/6.0/ref/models/options/#unique-together)
      * [`constraints`](https://docs.djangoproject.com/en/6.0/ref/models/options/#constraints)
      * [`verbose_name`](https://docs.djangoproject.com/en/6.0/ref/models/options/#verbose-name)
      * [`verbose_name_plural`](https://docs.djangoproject.com/en/6.0/ref/models/options/#verbose-name-plural)
    * [Read-only `Meta` attributes](https://docs.djangoproject.com/en/6.0/ref/models/options/#read-only-meta-attributes)
      * [`label`](https://docs.djangoproject.com/en/6.0/ref/models/options/#label)
      * [`label_lower`](https://docs.djangoproject.com/en/6.0/ref/models/options/#label-lower)


### Browse
  * Prev: [Model class reference](https://docs.djangoproject.com/en/6.0/ref/models/class/)
  * Next: [Model instance reference](https://docs.djangoproject.com/en/6.0/ref/models/instances/)
  * [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)


### You are here:
  * [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
    * [API Reference](https://docs.djangoproject.com/en/6.0/ref/)
      * [Models](https://docs.djangoproject.com/en/6.0/ref/models/)
        * Model `Meta` options


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
