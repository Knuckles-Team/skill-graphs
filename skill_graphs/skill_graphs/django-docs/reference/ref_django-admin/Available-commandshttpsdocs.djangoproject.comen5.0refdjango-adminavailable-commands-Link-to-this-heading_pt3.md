###  `sqlsequencereset`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#sqlsequencereset "Link to this heading")

django-admin sqlsequencereset app_label [app_label ...][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-sqlsequencereset "Link to this definition")

Prints the SQL statements for resetting sequences for the given app name(s).
Sequences are indexes used by some database engines to track the next available number for automatically incremented fields.
Use this command to generate SQL which will fix cases where a sequence is out of sync with its automatically incremented field data.

--database DATABASE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-sqlsequencereset-database "Link to this definition")

Specifies the database for which to print the SQL. Defaults to `default`.
###  `squashmigrations`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#squashmigrations "Link to this heading")

django-admin squashmigrations app_label [start_migration_name] migration_name[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-squashmigrations "Link to this definition")

Squashes the migrations for `app_label` up to and including `migration_name` down into fewer migrations, if possible. The resulting squashed migrations can live alongside the unsquashed ones safely. For more information, please read [Squashing migrations](https://docs.djangoproject.com/en/5.0/topics/migrations/#migration-squashing).
When `start_migration_name` is given, Django will only include migrations starting from and including this migration. This helps to mitigate the squashing limitation of [`RunPython`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RunPython "django.db.migrations.operations.RunPython") and [`django.db.migrations.operations.RunSQL`](https://docs.djangoproject.com/en/5.0/ref/migration-operations/#django.db.migrations.operations.RunSQL "django.db.migrations.operations.RunSQL") migration operations.

--no-optimize[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-squashmigrations-no-optimize "Link to this definition")

Disables the optimizer when generating a squashed migration. By default, Django will try to optimize the operations in your migrations to reduce the size of the resulting file. Use this option if this process is failing or creating incorrect migrations, though please also file a Django bug report about the behavior, as optimization is meant to be safe.

--noinput, --no-input[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-squashmigrations-noinput "Link to this definition")

Suppresses all user prompts.

--squashed-name SQUASHED_NAME[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-squashmigrations-squashed-name "Link to this definition")

Sets the name of the squashed migration. When omitted, the name is based on the first and last migration, with `_squashed_` in between.

--no-header[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-squashmigrations-no-header "Link to this definition")

Generate squashed migration file without Django version and timestamp header.
###  `startapp`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#startapp "Link to this heading")

django-admin startapp name [directory][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startapp "Link to this definition")

Creates a Django app directory structure for the given app name in the current directory or the given destination.
By default, `models.py` file and other app template files. If only the app name is given, the app directory will be created in the current working directory.
If the optional destination is provided, Django will use that existing directory rather than creating a new one. You can use ‘.’ to denote the current working directory.
For example:
```
django-admin startapp myapp /Users/jezdez/Code/myapp

```


--template TEMPLATE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-startapp-template "Link to this definition")

Provides the path to a directory with a custom app template file, or a path to an uncompressed archive (`.tar`) or a compressed archive (`.tar.gz`, `.tar.bz2`, `.tar.xz`, `.tar.lzma`, `.tgz`, `.tbz2`, `.txz`, `.tlz`, `.zip`) containing the app template files.
For example, this would look for an app template in the given directory when creating the `myapp` app:
```
django-admin startapp --template=/Users/jezdez/Code/my_app_template myapp

```

Django will also accept URLs (`http`, `https`, `ftp`) to compressed archives with the app template files, downloading and extracting them on the fly.
For example, taking advantage of GitHub’s feature to expose repositories as zip files, you can use a URL like:
```
django-admin startapp --template=https://github.com/githubuser/django-app-template/archive/main.zip myapp

```


--extension EXTENSIONS, -e EXTENSIONS[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-startapp-extension "Link to this definition")

Specifies which file extensions in the app template should be rendered with the template engine. Defaults to `py`.

--name FILES, -n FILES[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-startapp-name "Link to this definition")

Specifies which files in the app template (in addition to those matching `--extension`) should be rendered with the template engine. Defaults to an empty list.

--exclude DIRECTORIES, -x DIRECTORIES[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-startapp-exclude "Link to this definition")

Specifies which directories in the app template should be excluded, in addition to `.git` and `__pycache__`. If this option is not provided, directories named `__pycache__` or starting with `.` will be excluded.
The [`template context`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.Context "django.template.Context") used for all matching files is:
  * Any option passed to the `startapp` command (among the command’s supported options)
  * `app_name` – the app name as passed to the command
  * `app_directory` – the full path of the newly created app
  * `camel_case_app_name` – the app name in camel case format
  * `docs_version` – the version of the documentation: `'dev'` or `'1.x'`
  * `django_version` – the version of Django, e.g. `'2.0.3'`


Warning
When the app template files are rendered with the Django template engine (by default all `*.py` files), Django will also replace all stray template variables contained. For example, if one of the Python files contains a docstring explaining a particular feature related to template rendering, it might result in an incorrect example.
To work around this problem, you can use the [`templatetag`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-templatetag) template tag to “escape” the various parts of the template syntax.
In addition, to allow Python template files that contain Django template language syntax while also preventing packaging systems from trying to byte-compile invalid `*.py` files, template files ending with `.py-tpl` will be renamed to `.py`.
Warning
The contents of custom app (or project) templates should always be audited before use: Such templates define code that will become part of your project, and this means that such code will be trusted as much as any app you install, or code you write yourself. Further, even rendering the templates is, effectively, executing code that was provided as input to the management command. The Django template language may provide wide access into the system, so make sure any custom template you use is worthy of your trust.
###  `startproject`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#startproject "Link to this heading")

django-admin startproject name [directory][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startproject "Link to this definition")

Creates a Django project directory structure for the given project name in the current directory or the given destination.
By default, `manage.py` and a project package (containing a `settings.py` and other files).
If only the project name is given, both the project directory and project package will be named `<projectname>` and the project directory will be created in the current working directory.
If the optional destination is provided, Django will use that existing directory as the project directory, and create `manage.py` and the project package within it. Use ‘.’ to denote the current working directory.
For example:
```
django-admin startproject myproject /Users/jezdez/Code/myproject_repo

```


--template TEMPLATE[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-startproject-template "Link to this definition")

Specifies a directory, file path, or URL of a custom project template. See the [`startapp --template`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-startapp-template) documentation for examples and usage.

--extension EXTENSIONS, -e EXTENSIONS[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-startproject-extension "Link to this definition")

Specifies which file extensions in the project template should be rendered with the template engine. Defaults to `py`.

--name FILES, -n FILES[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-startproject-name "Link to this definition")

Specifies which files in the project template (in addition to those matching `--extension`) should be rendered with the template engine. Defaults to an empty list.

--exclude DIRECTORIES, -x DIRECTORIES[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-startproject-exclude "Link to this definition")

Specifies which directories in the project template should be excluded, in addition to `.git` and `__pycache__`. If this option is not provided, directories named `__pycache__` or starting with `.` will be excluded.
The [`template context`](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.Context "django.template.Context") used is:
  * Any option passed to the `startproject` command (among the command’s supported options)
  * `project_name` – the project name as passed to the command
  * `project_directory` – the full path of the newly created project
  * `secret_key` – a random key for the [`SECRET_KEY`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-SECRET_KEY) setting
  * `docs_version` – the version of the documentation: `'dev'` or `'1.x'`
  * `django_version` – the version of Django, e.g. `'2.0.3'`


Please also see the [rendering warning](https://docs.djangoproject.com/en/5.0/ref/django-admin/#render-warning) and [trusted code warning](https://docs.djangoproject.com/en/5.0/ref/django-admin/#trusted-code-warning) as mentioned for [`startapp`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startapp).
###  `test`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#test "Link to this heading")

django-admin test [test_label [test_label ...]][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-test "Link to this definition")

Runs tests for all installed apps. See [Testing in Django](https://docs.djangoproject.com/en/5.0/topics/testing/) for more information.

--failfast[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-failfast "Link to this definition")

Stops running tests and reports the failure immediately after a test fails.

--testrunner TESTRUNNER[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-testrunner "Link to this definition")

Controls the test runner class that is used to execute tests. This value overrides the value provided by the [`TEST_RUNNER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEST_RUNNER) setting.

--noinput, --no-input[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-noinput "Link to this definition")

Suppresses all user prompts. A typical prompt is a warning about deleting an existing test database.
#### Test runner options[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#test-runner-options "Link to this heading")
The `test` command receives options on behalf of the specified [`--testrunner`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-testrunner). These are the options of the default test runner: [`DiscoverRunner`](https://docs.djangoproject.com/en/5.0/topics/testing/advanced/#django.test.runner.DiscoverRunner "django.test.runner.DiscoverRunner").

--keepdb[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-keepdb "Link to this definition")

Preserves the test database between test runs. This has the advantage of skipping both the create and destroy actions which can greatly decrease the time to run tests, especially those in a large test suite. If the test database does not exist, it will be created on the first run and then preserved for each subsequent run. Unless the [`MIGRATE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEST_MIGRATE) test setting is `False`, any unapplied migrations will also be applied to the test database before running the test suite.

--shuffle [SEED][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-shuffle "Link to this definition")

Randomizes the order of tests before running them. This can help detect tests that aren’t properly isolated. The test order generated by this option is a deterministic function of the integer seed given. When no seed is passed, a seed is chosen randomly and printed to the console. To repeat a particular test order, pass a seed. The test orders generated by this option preserve Django’s [guarantees on test order](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#order-of-tests). They also keep tests grouped by test case class.
The shuffled orderings also have a special consistency property useful when narrowing down isolation issues. Namely, for a given seed and when running a subset of tests, the new order will be the original shuffling restricted to the smaller set. Similarly, when adding tests while keeping the seed the same, the order of the original tests will be the same in the new order.

--reverse, -r[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-reverse "Link to this definition")

Sorts test cases in the opposite execution order. This may help in debugging the side effects of tests that aren’t properly isolated. [Grouping by test class](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#order-of-tests) is preserved when using this option. This can be used in conjunction with `--shuffle` to reverse the order for a particular seed.

--debug-mode[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-debug-mode "Link to this definition")

Sets the [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) setting to `True` prior to running tests. This may help troubleshoot test failures.

--debug-sql, -d[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-debug-sql "Link to this definition")

Enables [SQL logging](https://docs.djangoproject.com/en/5.0/ref/logging/#django-db-logger) for failing tests. If `--verbosity` is `2`, then queries in passing tests are also output.

--parallel [N][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-parallel "Link to this definition")


DJANGO_TEST_PROCESSES[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#envvar-DJANGO_TEST_PROCESSES "Link to this definition")

Runs tests in separate parallel processes. Since modern processors have multiple cores, this allows running tests significantly faster.
Using `--parallel` without a value, or with the value `auto`, runs one test process per core according to `--parallel 4`, or by setting the [`DJANGO_TEST_PROCESSES`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#envvar-DJANGO_TEST_PROCESSES) environment variable.
Django distributes test cases —
Each process gets its own database. You must ensure that different test case classes don’t access the same resources. For instance, test case classes that touch the filesystem should create a temporary directory for their own use.
Note
If you have test classes that cannot be run in parallel, you can use `SerializeMixin` to run them sequentially. See [Enforce running test classes sequentially](https://docs.djangoproject.com/en/5.0/topics/testing/advanced/#topics-testing-enforce-run-sequentially).
This option requires the third-party `tblib` package to display tracebacks correctly:
```
$ python -m pip install tblib

```

This feature isn’t available on Windows. It doesn’t work with the Oracle database backend either.
If you want to use `--parallel=1`). You’ll see something like `bdb.BdbQuit` if you don’t.
Warning
When test parallelization is enabled and a test fails, Django may be unable to display the exception traceback. This can make debugging difficult. If you encounter this problem, run the affected test without parallelization to see the traceback of the failure.
This is a known limitation. It arises from the need to serialize objects in order to exchange them between processes. See

--tag TAGS[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-tag "Link to this definition")

Runs only tests [marked with the specified tags](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#topics-tagging-tests). May be specified multiple times and combined with [`test --exclude-tag`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-exclude-tag).
Tests that fail to load are always considered matching.

--exclude-tag EXCLUDE_TAGS[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-exclude-tag "Link to this definition")

Excludes tests [marked with the specified tags](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#topics-tagging-tests). May be specified multiple times and combined with [`test --tag`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-tag).

-k TEST_NAME_PATTERNS[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-k "Link to this definition")

Runs test methods and classes matching test name patterns, in the same way as

--pdb[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-pdb "Link to this definition")

Spawns a `pdb` debugger at each test error or failure. If you have it installed, `ipdb` is used instead.

--buffer, -b[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-buffer "Link to this definition")

Discards output (`stdout` and `stderr`) for passing tests, in the same way as

--no-faulthandler[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-no-faulthandler "Link to this definition")

Django automatically calls `--no-faulthandler` to disable this behavior.

--timing[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-timing "Link to this definition")

Outputs timings, including database setup and total run time.

--durations N[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-durations "Link to this definition")

New in Django 5.0.
Shows the N slowest test cases (N=0 for all).
Python 3.12 and later
This feature is only available for Python 3.12 and later.
###  `testserver`[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#testserver "Link to this heading")

django-admin testserver [fixture [fixture ...]][¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-testserver "Link to this definition")

Runs a Django development server (as in [`runserver`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-runserver)) using data from the given fixture(s).
For example, this command:
```
django-admin testserver mydata.json

```

…would perform the following steps:
  1. Create a test database, as described in [The test database](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#the-test-database).
  2. Populate the test database with fixture data from the given fixtures. (For more on fixtures, see the documentation for [`loaddata`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-loaddata) above.)
  3. Runs the Django development server (as in [`runserver`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-runserver)), pointed at this newly created test database instead of your production database.


This is useful in a number of ways:
  * When you’re writing [unit tests](https://docs.djangoproject.com/en/5.0/topics/testing/overview/) of how your views act with certain fixture data, you can use `testserver` to interact with the views in a web browser, manually.
  * Let’s say you’re developing your Django application and have a “pristine” copy of a database that you’d like to interact with. You can dump your database to a [fixture](https://docs.djangoproject.com/en/5.0/topics/db/fixtures/#fixtures-explanation) (using the [`dumpdata`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-dumpdata) command, explained above), then use `testserver` to run your web application with that data. With this arrangement, you have the flexibility of messing up your data in any way, knowing that whatever data changes you’re making are only being made to a test database.


Note that this server does _not_ automatically detect changes to your Python source code (as [`runserver`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-runserver) does). It does, however, detect changes to templates.

--addrport ADDRPORT[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-testserver-addrport "Link to this definition")

Specifies a different port, or IP address and port, from the default of `127.0.0.1:8000`. This value follows exactly the same format and serves exactly the same function as the argument to the [`runserver`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-runserver) command.
Examples:
To run the test server on port 7000 with `fixture1` and `fixture2`:
```
django-admin testserver --addrport 7000 fixture1 fixture2
django-admin testserver fixture1 fixture2 --addrport 7000

```

(The above statements are equivalent. We include both of them to demonstrate that it doesn’t matter whether the options come before or after the fixture arguments.)
To run on 1.2.3.4:7000 with a `test` fixture:
```
django-admin testserver --addrport 1.2.3.4:7000 test

```


--noinput, --no-input[¶](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-testserver-noinput "Link to this definition")

Suppresses all user prompts. A typical prompt is a warning about deleting an existing test database.
