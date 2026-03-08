## Oracle notes[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#oracle-notes "Link to this heading")
Django supports
Deprecated since version 5.0: Support for `cx_Oracle` is deprecated.
In order for the `python manage.py migrate` command to work, your Oracle database user must have privileges to run the following commands:
  * CREATE TABLE
  * CREATE SEQUENCE
  * CREATE PROCEDURE
  * CREATE TRIGGER


To run a project’s test suite, the user usually needs these _additional_ privileges:
  * CREATE USER
  * ALTER USER
  * DROP USER
  * CREATE TABLESPACE
  * DROP TABLESPACE
  * CREATE SESSION WITH ADMIN OPTION
  * CREATE TABLE WITH ADMIN OPTION
  * CREATE SEQUENCE WITH ADMIN OPTION
  * CREATE PROCEDURE WITH ADMIN OPTION
  * CREATE TRIGGER WITH ADMIN OPTION


While the `RESOURCE` role has the required `CREATE TABLE`, `CREATE SEQUENCE`, `CREATE PROCEDURE`, and `CREATE TRIGGER` privileges, and a user granted `RESOURCE WITH ADMIN OPTION` can grant `RESOURCE`, such a user cannot grant the individual privileges (e.g. `CREATE TABLE`), and thus `RESOURCE WITH ADMIN OPTION` is not usually sufficient for running tests.
Some test suites also create views or materialized views; to run these, the user also needs `CREATE VIEW WITH ADMIN OPTION` and `CREATE MATERIALIZED VIEW WITH ADMIN OPTION` privileges. In particular, this is needed for Django’s own test suite.
All of these privileges are included in the DBA role, which is appropriate for use on a private developer’s database.
The Oracle database backend uses the `SYS.DBMS_LOB` and `SYS.DBMS_RANDOM` packages, so your user will require execute permissions on it. It’s normally accessible to all users by default, but in case it is not, you’ll need to grant permissions like so:
```
GRANT EXECUTE ON SYS.DBMS_LOB TO user;
GRANT EXECUTE ON SYS.DBMS_RANDOM TO user;

```

### Connecting to the database[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#id13 "Link to this heading")
To connect using the service name of your Oracle database, your `settings.py` file should look something like this:
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.oracle",
        "NAME": "xe",
        "USER": "a_user",
        "PASSWORD": "a_password",
        "HOST": "",
        "PORT": "",
    }
}

```

In this case, you should leave both [`HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-HOST) and [`PORT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-PORT) empty. However, if you don’t use a `tnsnames.ora` file or a similar naming method and want to connect using the SID (“xe” in this example), then fill in both [`HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-HOST) and [`PORT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-PORT) like so:
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.oracle",
        "NAME": "xe",
        "USER": "a_user",
        "PASSWORD": "a_password",
        "HOST": "dbprod01ned.mycompany.com",
        "PORT": "1540",
    }
}

```

You should either supply both [`HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-HOST) and [`PORT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-PORT), or leave both as empty strings. Django will use a different connect descriptor depending on that choice.
#### Full DSN and Easy Connect[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#full-dsn-and-easy-connect "Link to this heading")
A Full DSN or Easy Connect string can be used in [`NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-NAME) if both [`HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-HOST) and [`PORT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-PORT) are empty. This format is required when using RAC or pluggable databases without `tnsnames.ora`, for example.
Example of an Easy Connect string:
```
"NAME": "localhost:1521/orclpdb1"

```

Example of a full DSN string:
```
"NAME": (
    "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))"
    "(CONNECT_DATA=(SERVICE_NAME=orclpdb1)))"
)

```

### Threaded option[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#threaded-option "Link to this heading")
If you plan to run Django in a multithreaded environment (e.g. Apache using the default MPM module on any modern operating system), then you **must** set the `threaded` option of your Oracle database configuration to `True`:
```
"OPTIONS": {
    "threaded": True,
}

```

Failure to do this may result in crashes and other odd behavior.
### INSERT … RETURNING INTO[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#insert-returning-into "Link to this heading")
By default, the Oracle backend uses a `RETURNING INTO` clause to efficiently retrieve the value of an `AutoField` when inserting new rows. This behavior may result in a `DatabaseError` in certain unusual setups, such as when inserting into a remote table, or into a view with an `INSTEAD OF` trigger. The `RETURNING INTO` clause can be disabled by setting the `use_returning_into` option of the database configuration to `False`:
```
"OPTIONS": {
    "use_returning_into": False,
}

```

In this case, the Oracle backend will use a separate `SELECT` query to retrieve `AutoField` values.
### Naming issues[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#naming-issues "Link to this heading")
Oracle imposes a name length limit of 30 characters. To accommodate this, the backend truncates database identifiers to fit, replacing the final four characters of the truncated name with a repeatable MD5 hash value. Additionally, the backend turns database identifiers to all-uppercase.
To prevent these transformations (this is usually required only when dealing with legacy databases or accessing tables which belong to other users), use a quoted name as the value for `db_table`:
```
class LegacyModel(models.Model):
    class Meta:
        db_table = '"name_left_in_lowercase"'


class ForeignModel(models.Model):
    class Meta:
        db_table = '"OTHER_USER"."NAME_ONLY_SEEMS_OVER_30"'

```

Quoted names can also be used with Django’s other supported database backends; except for Oracle, however, the quotes have no effect.
When running `migrate`, an `ORA-06552` error may be encountered if certain Oracle keywords are used as the name of a model field or the value of a `db_column` option. Django quotes all identifiers used in queries to prevent most such problems, but this error can still occur when an Oracle datatype is used as a column name. In particular, take care to avoid using the names `date`, `timestamp`, `number` or `float` as a field name.
### NULL and empty strings[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#null-and-empty-strings "Link to this heading")
Django generally prefers to use the empty string (`''`) rather than `NULL`, but Oracle treats both identically. To get around this, the Oracle backend ignores an explicit `null` option on fields that have the empty string as a possible value and generates DDL as if `null=True`. When fetching from the database, it is assumed that a `NULL` value in one of these fields really means the empty string, and the data is silently converted to reflect this assumption.
###  `TextField` limitations[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#id14 "Link to this heading")
The Oracle backend stores `TextFields` as `NCLOB` columns. Oracle imposes some limitations on the usage of such LOB columns in general:
  * LOB columns may not be used as primary keys.
  * LOB columns may not be used in indexes.
  * LOB columns may not be used in a `SELECT DISTINCT` list. This means that attempting to use the `QuerySet.distinct` method on a model that includes `TextField` columns will result in an `ORA-00932` error when run against Oracle. As a workaround, use the `QuerySet.defer` method in conjunction with `distinct()` to prevent `TextField` columns from being included in the `SELECT DISTINCT` list.
