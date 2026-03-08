This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/ref/schema-editor/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/ref/schema-editor/)
  * [pl](https://docs.djangoproject.com/pl/5.0/ref/schema-editor/)
  * [ko](https://docs.djangoproject.com/ko/5.0/ref/schema-editor/)
  * [ja](https://docs.djangoproject.com/ja/5.0/ref/schema-editor/)
  * [it](https://docs.djangoproject.com/it/5.0/ref/schema-editor/)
  * [id](https://docs.djangoproject.com/id/5.0/ref/schema-editor/)
  * [fr](https://docs.djangoproject.com/fr/5.0/ref/schema-editor/)
  * [es](https://docs.djangoproject.com/es/5.0/ref/schema-editor/)
  * [el](https://docs.djangoproject.com/el/5.0/ref/schema-editor/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/ref/schema-editor/)
  * [6.0](https://docs.djangoproject.com/en/6.0/ref/schema-editor/)
  * [5.2](https://docs.djangoproject.com/en/5.2/ref/schema-editor/)
  * [5.1](https://docs.djangoproject.com/en/5.1/ref/schema-editor/)
  * [4.2](https://docs.djangoproject.com/en/4.2/ref/schema-editor/)
  * [4.1](https://docs.djangoproject.com/en/4.1/ref/schema-editor/)
  * [4.0](https://docs.djangoproject.com/en/4.0/ref/schema-editor/)
  * [3.2](https://docs.djangoproject.com/en/3.2/ref/schema-editor/)
  * [3.1](https://docs.djangoproject.com/en/3.1/ref/schema-editor/)
  * [3.0](https://docs.djangoproject.com/en/3.0/ref/schema-editor/)
  * [2.2](https://docs.djangoproject.com/en/2.2/ref/schema-editor/)
  * [2.1](https://docs.djangoproject.com/en/2.1/ref/schema-editor/)
  * [2.0](https://docs.djangoproject.com/en/2.0/ref/schema-editor/)
  * [1.11](https://docs.djangoproject.com/en/1.11/ref/schema-editor/)
  * [1.10](https://docs.djangoproject.com/en/1.10/ref/schema-editor/)
  * [1.8](https://docs.djangoproject.com/en/1.8/ref/schema-editor/)


  * [](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#top)


#  `SchemaEditor`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#module-django.db.backends.base.schema "Link to this heading")

_class_ BaseDatabaseSchemaEditor[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor "Link to this definition")

Django’s migration system is split into two parts; the logic for calculating and storing what operations should be run (`django.db.migrations`), and the database abstraction layer that turns things like “create a model” or “delete a field” into SQL - which is the job of the `SchemaEditor`.
It’s unlikely that you will want to interact directly with `SchemaEditor` as a normal developer using Django, but if you want to write your own migration system, or have more advanced needs, it’s a lot nicer than writing SQL.
Each database backend in Django supplies its own version of `SchemaEditor`, and it’s always accessible via the `connection.schema_editor()` context manager:
```
with connection.schema_editor() as schema_editor:
    schema_editor.delete_model(MyModel)

```

It must be used via the context manager as this allows it to manage things like transactions and deferred SQL (like creating `ForeignKey` constraints).
It exposes all possible operations as methods, that should be called in the order you wish changes to be applied. Some possible operations or types of change are not possible on all databases - for example, MyISAM does not support foreign key constraints.
If you are writing or maintaining a third-party database backend for Django, you will need to provide a `SchemaEditor` implementation in order to work with Django’s migration functionality - however, as long as your database is relatively standard in its use of SQL and relational design, you should be able to subclass one of the built-in Django `SchemaEditor` classes and tweak the syntax a little.
## Methods[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#methods "Link to this heading")
###  `execute()`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#execute "Link to this heading")

BaseDatabaseSchemaEditor.execute(_sql_ , _params =()_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor.execute)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.execute "Link to this definition")

Executes the SQL statement passed in, with parameters if supplied. This is a wrapper around the normal database cursors that allows capture of the SQL to a `.sql` file if the user wishes.
###  `create_model()`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#create-model "Link to this heading")

BaseDatabaseSchemaEditor.create_model(_model_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor.create_model)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.create_model "Link to this definition")

Creates a new table in the database for the provided model, along with any unique constraints or indexes it requires.
###  `delete_model()`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#delete-model "Link to this heading")

BaseDatabaseSchemaEditor.delete_model(_model_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor.delete_model)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.delete_model "Link to this definition")

Drops the model’s table in the database along with any unique constraints or indexes it has.
###  `add_index()`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#add-index "Link to this heading")

BaseDatabaseSchemaEditor.add_index(_model_ , _index_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor.add_index)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.add_index "Link to this definition")

Adds `index` to `model`’s table.
###  `remove_index()`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#remove-index "Link to this heading")

BaseDatabaseSchemaEditor.remove_index(_model_ , _index_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor.remove_index)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.remove_index "Link to this definition")

Removes `index` from `model`’s table.
###  `rename_index()`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#rename-index "Link to this heading")

BaseDatabaseSchemaEditor.rename_index(_model_ , _old_index_ , _new_index_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor.rename_index)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.rename_index "Link to this definition")

Renames `old_index` from `model`’s table to `new_index`.
###  `add_constraint()`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#add-constraint "Link to this heading")

BaseDatabaseSchemaEditor.add_constraint(_model_ , _constraint_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor.add_constraint)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.add_constraint "Link to this definition")

Adds `constraint` to `model`’s table.
###  `remove_constraint()`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#remove-constraint "Link to this heading")

BaseDatabaseSchemaEditor.remove_constraint(_model_ , _constraint_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor.remove_constraint)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.remove_constraint "Link to this definition")

Removes `constraint` from `model`’s table.
###  `alter_unique_together()`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#alter-unique-together "Link to this heading")

BaseDatabaseSchemaEditor.alter_unique_together(_model_ , _old_unique_together_ , _new_unique_together_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor.alter_unique_together)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.alter_unique_together "Link to this definition")

Changes a model’s [`unique_together`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.unique_together "django.db.models.Options.unique_together") value; this will add or remove unique constraints from the model’s table until they match the new value.
###  `alter_index_together()`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#alter-index-together "Link to this heading")

BaseDatabaseSchemaEditor.alter_index_together(_model_ , _old_index_together_ , _new_index_together_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor.alter_index_together)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.alter_index_together "Link to this definition")

Changes a model’s [`index_together`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.index_together "django.db.models.Options.index_together") value; this will add or remove indexes from the model’s table until they match the new value.
###  `alter_db_table()`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#alter-db-table "Link to this heading")

BaseDatabaseSchemaEditor.alter_db_table(_model_ , _old_db_table_ , _new_db_table_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor.alter_db_table)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.alter_db_table "Link to this definition")

Renames the model’s table from `old_db_table` to `new_db_table`.
###  `alter_db_table_comment()`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#alter-db-table-comment "Link to this heading")
New in Django 4.2.

BaseDatabaseSchemaEditor.alter_db_table_comment(_model_ , _old_db_table_comment_ , _new_db_table_comment_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor.alter_db_table_comment)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.alter_db_table_comment "Link to this definition")

Change the `model`’s table comment to `new_db_table_comment`.
###  `alter_db_tablespace()`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#alter-db-tablespace "Link to this heading")

BaseDatabaseSchemaEditor.alter_db_tablespace(_model_ , _old_db_tablespace_ , _new_db_tablespace_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor.alter_db_tablespace)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.alter_db_tablespace "Link to this definition")

Moves the model’s table from one tablespace to another.
###  `add_field()`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#add-field "Link to this heading")

BaseDatabaseSchemaEditor.add_field(_model_ , _field_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor.add_field)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.add_field "Link to this definition")

Adds a column (or sometimes multiple) to the model’s table to represent the field. This will also add indexes or a unique constraint if the field has `db_index=True` or `unique=True`.
If the field is a `ManyToManyField` without a value for `through`, instead of creating a column, it will make a table to represent the relationship. If `through` is provided, it is a no-op.
If the field is a `ForeignKey`, this will also add the foreign key constraint to the column.
###  `remove_field()`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#remove-field "Link to this heading")

BaseDatabaseSchemaEditor.remove_field(_model_ , _field_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor.remove_field)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.remove_field "Link to this definition")

Removes the column(s) representing the field from the model’s table, along with any unique constraints, foreign key constraints, or indexes caused by that field.
If the field is a ManyToManyField without a value for `through`, it will remove the table created to track the relationship. If `through` is provided, it is a no-op.
###  `alter_field()`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#alter-field "Link to this heading")

BaseDatabaseSchemaEditor.alter_field(_model_ , _old_field_ , _new_field_ , _strict =False_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/db/backends/base/schema/#BaseDatabaseSchemaEditor.alter_field)[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.alter_field "Link to this definition")

This transforms the field on the model from the old field to the new one. This includes changing the name of the column (the [`db_column`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field.db_column "django.db.models.Field.db_column") attribute), changing the type of the field (if the field class changes), changing the `NULL` status of the field, adding or removing field-only unique constraints and indexes, changing primary key, and changing the destination of `ForeignKey` constraints.
The most common transformation this cannot do is transforming a `ManyToManyField` into a normal Field or vice-versa; Django cannot do this without losing data, and so it will refuse to do it. Instead, [`remove_field()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.remove_field "django.db.backends.base.schema.BaseDatabaseSchemaEditor.remove_field") and [`add_field()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.add_field "django.db.backends.base.schema.BaseDatabaseSchemaEditor.add_field") should be called separately.
If the database has the `supports_combined_alters`, Django will try and do as many of these in a single database call as possible; otherwise, it will issue a separate ALTER statement for each change, but will not issue ALTERs where no change is required.
## Attributes[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#attributes "Link to this heading")
All attributes should be considered read-only unless stated otherwise.
###  `connection`[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#connection "Link to this heading")

SchemaEditor.connection[¶](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#django.db.backends.base.schema.SchemaEditor.connection "Link to this definition")

A connection object to the database. A useful attribute of the connection is `alias` which can be used to determine the name of the database being accessed.
This is useful when doing data migrations for [migrations with multiple databases](https://docs.djangoproject.com/en/5.0/howto/writing-migrations/#data-migrations-and-multiple-databases).
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/ref/request-response/)
[Settings ](https://docs.djangoproject.com/en/5.0/ref/settings/)
[](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Yuval Adam donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [`SchemaEditor`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/)
    * [Methods](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#methods)
      * [`execute()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#execute)
      * [`create_model()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#create-model)
      * [`delete_model()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#delete-model)
      * [`add_index()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#add-index)
      * [`remove_index()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#remove-index)
      * [`rename_index()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#rename-index)
      * [`add_constraint()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#add-constraint)
      * [`remove_constraint()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#remove-constraint)
      * [`alter_unique_together()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#alter-unique-together)
      * [`alter_index_together()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#alter-index-together)
      * [`alter_db_table()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#alter-db-table)
      * [`alter_db_table_comment()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#alter-db-table-comment)
      * [`alter_db_tablespace()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#alter-db-tablespace)
      * [`add_field()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#add-field)
      * [`remove_field()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#remove-field)
      * [`alter_field()`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#alter-field)
    * [Attributes](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#attributes)
      * [`connection`](https://docs.djangoproject.com/en/5.0/ref/schema-editor/#connection)


### Browse
  * Prev: [Request and response objects](https://docs.djangoproject.com/en/5.0/ref/request-response/)
  * Next: [Settings](https://docs.djangoproject.com/en/5.0/ref/settings/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * `SchemaEditor`


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
