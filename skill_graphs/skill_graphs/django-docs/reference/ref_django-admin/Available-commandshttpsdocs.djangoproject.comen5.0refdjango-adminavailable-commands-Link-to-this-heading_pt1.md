## Available commands[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#available-commands "Link to this heading")
###  `check`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#check "Link to this heading")

django-admin check [app_label [app_label ...]][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-check "Link to this definition")

Uses the [system check framework](https://docs.djangoproject.com/en/5.0/ref/checks/) to inspect the entire Django project for common problems.
By default, all apps will be checked. You can check a subset of apps by providing a list of app labels as arguments:
```
django-admin check auth admin myapp

```


--tag TAGS, -t TAGS[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-check-tag "Link to this definition")

The system check framework performs many different types of checks that are [categorized with tags](https://docs.djangoproject.com/en/5.0/ref/checks/#system-check-builtin-tags). You can use these tags to restrict the checks performed to just those in a particular category. For example, to perform only models and compatibility checks, run:
```
django-admin check --tag models --tag compatibility

```


--database DATABASE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-check-database "Link to this definition")

Specifies the database to run checks requiring database access:
```
django-admin check --database default --database other

```

By default, these checks will not be run.

--list-tags[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-check-list-tags "Link to this definition")

Lists all available tags.

--deploy[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-check-deploy "Link to this definition")

Activates some additional checks that are only relevant in a deployment setting.
You can use this option in your local development environment, but since your local development settings module may not have many of your production settings, you will probably want to point the `check` command at a different settings module, either by setting the [`DJANGO_SETTINGS_MODULE`](https://docs.djangoproject.com/en/5.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE) environment variable, or by passing the `--settings` option:
```
django-admin check --deploy --settings=production_settings

```

Or you could run it directly on a production or staging deployment to verify that the correct settings are in use (omitting `--settings`). You could even make it part of your integration test suite.

--fail-level {CRITICAL,ERROR,WARNING,INFO,DEBUG}[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-check-fail-level "Link to this definition")

Specifies the message level that will cause the command to exit with a non-zero status. Default is `ERROR`.
###  `compilemessages`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#compilemessages "Link to this heading")

django-admin compilemessages[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-compilemessages "Link to this definition")

Compiles `.po` files created by [`makemessages`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-makemessages) to `.mo` files for use with the built-in gettext support. See [Internationalization and localization](https://docs.djangoproject.com/en/5.0/topics/i18n/).

--locale LOCALE, -l LOCALE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-compilemessages-locale "Link to this definition")

Specifies the locale(s) to process. If not provided, all locales are processed.

--exclude EXCLUDE, -x EXCLUDE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-compilemessages-exclude "Link to this definition")

Specifies the locale(s) to exclude from processing. If not provided, no locales are excluded.

--use-fuzzy, -f[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-compilemessages-use-fuzzy "Link to this definition")

Includes
Example usage:
```
django-admin compilemessages --locale=pt_BR
django-admin compilemessages --locale=pt_BR --locale=fr -f
django-admin compilemessages -l pt_BR
django-admin compilemessages -l pt_BR -l fr --use-fuzzy
django-admin compilemessages --exclude=pt_BR
django-admin compilemessages --exclude=pt_BR --exclude=fr
django-admin compilemessages -x pt_BR
django-admin compilemessages -x pt_BR -x fr

```


--ignore PATTERN, -i PATTERN[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-compilemessages-ignore "Link to this definition")

Ignores directories matching the given
Example usage:
```
django-admin compilemessages --ignore=cache --ignore=outdated/*/locale

```

###  `createcachetable`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#createcachetable "Link to this heading")

django-admin createcachetable[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-createcachetable "Link to this definition")

Creates the cache tables for use with the database cache backend using the information from your settings file. See [Django’s cache framework](https://docs.djangoproject.com/en/5.0/topics/cache/) for more information.

--database DATABASE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-createcachetable-database "Link to this definition")

Specifies the database in which the cache table(s) will be created. Defaults to `default`.

--dry-run[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-createcachetable-dry-run "Link to this definition")

Prints the SQL that would be run without actually running it, so you can customize it or use the migrations framework.
###  `dbshell`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#dbshell "Link to this heading")

django-admin dbshell[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-dbshell "Link to this definition")

Runs the command-line client for the database engine specified in your [`ENGINE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASE-ENGINE) setting, with the connection parameters specified in your [`USER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USER), [`PASSWORD`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-PASSWORD), etc., settings.
  * For PostgreSQL, this runs the `psql` command-line client.
  * For MySQL, this runs the `mysql` command-line client.
  * For SQLite, this runs the `sqlite3` command-line client.
  * For Oracle, this runs the `sqlplus` command-line client.


This command assumes the programs are on your `PATH` so that a call to the program name (`psql`, `mysql`, `sqlite3`, `sqlplus`) will find the program in the right place. There’s no way to specify the location of the program manually.

--database DATABASE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-dbshell-database "Link to this definition")

Specifies the database onto which to open a shell. Defaults to `default`.

-- ARGUMENTS[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-dbshell-0 "Link to this definition")

Any arguments following a `--` divider will be passed on to the underlying command-line client. For example, with PostgreSQL you can use the `psql` command’s `-c` flag to execute a raw SQL query directly:
/ 
```
$ django-admin dbshell -- -c 'select current_user'
 current_user
--------------
 postgres
(1 row)

```

```
...\> django-admin dbshell -- -c 'select current_user'
 current_user
--------------
 postgres
(1 row)

```

On MySQL/MariaDB, you can do this with the `mysql` command’s `-e` flag:
/ 
```
$ django-admin dbshell -- -e "select user()"
+----------------------+
| user()               |
+----------------------+
| djangonaut@localhost |
+----------------------+

```

```
...\> django-admin dbshell -- -e "select user()"
+----------------------+
| user()               |
+----------------------+
| djangonaut@localhost |
+----------------------+

```

Note
Be aware that not all options set in the [`OPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-OPTIONS) part of your database configuration in [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES) are passed to the command-line client, e.g. `'isolation_level'`.
###  `diffsettings`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#diffsettings "Link to this heading")

django-admin diffsettings[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-diffsettings "Link to this definition")

Displays differences between the current settings file and Django’s default settings (or another settings file specified by [`--default`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-diffsettings-default)).
Settings that don’t appear in the defaults are followed by `"###"`. For example, the default settings don’t define [`ROOT_URLCONF`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ROOT_URLCONF), so [`ROOT_URLCONF`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ROOT_URLCONF) is followed by `"###"` in the output of `diffsettings`.

--all[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-diffsettings-all "Link to this definition")

Displays all settings, even if they have Django’s default value. Such settings are prefixed by `"###"`.

--default MODULE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-diffsettings-default "Link to this definition")

The settings module to compare the current settings against. Leave empty to compare against Django’s default settings.

--output {hash,unified}[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-diffsettings-output "Link to this definition")

Specifies the output format. Available values are `hash` and `unified`. `hash` is the default mode that displays the output that’s described above. `unified` displays the output similar to `diff -u`. Default settings are prefixed with a minus sign, followed by the changed setting prefixed with a plus sign.
###  `dumpdata`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#dumpdata "Link to this heading")

django-admin dumpdata [app_label[.ModelName] [app_label[.ModelName] ...]][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-dumpdata "Link to this definition")

Outputs to standard output all data in the database associated with the named application(s).
If no application name is provided, all installed applications will be dumped.
The output of `dumpdata` can be used as input for [`loaddata`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-loaddata).
When result of `dumpdata` is saved as a file, it can serve as a [fixture](https://docs.djangoproject.com/en/5.0/topics/db/fixtures/#fixtures-explanation) for [tests](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#topics-testing-fixtures) or as an [initial data](https://docs.djangoproject.com/en/5.0/howto/initial-data/#initial-data-via-fixtures).
Note that `dumpdata` uses the default manager on the model for selecting the records to dump. If you’re using a [custom manager](https://docs.djangoproject.com/en/5.0/topics/db/managers/#custom-managers) as the default manager and it filters some of the available records, not all of the objects will be dumped.

--all, -a[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-dumpdata-all "Link to this definition")

Uses Django’s base manager, dumping records which might otherwise be filtered or modified by a custom manager.

--format FORMAT[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-dumpdata-format "Link to this definition")

Specifies the serialization format of the output. Defaults to JSON. Supported formats are listed in [Serialization formats](https://docs.djangoproject.com/en/5.0/topics/serialization/#serialization-formats).

--indent INDENT[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-dumpdata-indent "Link to this definition")

Specifies the number of indentation spaces to use in the output. Defaults to `None` which displays all data on single line.

--exclude EXCLUDE, -e EXCLUDE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-dumpdata-exclude "Link to this definition")

Prevents specific applications or models (specified in the form of `app_label.ModelName`) from being dumped. If you specify a model name, then only that model will be excluded, rather than the entire application. You can also mix application names and model names.
If you want to exclude multiple applications, pass `--exclude` more than once:
```
django-admin dumpdata --exclude=auth --exclude=contenttypes

```


--database DATABASE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-dumpdata-database "Link to this definition")

Specifies the database from which data will be dumped. Defaults to `default`.

--natural-foreign[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-dumpdata-natural-foreign "Link to this definition")

Uses the `natural_key()` model method to serialize any foreign key and many-to-many relationship to objects of the type that defines the method. If you’re dumping `contrib.auth` `Permission` objects or `contrib.contenttypes` `ContentType` objects, you should probably use this flag. See the [natural keys](https://docs.djangoproject.com/en/5.0/topics/serialization/#topics-serialization-natural-keys) documentation for more details on this and the next option.

--natural-primary[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-dumpdata-natural-primary "Link to this definition")

Omits the primary key in the serialized data of this object since it can be calculated during deserialization.

--pks PRIMARY_KEYS[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-dumpdata-pks "Link to this definition")

Outputs only the objects specified by a comma separated list of primary keys. This is only available when dumping one model. By default, all the records of the model are output.

--output OUTPUT, -o OUTPUT[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-dumpdata-output "Link to this definition")

Specifies a file to write the serialized data to. By default, the data goes to standard output.
When this option is set and `--verbosity` is greater than 0 (the default), a progress bar is shown in the terminal.
#### Fixtures compression[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#fixtures-compression "Link to this heading")
The output file can be compressed with one of the `bz2`, `gz`, `lzma`, or `xz` formats by ending the filename with the corresponding extension. For example, to output the data as a compressed JSON file:
```
django-admin dumpdata -o mydata.json.gz

```

###  `flush`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#flush "Link to this heading")

django-admin flush[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-flush "Link to this definition")

Removes all data from the database and re-executes any post-synchronization handlers. The table of which migrations have been applied is not cleared.
If you would rather start from an empty database and rerun all migrations, you should drop and recreate the database and then run [`migrate`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-migrate) instead.

--noinput, --no-input[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-flush-noinput "Link to this definition")

Suppresses all user prompts.

--database DATABASE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-flush-database "Link to this definition")

Specifies the database to flush. Defaults to `default`.
###  `inspectdb`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#inspectdb "Link to this heading")

django-admin inspectdb [table [table ...]][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-inspectdb "Link to this definition")

Introspects the database tables in the database pointed-to by the [`NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-NAME) setting and outputs a Django model module (a `models.py` file) to standard output.
You may choose what tables or views to inspect by passing their names as arguments. If no arguments are provided, models are created for views only if the [`--include-views`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-inspectdb-include-views) option is used. Models for partition tables are created on PostgreSQL if the [`--include-partitions`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-inspectdb-include-partitions) option is used.
Use this if you have a legacy database with which you’d like to use Django. The script will inspect the database and create a model for each table within it.
As you might expect, the created models will have an attribute for every field in the table. Note that `inspectdb` has a few special cases in its field-name output:
  * If `inspectdb` cannot map a column’s type to a model field type, it’ll use `TextField` and will insert the Python comment `'This field type is a guess.'` next to the field in the generated model. The recognized fields may depend on apps listed in [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS). For example, [`django.contrib.postgres`](https://docs.djangoproject.com/en/5.0/ref/contrib/postgres/#module-django.contrib.postgres "django.contrib.postgres: PostgreSQL-specific fields and features") adds recognition for several PostgreSQL-specific field types.
  * If the database column name is a Python reserved word (such as `'pass'`, `'class'` or `'for'`), `inspectdb` will append `'_field'` to the attribute name. For example, if a table has a column `'for'`, the generated model will have a field `'for_field'`, with the `db_column` attribute set to `'for'`. `inspectdb` will insert the Python comment `'Field renamed because it was a Python reserved word.'` next to the field.


This feature is meant as a shortcut, not as definitive model generation. After you run it, you’ll want to look over the generated models yourself to make customizations. In particular, you’ll need to rearrange models’ order, so that models that refer to other models are ordered properly.
Django doesn’t create database defaults when a [`default`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field.default "django.db.models.Field.default") is specified on a model field. Similarly, database defaults aren’t translated to model field defaults or detected in any fashion by `inspectdb`.
By default, `inspectdb` creates unmanaged models. That is, `managed = False` in the model’s `Meta` class tells Django not to manage each table’s creation, modification, and deletion. If you do want to allow Django to manage the table’s lifecycle, you’ll need to change the [`managed`](https://docs.djangoproject.com/en/5.0/ref/models/options/#django.db.models.Options.managed "django.db.models.Options.managed") option to `True` (or remove it because `True` is its default value).
#### Database-specific notes[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#database-specific-notes "Link to this heading")
##### Oracle[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#oracle "Link to this heading")
  * Models are created for materialized views if [`--include-views`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-inspectdb-include-views) is used.


##### PostgreSQL[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#postgresql "Link to this heading")
  * Models are created for foreign tables.
  * Models are created for materialized views if [`--include-views`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-inspectdb-include-views) is used.
  * Models are created for partition tables if [`--include-partitions`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-inspectdb-include-partitions) is used.



--database DATABASE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-inspectdb-database "Link to this definition")

Specifies the database to introspect. Defaults to `default`.

--include-partitions[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-inspectdb-include-partitions "Link to this definition")

If this option is provided, models are also created for partitions.
Only support for PostgreSQL is implemented.

--include-views[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-inspectdb-include-views "Link to this definition")

If this option is provided, models are also created for database views.
###  `loaddata`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#loaddata "Link to this heading")

django-admin loaddata fixture [fixture ...][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-loaddata "Link to this definition")

Searches for and loads the contents of the named [fixture](https://docs.djangoproject.com/en/5.0/topics/db/fixtures/#fixtures-explanation) into the database.

--database DATABASE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-loaddata-database "Link to this definition")

Specifies the database into which the data will be loaded. Defaults to `default`.

--ignorenonexistent, -i[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-loaddata-ignorenonexistent "Link to this definition")

Ignores fields and models that may have been removed since the fixture was originally generated.

--app APP_LABEL[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-loaddata-app "Link to this definition")

Specifies a single app to look for fixtures in rather than looking in all apps.

--format FORMAT[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-loaddata-format "Link to this definition")

Specifies the [serialization format](https://docs.djangoproject.com/en/5.0/topics/serialization/#serialization-formats) (e.g., `json` or `xml`) for fixtures [read from stdin](https://docs.djangoproject.com/en/5.0/ref/django-admin/#loading-fixtures-stdin).

--exclude EXCLUDE, -e EXCLUDE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-loaddata-exclude "Link to this definition")

Excludes loading the fixtures from the given applications and/or models (in the form of `app_label` or `app_label.ModelName`). Use the option multiple times to exclude more than one app or model.
#### Loading fixtures from `stdin`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#loading-fixtures-from-stdin "Link to this heading")
You can use a dash as the fixture name to load input from `sys.stdin`. For example:
```
django-admin loaddata --format=json -

```

When reading from `stdin`, the [`--format`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-loaddata-format) option is required to specify the [serialization format](https://docs.djangoproject.com/en/5.0/topics/serialization/#serialization-formats) of the input (e.g., `json` or `xml`).
Loading from `stdin` is useful with standard input and output redirections. For example:
```
django-admin dumpdata --format=json --database=test app_label.ModelName | django-admin loaddata --format=json --database=prod -

```

The [`dumpdata`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-dumpdata) command can be used to generate input for `loaddata`.
See also
For more detail about fixtures see the [Fixtures](https://docs.djangoproject.com/en/5.0/topics/db/fixtures/#fixtures-explanation) topic.
###  `makemessages`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#makemessages "Link to this heading")

django-admin makemessages[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-makemessages "Link to this definition")

Runs over the entire source tree of the current directory and pulls out all strings marked for translation. It creates (or updates) a message file in the conf/locale (in the Django tree) or locale (for project and application) directory. After making changes to the messages files you need to compile them with [`compilemessages`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-compilemessages) for use with the builtin gettext support. See the [i18n documentation](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/#how-to-create-language-files) for details.
This command doesn’t require configured settings. However, when settings aren’t configured, the command can’t ignore the [`MEDIA_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_ROOT) and [`STATIC_ROOT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATIC_ROOT) directories or include [`LOCALE_PATHS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LOCALE_PATHS).

--all, -a[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemessages-all "Link to this definition")

Updates the message files for all available languages.

--extension EXTENSIONS, -e EXTENSIONS[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemessages-extension "Link to this definition")
