## MySQL notes[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#mysql-notes "Link to this heading")
### Version support[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#version-support "Link to this heading")
Django supports MySQL 8.0.11 and higher.
Django’s `inspectdb` feature uses the `information_schema` database, which contains detailed data on all database schemas.
Django expects the database to support Unicode (UTF-8 encoding) and delegates to it the task of enforcing transactions and referential integrity. It is important to be aware of the fact that the two latter ones aren’t actually enforced by MySQL when using the MyISAM storage engine, see the next section.
### Storage engines[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#storage-engines "Link to this heading")
MySQL has several
MySQL’s default storage engine is `AUTO_INCREMENT` value, instead recreating it as “max(id)+1”. This may result in an inadvertent reuse of [`AutoField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.AutoField "django.db.models.AutoField") values.
The main drawbacks of
### MySQL DB API Drivers[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#mysql-db-api-drivers "Link to this heading")
MySQL has a couple drivers that implement the Python Database API described in
  * **the recommended choice**.


These drivers are thread-safe and provide connection pooling.
In addition to a DB API driver, Django needs an adapter to access the database drivers from its ORM. Django provides an adapter for mysqlclient while MySQL Connector/Python includes
#### mysqlclient[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#mysqlclient "Link to this heading")
Django requires [mysqlclient](https://docs.djangoproject.com/en/5.0/ref/databases/#mysqlclient) 1.4.3 or later.
#### MySQL Connector/Python[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#id8 "Link to this heading")
MySQL Connector/Python is available from the
### Time zone definitions[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#time-zone-definitions "Link to this heading")
If you plan on using Django’s [timezone support](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/), use
### Creating your database[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#creating-your-database "Link to this heading")
You can
```
CREATE DATABASE <dbname> CHARACTER SET utf8;

```

This ensures all tables and columns will use UTF-8 by default.
#### Collation settings[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#collation-settings "Link to this heading")
The collation setting for a column controls the order in which data is sorted as well as what strings compare as equal. You can specify the `db_collation` parameter to set the collation name of the column for [`CharField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.CharField.db_collation "django.db.models.CharField.db_collation") and [`TextField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.TextField.db_collation "django.db.models.TextField.db_collation").
The collation can also be set on a database-wide level and per-table. This is
By default, with a UTF-8 database, MySQL will use the `utf8_general_ci` collation. This results in all string equality comparisons being done in a _case-insensitive_ manner. That is, `"Fred"` and `"freD"` are considered equal at the database level. If you have a unique constraint on a field, it would be illegal to try to insert both `"aa"` and `"AA"` into the same column, since they compare as equal (and, hence, non-unique) with the default collation. If you want case-sensitive comparisons on a particular column or table, change the column or table to use the `utf8_bin` collation.
Please note that according to `utf8_general_ci` collation are faster, but slightly less correct, than comparisons for `utf8_unicode_ci`. If this is acceptable for your application, you should use `utf8_general_ci` because it is faster. If this is not acceptable (for example, if you require German dictionary order), use `utf8_unicode_ci` because it is more accurate.
Warning
Model formsets validate unique fields in a case-sensitive manner. Thus when using a case-insensitive collation, a formset with unique field values that differ only by case will pass validation, but upon calling `save()`, an `IntegrityError` will be raised.
### Connecting to the database[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#connecting-to-the-database "Link to this heading")
Refer to the [settings documentation](https://docs.djangoproject.com/en/5.0/ref/settings/).
Connection settings are used in this order:
  1. [`OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-OPTIONS).
  2. [`NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-NAME), [`USER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USER), [`PASSWORD`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-PASSWORD), [`HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-HOST), [`PORT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-PORT)
  3. MySQL option files.


In other words, if you set the name of the database in [`OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-OPTIONS), this will take precedence over [`NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-NAME), which would override anything in a
Here’s a sample configuration which uses a MySQL option file:
```
# settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": "/path/to/my.cnf",
        },
    }
}

```

```
# my.cnf
[client]
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8

```

Several other `ssl`, `init_command`, and `sql_mode`.
#### Setting `sql_mode`[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#setting-sql-mode "Link to this heading")
The default value of the `sql_mode` option contains `STRICT_TRANS_TABLES`. That option escalates warnings into errors when data are truncated upon insertion, so Django highly recommends activating a `STRICT_TRANS_TABLES` or `STRICT_ALL_TABLES`).
If you need to customize the SQL mode, you can set the `sql_mode` variable like other MySQL options: either in a config file or with the entry `'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"` in the [`OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-OPTIONS) part of your database configuration in [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES).
#### Isolation level[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#mysql-isolation-level "Link to this heading")
When running concurrent loads, database transactions from different sessions (say, separate threads handling different requests) may interact with each other. These interactions are affected by each session’s `'isolation_level'` entry in the [`OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-OPTIONS) part of your database configuration in [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES). Valid values for this entry are the four standard isolation levels:
  * `'read uncommitted'`
  * `'read committed'`
  * `'repeatable read'`
  * `'serializable'`


or `None` to use the server’s configured isolation level. However, Django works best with and defaults to read committed rather than MySQL’s default, repeatable read. Data loss is possible with repeatable read. In particular, you may see cases where [`get_or_create()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.get_or_create "django.db.models.query.QuerySet.get_or_create") will raise an [`IntegrityError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.IntegrityError "django.db.IntegrityError") but the object won’t appear in a subsequent [`get()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.get "django.db.models.query.QuerySet.get") call.
### Creating your tables[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#creating-your-tables "Link to this heading")
When Django generates the schema, it doesn’t specify a storage engine, so tables will be created with whatever default storage engine your database server is configured for. The easiest solution is to set your database server’s default storage engine to the desired engine.
If you’re using a hosting service and can’t change your server’s default storage engine, you have a couple of options.
  * After the tables are created, execute an `ALTER TABLE` statement to convert a table to a new storage engine (such as InnoDB):
```
ALTER TABLE <tablename> ENGINE=INNODB;

```

This can be tedious if you have a lot of tables.
  * Another option is to use the `init_command` option for MySQLdb prior to creating your tables:
```
"OPTIONS": {
    "init_command": "SET default_storage_engine=INNODB",
}

```

This sets the default storage engine upon connecting to the database. After your tables have been created, you should remove this option as it adds a query that is only needed during table creation to each database connection.


### Table names[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#table-names "Link to this heading")
There are [`db_table`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.db_table "django.db.models.Options.db_table") parameter.
### Savepoints[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#savepoints "Link to this heading")
Both the Django ORM and MySQL (when using the InnoDB [storage engine](https://docs.djangoproject.com/en/5.0/ref/databases/#mysql-storage-engines)) support database [savepoints](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#topics-db-transactions-savepoints).
If you use the MyISAM storage engine please be aware of the fact that you will receive database-generated errors if you try to use the [savepoint-related methods of the transactions API](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#topics-db-transactions-savepoints). The reason for this is that detecting the storage engine of a MySQL database/table is an expensive operation so it was decided it isn’t worth to dynamically convert these methods in no-op’s based in the results of such detection.
### Notes on specific fields[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#notes-on-specific-fields "Link to this heading")
#### Character fields[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#character-fields "Link to this heading")
Any fields that are stored with `VARCHAR` column types may have their `max_length` restricted to 255 characters if you are using `unique=True` for the field. This affects [`CharField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.CharField "django.db.models.CharField"), [`SlugField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.SlugField "django.db.models.SlugField"). See
####  `TextField` limitations[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#textfield-limitations "Link to this heading")
MySQL can index only the first N chars of a `BLOB` or `TEXT` column. Since `TextField` doesn’t have a defined length, you can’t mark it as `unique=True`. MySQL will report: “BLOB/TEXT column ‘<db_column>’ used in key specification without a key length”.
#### Fractional seconds support for Time and DateTime fields[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#fractional-seconds-support-for-time-and-datetime-fields "Link to this heading")
MySQL can store fractional seconds, provided that the column definition includes a fractional indication (e.g. `DATETIME(6)`).
Django will not upgrade existing columns to include fractional seconds if the database server supports it. If you want to enable them on an existing database, it’s up to you to either manually update the column on the target database, by executing a command like:
```
ALTER TABLE `your_table` MODIFY `your_datetime_column` DATETIME(6)

```

or using a [`RunSQL`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RunSQL "django.db.migrations.operations.RunSQL") operation in a [data migration](https://docs.djangoproject.com/en/5.0/topics/migrations/#data-migrations).
####  `TIMESTAMP` columns[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#timestamp-columns "Link to this heading")
If you are using a legacy database that contains `TIMESTAMP` columns, you must set [`USE_TZ = False`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_TZ) to avoid data corruption. [`inspectdb`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-inspectdb) maps these columns to [`DateTimeField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.DateTimeField "django.db.models.DateTimeField") and if you enable timezone support, both MySQL and Django will attempt to convert the values from UTC to local time.
### Row locking with `QuerySet.select_for_update()`[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#row-locking-with-queryset-select-for-update "Link to this heading")
MySQL and MariaDB do not support some options to the `SELECT ... FOR UPDATE` statement. If `select_for_update()` is used with an unsupported option, then a [`NotSupportedError`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.db.NotSupportedError "django.db.NotSupportedError") is raised.
Option | MariaDB | MySQL
---|---|---
`SKIP LOCKED` | X (≥10.6) | X
`NOWAIT` | X | X
`OF` |  | X
`NO KEY` |  |
When using `select_for_update()` on MySQL, make sure you filter a queryset against at least a set of fields contained in unique constraints or only against fields covered by indexes. Otherwise, an exclusive write lock will be acquired over the full table for the duration of the transaction.
### Automatic typecasting can cause unexpected results[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#automatic-typecasting-can-cause-unexpected-results "Link to this heading")
When performing a query on a string type, but with an integer value, MySQL will coerce the types of all values in the table to an integer before performing the comparison. If your table contains the values `'abc'`, `'def'` and you query for `WHERE mycolumn=0`, both rows will match. Similarly, `WHERE mycolumn=1` will match the value `'abc1'`. Therefore, string type fields included in Django will always cast the value to a string before using it in a query.
If you implement custom model fields that inherit from [`Field`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field "django.db.models.Field") directly, are overriding [`get_prep_value()`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field.get_prep_value "django.db.models.Field.get_prep_value"), or use [`RawSQL`](https://docs.djangoproject.com/en/5.0/ref/models/expressions/#django.db.models.expressions.RawSQL "django.db.models.expressions.RawSQL"), [`extra()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.extra "django.db.models.query.QuerySet.extra"), or [`raw()`](https://docs.djangoproject.com/en/5.0/topics/db/sql/#django.db.models.Manager.raw "django.db.models.Manager.raw"), you should ensure that you perform appropriate typecasting.
