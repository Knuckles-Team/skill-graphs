## PostgreSQL notes[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes "Link to this heading")
Django supports PostgreSQL 12 and higher.
Note
Support for `psycopg2` is likely to be deprecated and removed at some point in the future.
Changed in Django 4.2:
Support for `psycopg` 3.1.8+ was added.
### PostgreSQL connection settings[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-connection-settings "Link to this heading")
See [`HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-HOST) for details.
To connect using a service name from the [`OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-OPTIONS) part of your database configuration in [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES):
`settings.py`[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#id15 "Link to this code")
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "OPTIONS": {
            "service": "my_service",
            "passfile": ".my_pgpass",
        },
    }
}

```

`.pg_service.conf`[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#id16 "Link to this code")
```
[my_service]
host=localhost
user=USER
dbname=NAME
port=5432

```

`.my_pgpass`[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#id17 "Link to this code")
```
localhost:5432:NAME:USER:PASSWORD

```

The PostgreSQL backend passes the content of [`OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-OPTIONS) as keyword arguments to the connection constructor, allowing for more advanced control of driver behavior. All available
Warning
Using a service name for testing purposes is not supported. This [may be implemented later](https://code.djangoproject.com/ticket/33685).
### Optimizing PostgreSQL’s configuration[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#optimizing-postgresql-s-configuration "Link to this heading")
Django needs the following parameters for its database connections:
  * `client_encoding`: `'UTF8'`,
  * `default_transaction_isolation`: `'read committed'` by default, or the value set in the connection options (see below),
  *

`timezone`:

    * when [`USE_TZ`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_TZ) is `True`, `'UTC'` by default, or the [`TIME_ZONE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASE-TIME_ZONE) value set for the connection,
    * when [`USE_TZ`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_TZ) is `False`, the value of the global [`TIME_ZONE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_ZONE) setting.


If these parameters already have the correct values, Django won’t set them for every new connection, which improves performance slightly. You can configure them directly in `postgresql.conf` or more conveniently per database user with
Django will work just fine without this optimization, but each new connection will do some additional queries to set these parameters.
### Isolation level[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#isolation-level "Link to this heading")
Like PostgreSQL itself, Django defaults to the `READ COMMITTED` `REPEATABLE READ` or `SERIALIZABLE`, set it in the [`OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-OPTIONS) part of your database configuration in [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES):
```
from django.db.backends.postgresql.psycopg_any import IsolationLevel

DATABASES = {
    # ...
    "OPTIONS": {
        "isolation_level": IsolationLevel.SERIALIZABLE,
    },
}

```

Note
Under higher isolation levels, your application should be prepared to handle exceptions raised on serialization failures. This option is designed for advanced uses.
Changed in Django 4.2:
`IsolationLevel` was added.
### Role[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#role "Link to this heading")
New in Django 4.2.
If you need to use a different role for database connections than the role use to establish the connection, set it in the [`OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-OPTIONS) part of your database configuration in [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES):
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # ...
        "OPTIONS": {
            "assume_role": "my_application_role",
        },
    },
}

```

### Server-side parameters binding[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#server-side-parameters-binding "Link to this heading")
New in Django 4.2.
With [`OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-OPTIONS) part of your database configuration in [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES):
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # ...
        "OPTIONS": {
            "server_side_binding": True,
        },
    },
}

```

This option is ignored with `psycopg2`.
### Indexes for `varchar` and `text` columns[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#indexes-for-varchar-and-text-columns "Link to this heading")
When specifying `db_index=True` on your model fields, Django typically outputs a single `CREATE INDEX` statement. However, if the database type for the field is either `varchar` or `text` (e.g., used by `CharField`, `FileField`, and `TextField`), then Django will create an additional index that uses an appropriate `LIKE` operator in their SQL, as is done with the `contains` and `startswith` lookup types.
### Migration operation for adding extensions[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#migration-operation-for-adding-extensions "Link to this heading")
If you need to add a PostgreSQL extension (like `hstore`, `postgis`, etc.) using a migration, use the [`CreateExtension`](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/operations/#django.contrib.postgres.operations.CreateExtension "django.contrib.postgres.operations.CreateExtension") operation.
### Server-side cursors[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#server-side-cursors "Link to this heading")
When using [`QuerySet.iterator()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.iterator "django.db.models.query.QuerySet.iterator"), Django opens a
#### Transaction pooling and server-side cursors[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#transaction-pooling-and-server-side-cursors "Link to this heading")
Using a connection pooler in transaction pooling mode (e.g.
Server-side cursors are local to a connection and remain open at the end of a transaction when [`AUTOCOMMIT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASE-AUTOCOMMIT) is `True`. A subsequent transaction may attempt to fetch more results from a server-side cursor. In transaction pooling mode, there’s no guarantee that subsequent transactions will use the same connection. If a different connection is used, an error is raised when the transaction references the server-side cursor, because server-side cursors are only accessible in the connection in which they were created.
One solution is to disable server-side cursors for a connection in [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES) by setting [`DISABLE_SERVER_SIDE_CURSORS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASE-DISABLE_SERVER_SIDE_CURSORS) to `True`.
To benefit from server-side cursors in transaction pooling mode, you could set up [another connection to the database](https://docs.djangoproject.com/en/5.0/topics/db/multi-db/) in order to perform queries that use server-side cursors. This connection needs to either be directly to the database or to a connection pooler in session pooling mode.
Another option is to wrap each `QuerySet` using server-side cursors in an [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") block, because it disables `autocommit` for the duration of the transaction. This way, the server-side cursor will only live for the duration of the transaction.
### Manually-specifying values of auto-incrementing primary keys[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#manually-specifying-values-of-auto-incrementing-primary-keys "Link to this heading")
Django uses PostgreSQL’s identity columns to store auto-incrementing primary keys. An identity column is populated with values from a
```
>>> from django.contrib.auth.models import User
>>> User.objects.create(username="alice", pk=1)
<User: alice>
>>> # The sequence hasn't been updated; its next value is 1.
>>> User.objects.create(username="bob")
IntegrityError: duplicate key value violates unique constraint
"auth_user_pkey" DETAIL:  Key (id)=(1) already exists.

```

If you need to specify such values, reset the sequence afterward to avoid reusing a value that’s already in the table. The [`sqlsequencereset`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-sqlsequencereset) management command generates the SQL statements to do that.
### Test database templates[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#test-database-templates "Link to this heading")
You can use the [`TEST['TEMPLATE']`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEST_TEMPLATE) setting to specify a `'template0'`) from which to create a test database.
### Speeding up test execution with non-durable settings[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#speeding-up-test-execution-with-non-durable-settings "Link to this heading")
You can speed up test execution times by
Warning
This is dangerous: it will make your database more susceptible to data loss or corruption in the case of a server crash or power loss. Only use this on a development machine where you can easily restore the entire contents of all databases in the cluster.
