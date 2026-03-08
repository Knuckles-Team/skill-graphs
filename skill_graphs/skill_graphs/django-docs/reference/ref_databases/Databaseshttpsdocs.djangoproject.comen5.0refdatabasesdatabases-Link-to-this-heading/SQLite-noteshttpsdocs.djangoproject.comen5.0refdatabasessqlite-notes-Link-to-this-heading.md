## SQLite notes[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#sqlite-notes "Link to this heading")
Django supports SQLite 3.27.0 and later.
### Substring matching and case sensitivity[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#substring-matching-and-case-sensitivity "Link to this heading")
For all SQLite versions, there is some slightly counter-intuitive behavior when attempting to match some types of strings. These are triggered when using the [`iexact`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-iexact) or [`contains`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-contains) filters in Querysets. The behavior splits into two cases:
1. For substring matching, all matches are done case-insensitively. That is a filter such as `filter(name__contains="aa")` will match a name of `"Aabb"`.
2. For strings containing characters outside the ASCII range, all exact string matches are performed case-sensitively, even when the case-insensitive options are passed into the query. So the [`iexact`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-iexact) filter will behave exactly the same as the [`exact`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#std-fieldlookup-exact) filter in these cases.
Some possible workarounds for this are
### Decimal handling[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#decimal-handling "Link to this heading")
SQLite has no real decimal internal type. Decimal values are internally converted to the `REAL` data type (8-byte IEEE floating point number), as explained in the
### “Database is locked” errors[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#database-is-locked-errors "Link to this heading")
SQLite is meant to be a lightweight database, and thus can’t support a high level of concurrency. `OperationalError: database is locked` errors indicate that your application is experiencing more concurrency than `sqlite` can handle in default configuration. This error means that one thread or process has an exclusive lock on the database connection and another thread timed out waiting for the lock the be released.
Python’s SQLite wrapper has a default timeout value that determines how long the second thread is allowed to wait on the lock before it times out and raises the `OperationalError: database is locked` error.
If you’re getting this error, you can solve it by:
  * Switching to another database backend. At a certain point SQLite becomes too “lite” for real-world applications, and these sorts of concurrency errors indicate you’ve reached that point.
  * Rewriting your code to reduce concurrency and ensure that database transactions are short-lived.
  * Increase the default timeout value by setting the `timeout` database option:
```
"OPTIONS": {
    # ...
    "timeout": 20,
    # ...
}

```

This will make SQLite wait a bit longer before throwing “database is locked” errors; it won’t really do anything to solve them.


###  `QuerySet.select_for_update()` not supported[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#queryset-select-for-update-not-supported "Link to this heading")
SQLite does not support the `SELECT ... FOR UPDATE` syntax. Calling it will have no effect.
### Isolation when using `QuerySet.iterator()`[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#isolation-when-using-queryset-iterator "Link to this heading")
There are special considerations described in [`QuerySet.iterator()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.iterator "django.db.models.query.QuerySet.iterator"). If a row is added, changed, or deleted within the loop, then that row may or may not appear, or may appear twice, in subsequent results fetched from the iterator. Your code must handle this.
### Enabling JSON1 extension on SQLite[¶](https://docs.djangoproject.com/en/5.0/ref/databases/#enabling-json1-extension-on-sqlite "Link to this heading")
To use [`JSONField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.JSONField "django.db.models.JSONField") on SQLite, you need to enable the `fields.E180`) will be raised.
To enable the JSON1 extension you can follow the instruction on [the wiki page](https://code.djangoproject.com/wiki/JSON1Extension).
Note
The JSON1 extension is enabled by default on SQLite 3.38+.
