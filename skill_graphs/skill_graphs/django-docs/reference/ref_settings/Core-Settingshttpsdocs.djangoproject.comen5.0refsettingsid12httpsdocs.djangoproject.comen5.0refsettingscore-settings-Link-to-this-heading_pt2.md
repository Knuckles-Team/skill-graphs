When [`USE_TZ`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_TZ) is `True`, reading datetimes from the database returns aware datetimes with the timezone set to this option’s value if not `None`, or to UTC otherwise.
When [`USE_TZ`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_TZ) is `False`, it is an error to set this option.
  * If the database backend doesn’t support time zones (e.g. SQLite, MySQL, Oracle), Django reads and writes datetimes in local time according to this option if it is set and in UTC if it isn’t.
Changing the connection time zone changes how datetimes are read from and written to the database.
    * If Django manages the database and you don’t have a strong reason to do otherwise, you should leave this option unset. It’s best to store datetimes in UTC because it avoids ambiguous or nonexistent datetimes during daylight saving time changes. Also, receiving datetimes in UTC keeps datetime arithmetic simple — there’s no need to consider potential offset changes over a DST transition.
    * If you’re connecting to a third-party database that stores datetimes in a local time rather than UTC, then you must set this option to the appropriate time zone. Likewise, if Django manages the database but third-party systems connect to the same database and expect to find datetimes in local time, then you must set this option.
  * If the database backend supports time zones (e.g., PostgreSQL), then the database connection’s time zone is set to this value.
Although setting the `TIME_ZONE` option is very rarely needed, there are situations where it becomes necessary. Specifically, it’s recommended to match the general [`TIME_ZONE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_ZONE) setting when dealing with raw queries involving date/time functions like PostgreSQL’s `date_trunc()` or `generate_series()`, especially when generating time-based series that transition daylight savings.
This value can be changed at any time, the database will handle the conversion of datetimes to the configured time zone.
However, this has a downside: receiving all datetimes in local time makes datetime arithmetic more tricky — you must account for possible offset changes over DST transitions.
Consider converting to local time explicitly with `AT TIME ZONE` in raw SQL queries instead of setting the `TIME_ZONE` option.


####  `DISABLE_SERVER_SIDE_CURSORS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#disable-server-side-cursors "Link to this heading")
Default: `False`
Set this to `True` if you want to disable the use of server-side cursors with [`QuerySet.iterator()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.iterator "django.db.models.query.QuerySet.iterator"). [Transaction pooling and server-side cursors](https://docs.djangoproject.com/en/5.0/ref/databases/#transaction-pooling-server-side-cursors) describes the use case.
This is a PostgreSQL-specific setting.
####  `USER`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#user "Link to this heading")
Default: `''` (Empty string)
The username to use when connecting to the database. Not used with SQLite.
####  `TEST`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#test "Link to this heading")
Default: `{}` (Empty dictionary)
A dictionary of settings for test databases; for more details about the creation and use of test databases, see [The test database](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#the-test-database).
Here’s an example with a test database configuration:
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "USER": "mydatabaseuser",
        "NAME": "mydatabase",
        "TEST": {
            "NAME": "mytestdatabase",
        },
    },
}

```

The following keys in the `TEST` dictionary are available:
#####  `CHARSET`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#charset "Link to this heading")
Default: `None`
The character set encoding used to create the test database. The value of this string is passed directly through to the database, so its format is backend-specific.
Supported by the `postgresql`) and `mysql`) backends.
#####  `COLLATION`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#collation "Link to this heading")
Default: `None`
The collation order to use when creating the test database. This value is passed directly to the backend, so its format is backend-specific.
Only supported for the `mysql` backend (see the
#####  `DEPENDENCIES`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#dependencies "Link to this heading")
Default: `['default']`, for all databases other than `default`, which has no dependencies.
The creation-order dependencies of the database. See the documentation on [controlling the creation order of test databases](https://docs.djangoproject.com/en/5.0/topics/testing/advanced/#topics-testing-creation-dependencies) for details.
#####  `MIGRATE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#migrate "Link to this heading")
Default: `True`
When set to `False`, migrations won’t run when creating the test database. This is similar to setting `None` as a value in [`MIGRATION_MODULES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIGRATION_MODULES), but for all apps.
#####  `MIRROR`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#mirror "Link to this heading")
Default: `None`
The alias of the database that this database should mirror during testing. It depends on transactions and therefore must be used within [`TransactionTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase") instead of [`TestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase").
This setting exists to allow for testing of primary/replica (referred to as master/slave by some databases) configurations of multiple databases. See the documentation on [testing primary/replica configurations](https://docs.djangoproject.com/en/5.0/topics/testing/advanced/#topics-testing-primaryreplica) for details.
#####  `NAME`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEST_NAME "Link to this heading")
Default: `None`
The name of database to use when running the test suite.
If the default value (`None`) is used with the SQLite database engine, the tests will use a memory resident database. For all other database engines the test database will use the name `'test_' + DATABASE_NAME`.
See [The test database](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#the-test-database).
#####  `TEMPLATE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#template "Link to this heading")
This is a PostgreSQL-specific setting.
The name of a `'template0'`) from which to create the test database.
#####  `CREATE_DB`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#create-db "Link to this heading")
Default: `True`
This is an Oracle-specific setting.
If it is set to `False`, the test tablespaces won’t be automatically created at the beginning of the tests or dropped at the end.
#####  `CREATE_USER`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#create-user "Link to this heading")
Default: `True`
This is an Oracle-specific setting.
If it is set to `False`, the test user won’t be automatically created at the beginning of the tests and dropped at the end.
#####  `USER`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEST_USER "Link to this heading")
Default: `None`
This is an Oracle-specific setting.
The username to use when connecting to the Oracle database that will be used when running tests. If not provided, Django will use `'test_' + USER`.
#####  `PASSWORD`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEST_PASSWD "Link to this heading")
Default: `None`
This is an Oracle-specific setting.
The password to use when connecting to the Oracle database that will be used when running tests. If not provided, Django will generate a random password.
#####  `ORACLE_MANAGED_FILES`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#oracle-managed-files "Link to this heading")
Default: `False`
This is an Oracle-specific setting.
If set to `True`, Oracle Managed Files (OMF) tablespaces will be used. [`DATAFILE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATAFILE) and [`DATAFILE_TMP`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATAFILE_TMP) will be ignored.
#####  `TBLSPACE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#tblspace "Link to this heading")
Default: `None`
This is an Oracle-specific setting.
The name of the tablespace that will be used when running tests. If not provided, Django will use `'test_' + USER`.
#####  `TBLSPACE_TMP`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#tblspace-tmp "Link to this heading")
Default: `None`
This is an Oracle-specific setting.
The name of the temporary tablespace that will be used when running tests. If not provided, Django will use `'test_' + USER + '_temp'`.
#####  `DATAFILE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#datafile "Link to this heading")
Default: `None`
This is an Oracle-specific setting.
The name of the datafile to use for the TBLSPACE. If not provided, Django will use `TBLSPACE + '.dbf'`.
#####  `DATAFILE_TMP`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#datafile-tmp "Link to this heading")
Default: `None`
This is an Oracle-specific setting.
The name of the datafile to use for the TBLSPACE_TMP. If not provided, Django will use `TBLSPACE_TMP + '.dbf'`.
#####  `DATAFILE_MAXSIZE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#datafile-maxsize "Link to this heading")
Default: `'500M'`
This is an Oracle-specific setting.
The maximum size that the DATAFILE is allowed to grow to.
#####  `DATAFILE_TMP_MAXSIZE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#datafile-tmp-maxsize "Link to this heading")
Default: `'500M'`
This is an Oracle-specific setting.
The maximum size that the DATAFILE_TMP is allowed to grow to.
#####  `DATAFILE_SIZE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#datafile-size "Link to this heading")
Default: `'50M'`
This is an Oracle-specific setting.
The initial size of the DATAFILE.
#####  `DATAFILE_TMP_SIZE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#datafile-tmp-size "Link to this heading")
Default: `'50M'`
This is an Oracle-specific setting.
The initial size of the DATAFILE_TMP.
#####  `DATAFILE_EXTSIZE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#datafile-extsize "Link to this heading")
Default: `'25M'`
This is an Oracle-specific setting.
The amount by which the DATAFILE is extended when more space is required.
#####  `DATAFILE_TMP_EXTSIZE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#datafile-tmp-extsize "Link to this heading")
Default: `'25M'`
This is an Oracle-specific setting.
The amount by which the DATAFILE_TMP is extended when more space is required.
###  `DATA_UPLOAD_MAX_MEMORY_SIZE`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#data-upload-max-memory-size "Link to this heading")
Default: `2621440` (i.e. 2.5 MB).
The maximum size in bytes that a request body may be before a [`SuspiciousOperation`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation") (`RequestDataTooBig`) is raised. The check is done when accessing `request.body` or `request.POST` and is calculated against the total request size excluding any file upload data. You can set this to `None` to disable the check. Applications that are expected to receive unusually large form posts should tune this setting.
The amount of request data is correlated to the amount of memory needed to process the request and populate the GET and POST dictionaries. Large requests could be used as a denial-of-service attack vector if left unchecked. Since web servers don’t typically perform deep request inspection, it’s not possible to perform a similar check at that level.
See also [`FILE_UPLOAD_MAX_MEMORY_SIZE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-FILE_UPLOAD_MAX_MEMORY_SIZE).
###  `DATA_UPLOAD_MAX_NUMBER_FIELDS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#data-upload-max-number-fields "Link to this heading")
Default: `1000`
The maximum number of parameters that may be received via GET or POST before a [`SuspiciousOperation`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation") (`TooManyFields`) is raised. You can set this to `None` to disable the check. Applications that are expected to receive an unusually large number of form fields should tune this setting.
The number of request parameters is correlated to the amount of time needed to process the request and populate the GET and POST dictionaries. Large requests could be used as a denial-of-service attack vector if left unchecked. Since web servers don’t typically perform deep request inspection, it’s not possible to perform a similar check at that level.
###  `DATA_UPLOAD_MAX_NUMBER_FILES`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#data-upload-max-number-files "Link to this heading")
New in Django 3.2.18.
Default: `100`
The maximum number of files that may be received via POST in a `multipart/form-data` encoded request before a [`SuspiciousOperation`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation") (`TooManyFiles`) is raised. You can set this to `None` to disable the check. Applications that are expected to receive an unusually large number of file fields should tune this setting.
The number of accepted files is correlated to the amount of time and memory needed to process the request. Large requests could be used as a denial-of-service attack vector if left unchecked. Since web servers don’t typically perform deep request inspection, it’s not possible to perform a similar check at that level.
###  `DATABASE_ROUTERS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#database-routers "Link to this heading")
Default: `[]` (Empty list)
The list of routers that will be used to determine which database to use when performing a database query.
See the documentation on [automatic database routing in multi database configurations](https://docs.djangoproject.com/en/5.0/topics/db/multi-db/#topics-db-multi-db-routing).
###  `DATE_FORMAT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#date-format "Link to this heading")
Default: `'N j, Y'` (e.g. `Feb. 4, 2003`)
The default formatting to use for displaying date fields in any part of the system. Note that the locale-dictated format has higher precedence and will be applied instead. See [`allowed date format strings`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatefilter-date).
See also [`DATETIME_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATETIME_FORMAT), [`TIME_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_FORMAT) and [`SHORT_DATE_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SHORT_DATE_FORMAT).
###  `DATE_INPUT_FORMATS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#date-input-formats "Link to this heading")
Default:
```
[
    "%Y-%m-%d",  # '2006-10-25'
    "%m/%d/%Y",  # '10/25/2006'
    "%m/%d/%y",  # '10/25/06'
    "%b %d %Y",  # 'Oct 25 2006'
    "%b %d, %Y",  # 'Oct 25, 2006'
    "%d %b %Y",  # '25 Oct 2006'
    "%d %b, %Y",  # '25 Oct, 2006'
    "%B %d %Y",  # 'October 25 2006'
    "%B %d, %Y",  # 'October 25, 2006'
    "%d %B %Y",  # '25 October 2006'
    "%d %B, %Y",  # '25 October, 2006'
]

```

A list of formats that will be accepted when inputting data on a date field. Formats will be tried in order, using the first valid one. Note that these format strings use Python’s [`date`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatefilter-date) template filter.
The locale-dictated format has higher precedence and will be applied instead.
See also [`DATETIME_INPUT_FORMATS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATETIME_INPUT_FORMATS) and [`TIME_INPUT_FORMATS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_INPUT_FORMATS).
###  `DATETIME_FORMAT`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#datetime-format "Link to this heading")
Default: `'N j, Y, P'` (e.g. `Feb. 4, 2003, 4 p.m.`)
The default formatting to use for displaying datetime fields in any part of the system. Note that the locale-dictated format has higher precedence and will be applied instead. See [`allowed date format strings`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatefilter-date).
See also [`DATE_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATE_FORMAT), [`TIME_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_FORMAT) and [`SHORT_DATETIME_FORMAT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SHORT_DATETIME_FORMAT).
###  `DATETIME_INPUT_FORMATS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#datetime-input-formats "Link to this heading")
Default:
```
[
    "%Y-%m-%d %H:%M:%S",  # '2006-10-25 14:30:59'
    "%Y-%m-%d %H:%M:%S.%f",  # '2006-10-25 14:30:59.000200'
    "%Y-%m-%d %H:%M",  # '2006-10-25 14:30'
    "%m/%d/%Y %H:%M:%S",  # '10/25/2006 14:30:59'
    "%m/%d/%Y %H:%M:%S.%f",  # '10/25/2006 14:30:59.000200'
    "%m/%d/%Y %H:%M",  # '10/25/2006 14:30'
    "%m/%d/%y %H:%M:%S",  # '10/25/06 14:30:59'
    "%m/%d/%y %H:%M:%S.%f",  # '10/25/06 14:30:59.000200'
    "%m/%d/%y %H:%M",  # '10/25/06 14:30'
]

```

A list of formats that will be accepted when inputting data on a datetime field. Formats will be tried in order, using the first valid one. Note that these format strings use Python’s [`date`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatefilter-date) template filter. Date-only formats are not included as datetime fields will automatically try [`DATE_INPUT_FORMATS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATE_INPUT_FORMATS) in last resort.
The locale-dictated format has higher precedence and will be applied instead.
See also [`DATE_INPUT_FORMATS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATE_INPUT_FORMATS) and [`TIME_INPUT_FORMATS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TIME_INPUT_FORMATS).
###  `DEBUG`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#debug "Link to this heading")
Default: `False`
A boolean that turns on/off debug mode.
Never deploy a site into production with [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) turned on.
One of the main features of debug mode is the display of detailed error pages. If your app raises an exception when [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is `True`, Django will display a detailed traceback, including a lot of metadata about your environment, such as all the currently defined Django settings (from `settings.py`).
As a security measure, Django will _not_ include settings that might be sensitive, such as [`SECRET_KEY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY). Specifically, it will exclude any setting whose name includes any of the following:
  * `'API'`
  * `'KEY'`
  * `'PASS'`
  * `'SECRET'`
  * `'SIGNATURE'`
  * `'TOKEN'`


Note that these are _partial_ matches. `'PASS'` will also match PASSWORD, just as `'TOKEN'` will also match TOKENIZED and so on.
Still, note that there are always going to be sections of your debug output that are inappropriate for public consumption. File paths, configuration options and the like all give attackers extra information about your server.
It is also important to remember that when running with [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) turned on, Django will remember every SQL query it executes. This is useful when you’re debugging, but it’ll rapidly consume memory on a production server.
Finally, if [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is `False`, you also need to properly set the [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ALLOWED_HOSTS) setting. Failing to do so will result in all requests being returned as “Bad Request (400)”.
Note
The default `settings.py` file created by [`django-admin startproject`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startproject) sets `DEBUG = True` for convenience.
###  `DEBUG_PROPAGATE_EXCEPTIONS`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#debug-propagate-exceptions "Link to this heading")
Default: `False`
If set to `True`, Django’s exception handling of view functions ([`handler500`](https://docs.djangoproject.com/en/5.0/ref/urls/#django.conf.urls.handler500 "django.conf.urls.handler500"), or the debug view if [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is `True`) and logging of 500 responses ([django.request](https://docs.djangoproject.com/en/5.0/ref/logging/#django-request-logger)) is skipped and exceptions propagate upward.
This can be useful for some test setups. It shouldn’t be used on a live site unless you want your web server (instead of Django) to generate “Internal Server Error” responses. In that case, make sure your server doesn’t show the stack trace or other sensitive information in the response.
###  `DECIMAL_SEPARATOR`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#decimal-separator "Link to this heading")
Default: `'.'` (Dot)
Default decimal separator used when formatting decimal numbers.
Note that the locale-dictated format has higher precedence and will be applied instead.
See also [`NUMBER_GROUPING`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-NUMBER_GROUPING), [`THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-THOUSAND_SEPARATOR) and [`USE_THOUSAND_SEPARATOR`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_THOUSAND_SEPARATOR).
###  `DEFAULT_AUTO_FIELD`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field "Link to this heading")
Default: `'`[`django.db.models.AutoField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.AutoField "django.db.models.AutoField")`'`
Default primary key field type to use for models that don’t have a field with [`primary_key=True`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field.primary_key "django.db.models.Field.primary_key").
Migrating auto-created through tables
The value of `DEFAULT_AUTO_FIELD` will be respected when creating new auto-created through tables for many-to-many relationships.
Unfortunately, the primary keys of existing auto-created through tables cannot currently be updated by the migrations framework.
This means that if you switch the value of `DEFAULT_AUTO_FIELD` and then generate migrations, the primary keys of the related models will be updated, as will the foreign keys from the through table, but the primary key of the auto-created through table will not be migrated.
In order to address this, you should add a [`RunSQL`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RunSQL "django.db.migrations.operations.RunSQL") operation to your migrations to perform the required `ALTER TABLE` step. You can check the existing table name through `sqlmigrate`, `dbshell`, or with the field’s `remote_field.through._meta.db_table` property.
Explicitly defined through models are already handled by the migrations system.
Allowing automatic migrations for the primary key of existing auto-created through tables [may be implemented at a later date](https://code.djangoproject.com/ticket/32674).
###  `DEFAULT_CHARSET`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#default-charset "Link to this heading")
Default: `'utf-8'`
Default charset to use for all `HttpResponse` objects, if a MIME type isn’t manually specified. Used when constructing the `Content-Type` header.
###  `DEFAULT_EXCEPTION_REPORTER`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#default-exception-reporter "Link to this heading")
Default: `'`[`django.views.debug.ExceptionReporter`](https://docs.djangoproject.com/en/5.0/howto/error-reporting/#django.views.debug.ExceptionReporter "django.views.debug.ExceptionReporter")`'`
Default exception reporter class to be used if none has been assigned to the [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") instance yet. See [Custom error reports](https://docs.djangoproject.com/en/5.0/howto/error-reporting/#custom-error-reports).
###  `DEFAULT_EXCEPTION_REPORTER_FILTER`[¶](https://docs.djangoproject.com/en/5.0/ref/settings/#default-exception-reporter-filter "Link to this heading")
Default: `'`[`django.views.debug.SafeExceptionReporterFilter`](https://docs.djangoproject.com/en/5.0/howto/error-reporting/#django.views.debug.SafeExceptionReporterFilter "django.views.debug.SafeExceptionReporterFilter")`'`
