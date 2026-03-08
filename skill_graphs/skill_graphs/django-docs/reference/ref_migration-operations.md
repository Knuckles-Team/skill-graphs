This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/migration-operations/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/migration-operations/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/migration-operations/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/migration-operations/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/migration-operations/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/migration-operations/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/migration-operations/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/migration-operations/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/migration-operations/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/migration-operations/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/migration-operations/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/migration-operations/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/migration-operations/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/migration-operations/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/migration-operations/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/migration-operations/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/migration-operations/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/migration-operations/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/migration-operations/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/migration-operations/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/migration-operations/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/migration-operations/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/migration-operations/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/migration-operations/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/migration-operations/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/migration-operations/)


  * [](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#top)


# Migration Operations[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#module-django.db.migrations.operations "Link to this heading")
Migration files are composed of one or more `Operation`s, objects that declaratively record what the migration should do to your database.
Django also uses these `Operation` objects to work out what your models looked like historically, and to calculate what changes you’ve made to your models since the last migration so it can automatically write your migrations; that’s why they’re declarative, as it means Django can easily load them all into memory and run through them without touching the database to work out what your project should look like.
There are also more specialized `Operation` objects which are for things like [data migrations](https://docs.djangoproject.com/en/5.0/topics/migrations/#data-migrations) and for advanced manual database manipulation. You can also write your own `Operation` classes if you want to encapsulate a custom change you commonly make.
If you need an empty migration file to write your own `Operation` objects into, use `python manage.py makemigrations --empty yourappname`, but be aware that manually adding schema-altering operations can confuse the migration autodetector and make resulting runs of [`makemigrations`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-makemigrations) output incorrect code.
All of the core Django operations are available from the `django.db.migrations.operations` module.
For introductory material, see the [migrations topic guide](https://docs.djangoproject.com/en/5.0/topics/migrations/).
## Schema Operations[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#schema-operations "Link to this heading")
###  `CreateModel`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#createmodel "Link to this heading")

_class_ CreateModel(_name_ , _fields_ , _options =None_, _bases =None_, _managers =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/models/#CreateModel)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.CreateModel "Link to this definition")

Creates a new model in the project history and a corresponding table in the database to match it.
`name` is the model name, as would be written in the `models.py` file.
`fields` is a list of 2-tuples of `(field_name, field_instance)`. The field instance should be an unbound field (so just `models.CharField(...)`, rather than a field taken from another model).
`options` is an optional dictionary of values from the model’s `Meta` class.
`bases` is an optional list of other classes to have this model inherit from; it can contain both class objects as well as strings in the format `"appname.ModelName"` if you want to depend on another model (so you inherit from the historical version). If it’s not supplied, it defaults to inheriting from the standard `models.Model`.
`managers` takes a list of 2-tuples of `(manager_name, manager_instance)`. The first manager in the list will be the default manager for this model during migrations.
###  `DeleteModel`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#deletemodel "Link to this heading")

_class_ DeleteModel(_name_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/models/#DeleteModel)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.DeleteModel "Link to this definition")

Deletes the model from the project history and its table from the database.
###  `RenameModel`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#renamemodel "Link to this heading")

_class_ RenameModel(_old_name_ , _new_name_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/models/#RenameModel)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RenameModel "Link to this definition")

Renames the model from an old name to a new one.
You may have to manually add this if you change the model’s name and quite a few of its fields at once; to the autodetector, this will look like you deleted a model with the old name and added a new one with a different name, and the migration it creates will lose any data in the old table.
###  `AlterModelTable`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#altermodeltable "Link to this heading")

_class_ AlterModelTable(_name_ , _table_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/models/#AlterModelTable)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.AlterModelTable "Link to this definition")

Changes the model’s table name (the [`db_table`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.db_table "django.db.models.Options.db_table") option on the `Meta` subclass).
###  `AlterModelTableComment`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#altermodeltablecomment "Link to this heading")
New in Django 4.2.

_class_ AlterModelTableComment(_name_ , _table_comment_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/models/#AlterModelTableComment)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.AlterModelTableComment "Link to this definition")

Changes the model’s table comment (the [`db_table_comment`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.db_table_comment "django.db.models.Options.db_table_comment") option on the `Meta` subclass).
###  `AlterUniqueTogether`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#alteruniquetogether "Link to this heading")

_class_ AlterUniqueTogether(_name_ , _unique_together_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/models/#AlterUniqueTogether)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.AlterUniqueTogether "Link to this definition")

Changes the model’s set of unique constraints (the [`unique_together`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.unique_together "django.db.models.Options.unique_together") option on the `Meta` subclass).
###  `AlterIndexTogether`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#alterindextogether "Link to this heading")

_class_ AlterIndexTogether(_name_ , _index_together_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/models/#AlterIndexTogether)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.AlterIndexTogether "Link to this definition")

Changes the model’s set of custom indexes (the `index_together` option on the `Meta` subclass).
Warning
`AlterIndexTogether` is officially supported only for pre-Django 4.2 migration files. For backward compatibility reasons, it’s still part of the public API, and there’s no plan to deprecate or remove it, but it should not be used for new migrations. Use [`AddIndex`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.AddIndex "django.db.migrations.operations.AddIndex") and [`RemoveIndex`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RemoveIndex "django.db.migrations.operations.RemoveIndex") operations instead.
###  `AlterOrderWithRespectTo`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#alterorderwithrespectto "Link to this heading")

_class_ AlterOrderWithRespectTo(_name_ , _order_with_respect_to_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/models/#AlterOrderWithRespectTo)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.AlterOrderWithRespectTo "Link to this definition")

Makes or deletes the `_order` column needed for the [`order_with_respect_to`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.order_with_respect_to "django.db.models.Options.order_with_respect_to") option on the `Meta` subclass.
###  `AlterModelOptions`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#altermodeloptions "Link to this heading")

_class_ AlterModelOptions(_name_ , _options_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/models/#AlterModelOptions)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.AlterModelOptions "Link to this definition")

Stores changes to miscellaneous model options (settings on a model’s `Meta`) like `permissions` and `verbose_name`. Does not affect the database, but persists these changes for [`RunPython`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RunPython "django.db.migrations.operations.RunPython") instances to use. `options` should be a dictionary mapping option names to values.
###  `AlterModelManagers`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#altermodelmanagers "Link to this heading")

_class_ AlterModelManagers(_name_ , _managers_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/models/#AlterModelManagers)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.AlterModelManagers "Link to this definition")

Alters the managers that are available during migrations.
###  `AddField`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#addfield "Link to this heading")

_class_ AddField(_model_name_ , _name_ , _field_ , _preserve_default =True_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/fields/#AddField)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.AddField "Link to this definition")

Adds a field to a model. `model_name` is the model’s name, `name` is the field’s name, and `field` is an unbound Field instance (the thing you would put in the field declaration in `models.py` - for example, `models.IntegerField(null=True)`.
The `preserve_default` argument indicates whether the field’s default value is permanent and should be baked into the project state (`True`), or if it is temporary and just for this migration (`False`) - usually because the migration is adding a non-nullable field to a table and needs a default value to put into existing rows. It does not affect the behavior of setting defaults in the database directly - Django never sets database defaults and always applies them in the Django ORM code.
Warning
On older databases, adding a field with a default value may cause a full rewrite of the table. This happens even for nullable fields and may have a negative performance impact. To avoid that, the following steps should be taken.
  * Add the nullable field without the default value and run the [`makemigrations`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-makemigrations) command. This should generate a migration with an `AddField` operation.
  * Add the default value to your field and run the [`makemigrations`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-makemigrations) command. This should generate a migration with an `AlterField` operation.


###  `RemoveField`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#removefield "Link to this heading")

_class_ RemoveField(_model_name_ , _name_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/fields/#RemoveField)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RemoveField "Link to this definition")

Removes a field from a model.
Bear in mind that when reversed, this is actually adding a field to a model. The operation is reversible (apart from any data loss, which is irreversible) if the field is nullable or if it has a default value that can be used to populate the recreated column. If the field is not nullable and does not have a default value, the operation is irreversible.
PostgreSQL
`RemoveField` will also delete any additional database objects that are related to the removed field (like views, for example). This is because the resulting `DROP COLUMN` statement will include the `CASCADE` clause to ensure
###  `AlterField`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#alterfield "Link to this heading")

_class_ AlterField(_model_name_ , _name_ , _field_ , _preserve_default =True_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/fields/#AlterField)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.AlterField "Link to this definition")

Alters a field’s definition, including changes to its type, [`null`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field.null "django.db.models.Field.null"), [`unique`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field.unique "django.db.models.Field.unique"), [`db_column`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field.db_column "django.db.models.Field.db_column") and other field attributes.
The `preserve_default` argument indicates whether the field’s default value is permanent and should be baked into the project state (`True`), or if it is temporary and just for this migration (`False`) - usually because the migration is altering a nullable field to a non-nullable one and needs a default value to put into existing rows. It does not affect the behavior of setting defaults in the database directly - Django never sets database defaults and always applies them in the Django ORM code.
Note that not all changes are possible on all databases - for example, you cannot change a text-type field like `models.TextField()` into a number-type field like `models.IntegerField()` on most databases.
###  `RenameField`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#renamefield "Link to this heading")

_class_ RenameField(_model_name_ , _old_name_ , _new_name_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/fields/#RenameField)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RenameField "Link to this definition")

Changes a field’s name (and, unless [`db_column`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field.db_column "django.db.models.Field.db_column") is set, its column name).
###  `AddIndex`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#addindex "Link to this heading")

_class_ AddIndex(_model_name_ , _index_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/models/#AddIndex)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.AddIndex "Link to this definition")

Creates an index in the database table for the model with `model_name`. `index` is an instance of the [`Index`](https://docs.djangoproject.com/en/5.0/ref/models/indexes/#django.db.models.Index "django.db.models.Index") class.
###  `RemoveIndex`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#removeindex "Link to this heading")

_class_ RemoveIndex(_model_name_ , _name_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/models/#RemoveIndex)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RemoveIndex "Link to this definition")

Removes the index named `name` from the model with `model_name`.
###  `RenameIndex`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#renameindex "Link to this heading")

_class_ RenameIndex(_model_name_ , _new_name_ , _old_name =None_, _old_fields =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/models/#RenameIndex)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RenameIndex "Link to this definition")

Renames an index in the database table for the model with `model_name`. Exactly one of `old_name` and `old_fields` can be provided. `old_fields` is an iterable of the strings, often corresponding to fields of [`index_together`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.index_together "django.db.models.Options.index_together").
On databases that don’t support an index renaming statement (SQLite and MariaDB < 10.5.2), the operation will drop and recreate the index, which can be expensive.
###  `AddConstraint`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#addconstraint "Link to this heading")

_class_ AddConstraint(_model_name_ , _constraint_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/models/#AddConstraint)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.AddConstraint "Link to this definition")

Creates a [constraint](https://docs.djangoproject.com/en/5.0/ref/models/constraints/) in the database table for the model with `model_name`.
###  `RemoveConstraint`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#removeconstraint "Link to this heading")

_class_ RemoveConstraint(_model_name_ , _name_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/models/#RemoveConstraint)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RemoveConstraint "Link to this definition")

Removes the constraint named `name` from the model with `model_name`.
## Special Operations[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#special-operations "Link to this heading")
###  `RunSQL`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#runsql "Link to this heading")

_class_ RunSQL(_sql_ , _reverse_sql =None_, _state_operations =None_, _hints =None_, _elidable =False_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/special/#RunSQL)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RunSQL "Link to this definition")

Allows running of arbitrary SQL on the database - useful for more advanced features of database backends that Django doesn’t support directly.
`sql`, and `reverse_sql` if provided, should be strings of SQL to run on the database. On most database backends (all but PostgreSQL), Django will split the SQL into individual statements prior to executing them.
Warning
On PostgreSQL and SQLite, only use `BEGIN` or `COMMIT` in your SQL in [non-atomic migrations](https://docs.djangoproject.com/en/5.0/howto/writing-migrations/#non-atomic-migrations), to avoid breaking Django’s transaction state.
You can also pass a list of strings or 2-tuples. The latter is used for passing queries and parameters in the same way as [cursor.execute()](https://docs.djangoproject.com/en/5.0/topics/db/sql/#executing-custom-sql). These three operations are equivalent:
```
migrations.RunSQL("INSERT INTO musician (name) VALUES ('Reinhardt');")
migrations.RunSQL([("INSERT INTO musician (name) VALUES ('Reinhardt');", None)])
migrations.RunSQL([("INSERT INTO musician (name) VALUES (%s);", ["Reinhardt"])])

```

If you want to include literal percent signs in the query, you have to double them if you are passing parameters.
The `reverse_sql` queries are executed when the migration is unapplied. They should undo what is done by the `sql` queries. For example, to undo the above insertion with a deletion:
```
migrations.RunSQL(
    sql=[("INSERT INTO musician (name) VALUES (%s);", ["Reinhardt"])],
    reverse_sql=[("DELETE FROM musician where name=%s;", ["Reinhardt"])],
)

```

If `reverse_sql` is `None` (the default), the `RunSQL` operation is irreversible.
The `state_operations` argument allows you to supply operations that are equivalent to the SQL in terms of project state. For example, if you are manually creating a column, you should pass in a list containing an `AddField` operation here so that the autodetector still has an up-to-date state of the model. If you don’t, when you next run `makemigrations`, it won’t see any operation that adds that field and so will try to run it again. For example:
```
migrations.RunSQL(
    "ALTER TABLE musician ADD COLUMN name varchar(255) NOT NULL;",
    state_operations=[
        migrations.AddField(
            "musician",
            "name",
            models.CharField(max_length=255),
        ),
    ],
)

```

The optional `hints` argument will be passed as `**hints` to the [`allow_migrate()`](https://docs.djangoproject.com/en/5.0/topics/db/multi-db/#allow_migrate "allow_migrate") method of database routers to assist them in making routing decisions. See [Hints](https://docs.djangoproject.com/en/5.0/topics/db/multi-db/#topics-db-multi-db-hints) for more details on database hints.
The optional `elidable` argument determines whether or not the operation will be removed (elided) when [squashing migrations](https://docs.djangoproject.com/en/5.0/topics/migrations/#migration-squashing).

RunSQL.noop[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RunSQL.noop "Link to this definition")

Pass the `RunSQL.noop` attribute to `sql` or `reverse_sql` when you want the operation not to do anything in the given direction. This is especially useful in making the operation reversible.
###  `RunPython`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#runpython "Link to this heading")

_class_ RunPython(_code_ , _reverse_code =None_, _atomic =None_, _hints =None_, _elidable =False_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/special/#RunPython)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RunPython "Link to this definition")

Runs custom Python code in a historical context. `code` (and `reverse_code` if supplied) should be callable objects that accept two arguments; the first is an instance of `django.apps.registry.Apps` containing historical models that match the operation’s place in the project history, and the second is an instance of [`SchemaEditor`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor "django.db.backends.base.schema.BaseDatabaseSchemaEditor").
The `reverse_code` argument is called when unapplying migrations. This callable should undo what is done in the `code` callable so that the migration is reversible. If `reverse_code` is `None` (the default), the `RunPython` operation is irreversible.
The optional `hints` argument will be passed as `**hints` to the [`allow_migrate()`](https://docs.djangoproject.com/en/5.0/topics/db/multi-db/#allow_migrate "allow_migrate") method of database routers to assist them in making a routing decision. See [Hints](https://docs.djangoproject.com/en/5.0/topics/db/multi-db/#topics-db-multi-db-hints) for more details on database hints.
The optional `elidable` argument determines whether or not the operation will be removed (elided) when [squashing migrations](https://docs.djangoproject.com/en/5.0/topics/migrations/#migration-squashing).
You are advised to write the code as a separate function above the `Migration` class in the migration file, and pass it to `RunPython`. Here’s an example of using `RunPython` to create some initial objects on a `Country` model:
```
from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Country = apps.get_model("myapp", "Country")
    db_alias = schema_editor.connection.alias
    Country.objects.using(db_alias).bulk_create(
        [
            Country(name="USA", code="us"),
            Country(name="France", code="fr"),
        ]
    )


def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    Country = apps.get_model("myapp", "Country")
    db_alias = schema_editor.connection.alias
    Country.objects.using(db_alias).filter(name="USA", code="us").delete()
    Country.objects.using(db_alias).filter(name="France", code="fr").delete()


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]

```

This is generally the operation you would use to create [data migrations](https://docs.djangoproject.com/en/5.0/topics/migrations/#data-migrations), run custom data updates and alterations, and anything else you need access to an ORM and/or Python code for.
Much like [`RunSQL`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RunSQL "django.db.migrations.operations.RunSQL"), ensure that if you change schema inside here you’re either doing it outside the scope of the Django model system (e.g. triggers) or that you use [`SeparateDatabaseAndState`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.SeparateDatabaseAndState "django.db.migrations.operations.SeparateDatabaseAndState") to add in operations that will reflect your changes to the model state - otherwise, the versioned ORM and the autodetector will stop working correctly.
By default, `RunPython` will run its contents inside a transaction on databases that do not support DDL transactions (for example, MySQL and Oracle). This should be safe, but may cause a crash if you attempt to use the `schema_editor` provided on these backends; in this case, pass `atomic=False` to the `RunPython` operation.
On databases that do support DDL transactions (SQLite and PostgreSQL), `RunPython` operations do not have any transactions automatically added besides the transactions created for each migration. Thus, on PostgreSQL, for example, you should avoid combining schema changes and `RunPython` operations in the same migration or you may hit errors like `OperationalError: cannot ALTER TABLE "mytable" because it has pending trigger events`.
If you have a different database and aren’t sure if it supports DDL transactions, check the `django.db.connection.features.can_rollback_ddl` attribute.
If the `RunPython` operation is part of a [non-atomic migration](https://docs.djangoproject.com/en/5.0/howto/writing-migrations/#non-atomic-migrations), the operation will only be executed in a transaction if `atomic=True` is passed to the `RunPython` operation.
Warning
`RunPython` does not magically alter the connection of the models for you; any model methods you call will go to the default database unless you give them the current database alias (available from `schema_editor.connection.alias`, where `schema_editor` is the second argument to your function).

_static_ RunPython.noop()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/special/#RunPython.noop)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RunPython.noop "Link to this definition")

Pass the `RunPython.noop` method to `code` or `reverse_code` when you want the operation not to do anything in the given direction. This is especially useful in making the operation reversible.
###  `SeparateDatabaseAndState`[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#separatedatabaseandstate "Link to this heading")

_class_ SeparateDatabaseAndState(_database_operations =None_, _state_operations =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/migrations/operations/special/#SeparateDatabaseAndState)[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.SeparateDatabaseAndState "Link to this definition")

A highly specialized operation that lets you mix and match the database (schema-changing) and state (autodetector-powering) aspects of operations.
It accepts two lists of operations. When asked to apply state, it will use the `state_operations` list (this is a generalized version of [`RunSQL`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RunSQL "django.db.migrations.operations.RunSQL")’s `state_operations` argument). When asked to apply changes to the database, it will use the `database_operations` list.
If the actual state of the database and Django’s view of the state get out of sync, this can break the migration framework, even leading to data loss. It’s worth exercising caution and checking your database and state operations carefully. You can use [`sqlmigrate`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-sqlmigrate) and [`dbshell`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-dbshell) to check your database operations. You can use [`makemigrations`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-makemigrations), especially with [`--dry-run`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemigrations-dry-run), to check your state operations.
For an example using `SeparateDatabaseAndState`, see [Changing a ManyToManyField to use a through model](https://docs.djangoproject.com/en/5.0/howto/writing-migrations/#changing-a-manytomanyfield-to-use-a-through-model).
## Writing your own[¶](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#writing-your-own "Link to this heading")
Operations have a relatively simple API, and they’re designed so that you can easily write your own to supplement the built-in Django ones. The basic structure of an `Operation` looks like this:
```
from django.db.migrations.operations.base import Operation


class MyCustomOperation(Operation):
    # If this is False, it means that this operation will be ignored by
    # sqlmigrate; if true, it will be run and the SQL collected for its output.
    reduces_to_sql = False

    # If this is False, Django will refuse to reverse past this operation.
    reversible = False

    def __init__(self, arg1, arg2):
        # Operations are usually instantiated with arguments in migration
        # files. Store the values of them on self for later use.
        pass

    def state_forwards(self, app_label, state):
        # The Operation should take the 'state' parameter (an instance of
        # django.db.migrations.state.ProjectState) and mutate it to match
        # any schema changes that have occurred.
        pass

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        # The Operation should use schema_editor to apply any changes it
        # wants to make to the database.
        pass

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        # If reversible is True, this is called when the operation is reversed.
        pass

    def describe(self):
        # This is used to describe what the operation does in console output.
        return "Custom Operation"

    @property
    def migration_name_fragment(self):
        # Optional. A filename part suitable for automatically naming a
        # migration containing this operation, or None if not applicable.
        return "custom_operation_%s_%s" % (self.arg1, self.arg2)

```

You can take this template and work from it, though we suggest looking at the built-in Django operations in `django.db.migrations.operations` - they cover a lot of the example usage of semi-internal aspects of the migration framework like `ProjectState` and the patterns used to get historical models, as well as `ModelState` and the patterns used to mutate historical models in `state_forwards()`.
Some things to note:
  * You don’t need to learn too much about `ProjectState` to write migrations; just know that it has an `apps` property that gives access to an app registry (which you can then call `get_model` on).
  * `database_forwards` and `database_backwards` both get two states passed to them; these represent the difference the `state_forwards` method would have applied, but are given to you for convenience and speed reasons.
  * If you want to work with model classes or model instances from the `from_state` argument in `database_forwards()` or `database_backwards()`, you must render model states using the `clear_delayed_apps_cache()` method to make related models available:
```
def database_forwards(self, app_label, schema_editor, from_state, to_state):
    # This operation should have access to all models. Ensure that all models are
    # reloaded in case any are delayed.
    from_state.clear_delayed_apps_cache()
    ...

```

  * `to_state` in the database_backwards method is the _older_ state; that is, the one that will be the current state once the migration has finished reversing.
  * You might see implementations of `references_model` on the built-in operations; this is part of the autodetection code and does not matter for custom operations.


Warning
For performance reasons, the [`Field`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field "django.db.models.Field") instances in `ModelState.fields` are reused across migrations. You must never change the attributes on these instances. If you need to mutate a field in `state_forwards()`, you must remove the old instance from `ModelState.fields` and add a new instance in its place. The same is true for the [`Manager`](https://docs.djangoproject.com/en/5.0/topics/db/managers/#django.db.models.Manager "django.db.models.Manager") instances in `ModelState.managers`.
As an example, let’s make an operation that loads PostgreSQL extensions (which contain some of PostgreSQL’s more exciting features). Since there’s no model state changes, all it does is run one command:
```
from django.db.migrations.operations.base import Operation


class LoadExtension(Operation):
    reversible = True

    def __init__(self, name):
        self.name = name

    def state_forwards(self, app_label, state):
        pass

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        schema_editor.execute("CREATE EXTENSION IF NOT EXISTS %s" % self.name)

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        schema_editor.execute("DROP EXTENSION %s" % self.name)

    def describe(self):
        return "Creates extension %s" % self.name

    @property
    def migration_name_fragment(self):
        return "create_extension_%s" % self.name

```

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/middleware/)
[Models ](https://docs.djangoproject.com/en/5.0/ref/models/)
[](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Goetz donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Migration Operations](https://docs.djangoproject.com/en/5.0/ref/migration-operations/)
    * [Schema Operations](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#schema-operations)
      * [`CreateModel`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#createmodel)
      * [`DeleteModel`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#deletemodel)
      * [`RenameModel`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#renamemodel)
      * [`AlterModelTable`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#altermodeltable)
      * [`AlterModelTableComment`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#altermodeltablecomment)
      * [`AlterUniqueTogether`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#alteruniquetogether)
      * [`AlterIndexTogether`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#alterindextogether)
      * [`AlterOrderWithRespectTo`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#alterorderwithrespectto)
      * [`AlterModelOptions`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#altermodeloptions)
      * [`AlterModelManagers`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#altermodelmanagers)
      * [`AddField`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#addfield)
      * [`RemoveField`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#removefield)
      * [`AlterField`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#alterfield)
      * [`RenameField`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#renamefield)
      * [`AddIndex`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#addindex)
      * [`RemoveIndex`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#removeindex)
      * [`RenameIndex`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#renameindex)
      * [`AddConstraint`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#addconstraint)
      * [`RemoveConstraint`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#removeconstraint)
    * [Special Operations](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#special-operations)
      * [`RunSQL`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#runsql)
      * [`RunPython`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#runpython)
      * [`SeparateDatabaseAndState`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#separatedatabaseandstate)
    * [Writing your own](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#writing-your-own)


### Browse
  * Prev: [Middleware](https://docs.djangoproject.com/en/5.0/ref/middleware/)
  * Next: [Models](https://docs.djangoproject.com/en/5.0/ref/models/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * Migration Operations


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
