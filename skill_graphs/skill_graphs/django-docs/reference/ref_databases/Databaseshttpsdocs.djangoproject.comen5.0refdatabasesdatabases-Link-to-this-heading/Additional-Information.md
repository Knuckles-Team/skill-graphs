## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Scott Macpherson donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Databases](https://docs.djangoproject.com/en/5.0/ref/databases/)
    * [General notes](https://docs.djangoproject.com/en/5.0/ref/databases/#general-notes)
      * [Persistent connections](https://docs.djangoproject.com/en/5.0/ref/databases/#persistent-connections)
        * [Connection management](https://docs.djangoproject.com/en/5.0/ref/databases/#connection-management)
        * [Caveats](https://docs.djangoproject.com/en/5.0/ref/databases/#caveats)
      * [Encoding](https://docs.djangoproject.com/en/5.0/ref/databases/#encoding)
    * [PostgreSQL notes](https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes)
      * [PostgreSQL connection settings](https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-connection-settings)
      * [Optimizing PostgreSQL’s configuration](https://docs.djangoproject.com/en/5.0/ref/databases/#optimizing-postgresql-s-configuration)
      * [Isolation level](https://docs.djangoproject.com/en/5.0/ref/databases/#isolation-level)
      * [Role](https://docs.djangoproject.com/en/5.0/ref/databases/#role)
      * [Server-side parameters binding](https://docs.djangoproject.com/en/5.0/ref/databases/#server-side-parameters-binding)
      * [Indexes for `varchar` and `text` columns](https://docs.djangoproject.com/en/5.0/ref/databases/#indexes-for-varchar-and-text-columns)
      * [Migration operation for adding extensions](https://docs.djangoproject.com/en/5.0/ref/databases/#migration-operation-for-adding-extensions)
      * [Server-side cursors](https://docs.djangoproject.com/en/5.0/ref/databases/#server-side-cursors)
        * [Transaction pooling and server-side cursors](https://docs.djangoproject.com/en/5.0/ref/databases/#transaction-pooling-and-server-side-cursors)
      * [Manually-specifying values of auto-incrementing primary keys](https://docs.djangoproject.com/en/5.0/ref/databases/#manually-specifying-values-of-auto-incrementing-primary-keys)
      * [Test database templates](https://docs.djangoproject.com/en/5.0/ref/databases/#test-database-templates)
      * [Speeding up test execution with non-durable settings](https://docs.djangoproject.com/en/5.0/ref/databases/#speeding-up-test-execution-with-non-durable-settings)
    * [MariaDB notes](https://docs.djangoproject.com/en/5.0/ref/databases/#mariadb-notes)
    * [MySQL notes](https://docs.djangoproject.com/en/5.0/ref/databases/#mysql-notes)
      * [Version support](https://docs.djangoproject.com/en/5.0/ref/databases/#version-support)
      * [Storage engines](https://docs.djangoproject.com/en/5.0/ref/databases/#storage-engines)
      * [MySQL DB API Drivers](https://docs.djangoproject.com/en/5.0/ref/databases/#mysql-db-api-drivers)
        * [mysqlclient](https://docs.djangoproject.com/en/5.0/ref/databases/#mysqlclient)
        * [MySQL Connector/Python](https://docs.djangoproject.com/en/5.0/ref/databases/#id8)
      * [Time zone definitions](https://docs.djangoproject.com/en/5.0/ref/databases/#time-zone-definitions)
      * [Creating your database](https://docs.djangoproject.com/en/5.0/ref/databases/#creating-your-database)
        * [Collation settings](https://docs.djangoproject.com/en/5.0/ref/databases/#collation-settings)
      * [Connecting to the database](https://docs.djangoproject.com/en/5.0/ref/databases/#connecting-to-the-database)
        * [Setting `sql_mode`](https://docs.djangoproject.com/en/5.0/ref/databases/#setting-sql-mode)
        * [Isolation level](https://docs.djangoproject.com/en/5.0/ref/databases/#mysql-isolation-level)
      * [Creating your tables](https://docs.djangoproject.com/en/5.0/ref/databases/#creating-your-tables)
      * [Table names](https://docs.djangoproject.com/en/5.0/ref/databases/#table-names)
      * [Savepoints](https://docs.djangoproject.com/en/5.0/ref/databases/#savepoints)
      * [Notes on specific fields](https://docs.djangoproject.com/en/5.0/ref/databases/#notes-on-specific-fields)
        * [Character fields](https://docs.djangoproject.com/en/5.0/ref/databases/#character-fields)
        * [`TextField` limitations](https://docs.djangoproject.com/en/5.0/ref/databases/#textfield-limitations)
        * [Fractional seconds support for Time and DateTime fields](https://docs.djangoproject.com/en/5.0/ref/databases/#fractional-seconds-support-for-time-and-datetime-fields)
        * [`TIMESTAMP` columns](https://docs.djangoproject.com/en/5.0/ref/databases/#timestamp-columns)
      * [Row locking with `QuerySet.select_for_update()`](https://docs.djangoproject.com/en/5.0/ref/databases/#row-locking-with-queryset-select-for-update)
      * [Automatic typecasting can cause unexpected results](https://docs.djangoproject.com/en/5.0/ref/databases/#automatic-typecasting-can-cause-unexpected-results)
    * [SQLite notes](https://docs.djangoproject.com/en/5.0/ref/databases/#sqlite-notes)
      * [Substring matching and case sensitivity](https://docs.djangoproject.com/en/5.0/ref/databases/#substring-matching-and-case-sensitivity)
      * [Decimal handling](https://docs.djangoproject.com/en/5.0/ref/databases/#decimal-handling)
      * [“Database is locked” errors](https://docs.djangoproject.com/en/5.0/ref/databases/#database-is-locked-errors)
      * [`QuerySet.select_for_update()` not supported](https://docs.djangoproject.com/en/5.0/ref/databases/#queryset-select-for-update-not-supported)
      * [Isolation when using `QuerySet.iterator()`](https://docs.djangoproject.com/en/5.0/ref/databases/#isolation-when-using-queryset-iterator)
      * [Enabling JSON1 extension on SQLite](https://docs.djangoproject.com/en/5.0/ref/databases/#enabling-json1-extension-on-sqlite)
    * [Oracle notes](https://docs.djangoproject.com/en/5.0/ref/databases/#oracle-notes)
      * [Connecting to the database](https://docs.djangoproject.com/en/5.0/ref/databases/#id13)
        * [Full DSN and Easy Connect](https://docs.djangoproject.com/en/5.0/ref/databases/#full-dsn-and-easy-connect)
      * [Threaded option](https://docs.djangoproject.com/en/5.0/ref/databases/#threaded-option)
      * [INSERT … RETURNING INTO](https://docs.djangoproject.com/en/5.0/ref/databases/#insert-returning-into)
      * [Naming issues](https://docs.djangoproject.com/en/5.0/ref/databases/#naming-issues)
      * [NULL and empty strings](https://docs.djangoproject.com/en/5.0/ref/databases/#null-and-empty-strings)
      * [`TextField` limitations](https://docs.djangoproject.com/en/5.0/ref/databases/#id14)
    * [Subclassing the built-in database backends](https://docs.djangoproject.com/en/5.0/ref/databases/#subclassing-the-built-in-database-backends)
    * [Using a 3rd-party database backend](https://docs.djangoproject.com/en/5.0/ref/databases/#using-a-3rd-party-database-backend)


### Browse
  * Prev: [Cross Site Request Forgery protection](https://docs.djangoproject.com/en/5.0/ref/csrf/)
  * Next: [`django-admin` and `manage.py`](https://docs.djangoproject.com/en/5.0/ref/django-admin/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [API Reference](https://docs.djangoproject.com/en/5.0/ref/)
      * Databases


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
