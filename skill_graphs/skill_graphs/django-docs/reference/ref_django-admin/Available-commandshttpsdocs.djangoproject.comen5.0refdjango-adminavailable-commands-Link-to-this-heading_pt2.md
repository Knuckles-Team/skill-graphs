
Specifies a list of file extensions to examine (default: `html`, `txt`, `py` or `js` if [`--domain`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemessages-domain) is `djangojs`).
Example usage:
```
django-admin makemessages --locale=de --extension xhtml

```

Separate multiple extensions with commas or use `-e` or `--extension` multiple times:
```
django-admin makemessages --locale=de --extension=html,txt --extension xml

```


--locale LOCALE, -l LOCALE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemessages-locale "Link to this definition")

Specifies the locale(s) to process.

--exclude EXCLUDE, -x EXCLUDE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemessages-exclude "Link to this definition")

Specifies the locale(s) to exclude from processing. If not provided, no locales are excluded.
Example usage:
```
django-admin makemessages --locale=pt_BR
django-admin makemessages --locale=pt_BR --locale=fr
django-admin makemessages -l pt_BR
django-admin makemessages -l pt_BR -l fr
django-admin makemessages --exclude=pt_BR
django-admin makemessages --exclude=pt_BR --exclude=fr
django-admin makemessages -x pt_BR
django-admin makemessages -x pt_BR -x fr

```


--domain DOMAIN, -d DOMAIN[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemessages-domain "Link to this definition")

Specifies the domain of the messages files. Supported options are:
  * `django` for all `*.py`, `*.html` and `*.txt` files (default)
  * `djangojs` for `*.js` files



--symlinks, -s[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemessages-symlinks "Link to this definition")

Follows symlinks to directories when looking for new translation strings.
Example usage:
```
django-admin makemessages --locale=de --symlinks

```


--ignore PATTERN, -i PATTERN[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemessages-ignore "Link to this definition")

Ignores files or directories matching the given
These patterns are used by default: `'CVS'`, `'.*'`, `'*~'`, `'*.pyc'`.
Example usage:
```
django-admin makemessages --locale=en_US --ignore=apps/* --ignore=secret/*.html

```


--no-default-ignore[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemessages-no-default-ignore "Link to this definition")

Disables the default values of `--ignore`.

--no-wrap[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemessages-no-wrap "Link to this definition")

Disables breaking long message lines into several lines in language files.

--no-location[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemessages-no-location "Link to this definition")

Suppresses writing ‘`#: filename:line`’ comment lines in language files. Using this option makes it harder for technically skilled translators to understand each message’s context.

--add-location [{full,file,never}][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemessages-add-location "Link to this definition")

Controls `#: filename:line` comment lines in language files. If the option is:
  * `full` (the default if not given): the lines include both file name and line number.
  * `file`: the line number is omitted.
  * `never`: the lines are suppressed (same as [`--no-location`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemessages-no-location)).


Requires `gettext` 0.19 or newer.

--no-obsolete[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemessages-no-obsolete "Link to this definition")

Removes obsolete message strings from the `.po` files.

--keep-pot[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemessages-keep-pot "Link to this definition")

Prevents deleting the temporary `.pot` files generated before creating the `.po` file. This is useful for debugging errors which may prevent the final language files from being created.
See also
See [Customizing the makemessages command](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/#customizing-makemessages) for instructions on how to customize the keywords that [`makemessages`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-makemessages) passes to `xgettext`.
###  `makemigrations`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#makemigrations "Link to this heading")

django-admin makemigrations [app_label [app_label ...]][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-makemigrations "Link to this definition")

Creates new migrations based on the changes detected to your models. Migrations, their relationship with apps and more are covered in depth in [the migrations documentation](https://docs.djangoproject.com/en/5.0/topics/migrations/).
Providing one or more app names as arguments will limit the migrations created to the app(s) specified and any dependencies needed (the table at the other end of a `ForeignKey`, for example).
To add migrations to an app that doesn’t have a `migrations` directory, run `makemigrations` with the app’s `app_label`.

--noinput, --no-input[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemigrations-noinput "Link to this definition")

Suppresses all user prompts. If a suppressed prompt cannot be resolved automatically, the command will exit with error code 3.

--empty[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemigrations-empty "Link to this definition")

Outputs an empty migration for the specified apps, for manual editing. This is for advanced users and should not be used unless you are familiar with the migration format, migration operations, and the dependencies between your migrations.

--dry-run[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemigrations-dry-run "Link to this definition")

Shows what migrations would be made without actually writing any migrations files to disk. Using this option along with `--verbosity 3` will also show the complete migrations files that would be written.

--merge[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemigrations-merge "Link to this definition")

Enables fixing of migration conflicts.

--name NAME, -n NAME[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemigrations-name "Link to this definition")

Allows naming the generated migration(s) instead of using a generated name. The name must be a valid Python

--no-header[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemigrations-no-header "Link to this definition")

Generate migration files without Django version and timestamp header.

--check[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemigrations-check "Link to this definition")

Makes `makemigrations` exit with a non-zero status when model changes without migrations are detected. Implies `--dry-run`.
Changed in Django 4.2:
In older versions, the missing migrations were also created when using the `--check` option.

--scriptable[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemigrations-scriptable "Link to this definition")

Diverts log output and input prompts to `stderr`, writing only paths of generated migration files to `stdout`.

--update[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemigrations-update "Link to this definition")

New in Django 4.2.
Merges model changes into the latest migration and optimize the resulting operations.
The updated migration will have a generated name. In order to preserve the previous name, set it using `--name`.
###  `migrate`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#migrate "Link to this heading")

django-admin migrate [app_label] [migration_name][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-migrate "Link to this definition")

Synchronizes the database state with the current set of models and migrations. Migrations, their relationship with apps and more are covered in depth in [the migrations documentation](https://docs.djangoproject.com/en/5.0/topics/migrations/).
The behavior of this command changes depending on the arguments provided:
  * No arguments: All apps have all of their migrations run.
  * `<app_label>`: The specified app has its migrations run, up to the most recent migration. This may involve running other apps’ migrations too, due to dependencies.
  * `<app_label> <migrationname>`: Brings the database schema to a state where the named migration is applied, but no later migrations in the same app are applied. This may involve unapplying migrations if you have previously migrated past the named migration. You can use a prefix of the migration name, e.g. `0001`, as long as it’s unique for the given app name. Use the name `zero` to migrate all the way back i.e. to revert all applied migrations for an app.


Warning
When unapplying migrations, all dependent migrations will also be unapplied, regardless of `<app_label>`. You can use `--plan` to check which migrations will be unapplied.

--database DATABASE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-migrate-database "Link to this definition")

Specifies the database to migrate. Defaults to `default`.

--fake[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-migrate-fake "Link to this definition")

Marks the migrations up to the target one (following the rules above) as applied, but without actually running the SQL to change your database schema.
This is intended for advanced users to manipulate the current migration state directly if they’re manually applying changes; be warned that using `--fake` runs the risk of putting the migration state table into a state where manual recovery will be needed to make migrations run correctly.

--fake-initial[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-migrate-fake-initial "Link to this definition")

Allows Django to skip an app’s initial migration if all database tables with the names of all models created by all [`CreateModel`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.CreateModel "django.db.migrations.operations.CreateModel") operations in that migration already exist. This option is intended for use when first running migrations against a database that preexisted the use of migrations. This option does not, however, check for matching database schema beyond matching table names and so is only safe to use if you are confident that your existing schema matches what is recorded in your initial migration.

--plan[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-migrate-plan "Link to this definition")

Shows the migration operations that will be performed for the given `migrate` command.

--run-syncdb[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-migrate-run-syncdb "Link to this definition")

Allows creating tables for apps without migrations. While this isn’t recommended, the migrations framework is sometimes too slow on large projects with hundreds of models.

--noinput, --no-input[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-migrate-noinput "Link to this definition")

Suppresses all user prompts. An example prompt is asking about removing stale content types.

--check[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-migrate-check "Link to this definition")

Makes `migrate` exit with a non-zero status when unapplied migrations are detected.

--prune[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-migrate-prune "Link to this definition")

Deletes nonexistent migrations from the `django_migrations` table. This is useful when migration files replaced by a squashed migration have been removed. See [Squashing migrations](https://docs.djangoproject.com/en/5.0/topics/migrations/#migration-squashing) for more details.
###  `optimizemigration`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#optimizemigration "Link to this heading")

django-admin optimizemigration app_label migration_name[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-optimizemigration "Link to this definition")

Optimizes the operations for the named migration and overrides the existing file. If the migration contains functions that must be manually copied, the command creates a new migration file suffixed with `_optimized` that is meant to replace the named migration.

--check[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-optimizemigration-check "Link to this definition")

Makes `optimizemigration` exit with a non-zero status when a migration can be optimized.
###  `runserver`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#runserver "Link to this heading")

django-admin runserver [addrport][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-runserver "Link to this definition")

Starts a lightweight development web server on the local machine. By default, the server runs on port 8000 on the IP address `127.0.0.1`. You can pass in an IP address and port number explicitly.
If you run this script as a user with normal privileges (recommended), you might not have access to start a port on a low port number. Low port numbers are reserved for the superuser (root).
This server uses the WSGI application object specified by the [`WSGI_APPLICATION`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-WSGI_APPLICATION) setting.
DO NOT USE THIS SERVER IN A PRODUCTION SETTING. It has not gone through security audits or performance tests. (And that’s how it’s gonna stay. We’re in the business of making web frameworks, not web servers, so improving this server to be able to handle a production environment is outside the scope of Django.)
The development server automatically reloads Python code for each request, as needed. You don’t need to restart the server for code changes to take effect. However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.
If you’re using Linux or MacOS and install both `pywatchman` 1.2.0 and higher.
Large directories with many files may cause performance issues
When using Watchman with a project that includes large non-Python directories like `node_modules`, it’s advisable to ignore this directory for optimal performance. See the
Watchman timeout

DJANGO_WATCHMAN_TIMEOUT[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#envvar-DJANGO_WATCHMAN_TIMEOUT "Link to this definition")

The default timeout of `Watchman` client is 5 seconds. You can change it by setting the [`DJANGO_WATCHMAN_TIMEOUT`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#envvar-DJANGO_WATCHMAN_TIMEOUT) environment variable.
When you start the server, and each time you change Python code while the server is running, the system check framework will check your entire Django project for some common errors (see the [`check`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-check) command). If any errors are found, they will be printed to standard output. You can use the `--skip-checks` option to skip running system checks.
You can run as many concurrent servers as you want, as long as they’re on separate ports by executing `django-admin runserver` more than once.
Note that the default IP address, `127.0.0.1`, is not accessible from other machines on your network. To make your development server viewable to other machines on the network, use its own IP address (e.g. `192.168.2.1`), `0` (shortcut for `0.0.0.0`), `0.0.0.0`, or `::` (with IPv6 enabled).
You can provide an IPv6 address surrounded by brackets (e.g. `[200a::1]:8000`). This will automatically enable IPv6 support.
A hostname containing ASCII-only characters can also be used.
If the [staticfiles](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/) contrib app is enabled (default in new projects) the [`runserver`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-runserver) command will be overridden with its own [runserver](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#staticfiles-runserver) command.
Logging of each request and response of the server is sent to the [django.server](https://docs.djangoproject.com/en/5.0/ref/logging/#django-server-logger) logger.

--noreload[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-runserver-noreload "Link to this definition")

Disables the auto-reloader. This means any Python code changes you make while the server is running will _not_ take effect if the particular Python modules have already been loaded into memory.

--nothreading[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-runserver-nothreading "Link to this definition")

Disables use of threading in the development server. The server is multithreaded by default.

--ipv6, -6[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-runserver-ipv6 "Link to this definition")

Uses IPv6 for the development server. This changes the default IP address from `127.0.0.1` to `::1`.
#### Examples of using different ports and addresses[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#examples-of-using-different-ports-and-addresses "Link to this heading")
Port 8000 on IP address `127.0.0.1`:
```
django-admin runserver

```

Port 8000 on IP address `1.2.3.4`:
```
django-admin runserver 1.2.3.4:8000

```

Port 7000 on IP address `127.0.0.1`:
```
django-admin runserver 7000

```

Port 7000 on IP address `1.2.3.4`:
```
django-admin runserver 1.2.3.4:7000

```

Port 8000 on IPv6 address `::1`:
```
django-admin runserver -6

```

Port 7000 on IPv6 address `::1`:
```
django-admin runserver -6 7000

```

Port 7000 on IPv6 address `2001:0db8:1234:5678::9`:
```
django-admin runserver [2001:0db8:1234:5678::9]:7000

```

Port 8000 on IPv4 address of host `localhost`:
```
django-admin runserver localhost:8000

```

Port 8000 on IPv6 address of host `localhost`:
```
django-admin runserver -6 localhost:8000

```

#### Serving static files with the development server[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#serving-static-files-with-the-development-server "Link to this heading")
By default, the development server doesn’t serve any static files for your site (such as CSS files, images, things under [`MEDIA_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_URL) and so forth). If you want to configure Django to serve static media, read [How to manage static files (e.g. images, JavaScript, CSS)](https://docs.djangoproject.com/en/5.0/howto/static-files/).
#### Serving with ASGI in development[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#serving-with-asgi-in-development "Link to this heading")
Django’s `runserver` command provides a WSGI server. In order to run under ASGI you will need to use an [ASGI server](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/). The Django Daphne project provides [Integration with runserver](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/daphne/#daphne-runserver) that you can use.
###  `sendtestemail`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#sendtestemail "Link to this heading")

django-admin sendtestemail [email [email ...]][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-sendtestemail "Link to this definition")

Sends a test email (to confirm email sending through Django is working) to the recipient(s) specified. For example:
```
django-admin sendtestemail foo@example.com bar@example.com

```

There are a couple of options, and you may use any combination of them together:

--managers[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-sendtestemail-managers "Link to this definition")

Mails the email addresses specified in [`MANAGERS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MANAGERS) using [`mail_managers()`](https://docs.djangoproject.com/en/5.0/topics/email/#django.core.mail.mail_managers "django.core.mail.mail_managers").

--admins[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-sendtestemail-admins "Link to this definition")

Mails the email addresses specified in [`ADMINS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ADMINS) using [`mail_admins()`](https://docs.djangoproject.com/en/5.0/topics/email/#django.core.mail.mail_admins "django.core.mail.mail_admins").
###  `shell`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#shell "Link to this heading")

django-admin shell[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-shell "Link to this definition")

Starts the Python interactive interpreter.

--interface {ipython,bpython,python}, -i {ipython,bpython,python}[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-shell-interface "Link to this definition")

Specifies the shell to use. By default, Django will use
IPython:
```
django-admin shell -i ipython

```

bpython:
```
django-admin shell -i bpython

```

If you have a “rich” shell installed but want to force use of the “plain” Python interpreter, use `python` as the interface name, like so:
```
django-admin shell -i python

```


--nostartup[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-shell-nostartup "Link to this definition")

Disables reading the startup script for the “plain” Python interpreter. By default, the script pointed to by the `~/.pythonrc.py` script is read.

--command COMMAND, -c COMMAND[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-shell-command "Link to this definition")

Lets you pass a command as a string to execute it as Django, like so:
```
django-admin shell --command="import django; print(django.__version__)"

```

You can also pass code in on standard input to execute it. For example:
```
$ django-admin shell <<EOF
> import django
> print(django.__version__)
> EOF

```

On Windows, the REPL is output due to implementation limits of
###  `showmigrations`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#showmigrations "Link to this heading")

django-admin showmigrations [app_label [app_label ...]][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-showmigrations "Link to this definition")

Shows all migrations in a project. You can choose from one of two formats:

--list, -l[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-showmigrations-list "Link to this definition")

Lists all of the apps Django knows about, the migrations available for each app, and whether or not each migration is applied (marked by an `[X]` next to the migration name). For a `--verbosity` of 2 and above, the applied datetimes are also shown.
Apps without migrations are also listed, but have `(no migrations)` printed under them.
This is the default output format.

--plan, -p[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-showmigrations-plan "Link to this definition")

Shows the migration plan Django will follow to apply migrations. Like `--list`, applied migrations are marked by an `[X]`. For a `--verbosity` of 2 and above, all dependencies of a migration will also be shown.
`app_label`s arguments limit the output, however, dependencies of provided apps may also be included.

--database DATABASE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-showmigrations-database "Link to this definition")

Specifies the database to examine. Defaults to `default`.
###  `sqlflush`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#sqlflush "Link to this heading")

django-admin sqlflush[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-sqlflush "Link to this definition")

Prints the SQL statements that would be executed for the [`flush`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-flush) command.

--database DATABASE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-sqlflush-database "Link to this definition")

Specifies the database for which to print the SQL. Defaults to `default`.
###  `sqlmigrate`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#sqlmigrate "Link to this heading")

django-admin sqlmigrate app_label migration_name[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-sqlmigrate "Link to this definition")

Prints the SQL for the named migration. This requires an active database connection, which it will use to resolve constraint names; this means you must generate the SQL against a copy of the database you wish to later apply it on.
Note that `sqlmigrate` doesn’t colorize its output.

--backwards[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-sqlmigrate-backwards "Link to this definition")

Generates the SQL for unapplying the migration. By default, the SQL created is for running the migration in the forwards direction.

--database DATABASE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-sqlmigrate-database "Link to this definition")

Specifies the database for which to generate the SQL. Defaults to `default`.
