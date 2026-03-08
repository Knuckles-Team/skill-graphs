This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#main-content)
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
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/testing/overview/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/testing/overview/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/testing/overview/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/testing/overview/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/testing/overview/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/testing/overview/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/testing/overview/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/testing/overview/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/testing/overview/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/testing/overview/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/testing/overview/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/testing/overview/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/testing/overview/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/testing/overview/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/testing/overview/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/testing/overview/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/testing/overview/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/testing/overview/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/testing/overview/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/testing/overview/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/testing/overview/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/testing/overview/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/testing/overview/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/testing/overview/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/testing/overview/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/testing/overview/)


  * [](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#top)


# Writing and running tests[¶](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#module-django.test "Link to this heading")
See also
The [testing tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial05/), the [testing tools reference](https://docs.djangoproject.com/en/5.0/topics/testing/tools/), and the [advanced testing topics](https://docs.djangoproject.com/en/5.0/topics/testing/advanced/).
This document is split into two primary sections. First, we explain how to write tests with Django. Then, we explain how to run them.
## Writing tests[¶](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#writing-tests "Link to this heading")
Django’s unit tests use a Python standard library module:
Here is an example which subclasses from [`django.test.TestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase"), which is a subclass of
```
from django.test import TestCase
from myapp.models import Animal


class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')

```

When you [run your tests](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#running-tests), the default behavior of the test utility is to find all the test case classes (that is, subclasses of `test`, automatically build a test suite out of those test case classes, and run that suite.
For more details about
Where should the tests live?
The default [`startapp`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startapp) template creates a `tests.py` file in the new application. This might be fine if you only have a few tests, but as your test suite grows you’ll likely want to restructure it into a tests package so you can split your tests into different submodules such as `test_models.py`, `test_views.py`, `test_forms.py`, etc. Feel free to pick whatever organizational scheme you like.
See also [Using the Django test runner to test reusable applications](https://docs.djangoproject.com/en/5.0/topics/testing/advanced/#testing-reusable-applications).
Warning
If your tests rely on database access such as creating or querying models, be sure to create your test classes as subclasses of [`django.test.TestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase") rather than
Using
## Running tests[¶](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#running-tests "Link to this heading")
Once you’ve written tests, run them using the [`test`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-test) command of your project’s `manage.py` utility:
```
$ ./manage.py test

```

Test discovery is based on the unittest module’s `test*.py` under the current working directory.
You can specify particular tests to run by supplying any number of “test labels” to `./manage.py test`. Each test label can be a full Python dotted path to a package, module, `TestCase` subclass, or test method. For instance:
```
# Run all the tests in the animals.tests module
$ ./manage.py test animals.tests

# Run all the tests found within the 'animals' package
$ ./manage.py test animals

# Run just one test case class
$ ./manage.py test animals.tests.AnimalTestCase

# Run just one test method
$ ./manage.py test animals.tests.AnimalTestCase.test_animals_can_speak

```

You can also provide a path to a directory to discover tests below that directory:
```
$ ./manage.py test animals/

```

You can specify a custom filename pattern match using the `-p` (or `--pattern`) option, if your test files are named differently from the `test*.py` pattern:
```
$ ./manage.py test --pattern="tests_*.py"

```

If you press `Ctrl-C` while the tests are running, the test runner will wait for the currently running test to complete and then exit gracefully. During a graceful exit the test runner will output details of any test failures, report on how many tests were run and how many errors and failures were encountered, and destroy any test databases as usual. Thus pressing `Ctrl-C` can be very useful if you forget to pass the [`--failfast`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-failfast) option, notice that some tests are unexpectedly failing and want to get details on the failures without waiting for the full test run to complete.
If you do not want to wait for the currently running test to finish, you can press `Ctrl-C` a second time and the test run will halt immediately, but not gracefully. No details of the tests run before the interruption will be reported, and any test databases created by the run will not be destroyed.
Test with warnings enabled
It’s a good idea to run your tests with Python warnings enabled: `python -Wa manage.py test`. The `-Wa` flag tells Python to display deprecation warnings. Django, like many other Python libraries, uses these warnings to flag when features are going away. It also might flag areas in your code that aren’t strictly wrong but could benefit from a better implementation.
### The test database[¶](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#the-test-database "Link to this heading")
Tests that require a database (namely, model tests) will not use your “real” (production) database. Separate, blank databases are created for the tests.
Regardless of whether the tests pass or fail, the test databases are destroyed when all the tests have been executed.
You can prevent the test databases from being destroyed by using the [`test --keepdb`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-keepdb) option. This will preserve the test database between runs. If the database does not exist, it will first be created. Any migrations will also be applied in order to keep it up to date.
As described in the previous section, if a test run is forcefully interrupted, the test database may not be destroyed. On the next run, you’ll be asked whether you want to reuse or destroy the database. Use the [`test --noinput`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-noinput) option to suppress that prompt and automatically destroy the database. This can be useful when running tests on a continuous integration server where tests may be interrupted by a timeout, for example.
The default test database names are created by prepending `test_` to the value of each [`NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-NAME) in [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES). When using SQLite, the tests will use an in-memory database by default (i.e., the database will be created in memory, bypassing the filesystem entirely!). The [`TEST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASE-TEST) dictionary in [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES) offers a number of settings to configure your test database. For example, if you want to use a different database name, specify [`NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEST_NAME) in the [`TEST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASE-TEST) dictionary for any given database in [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES).
On PostgreSQL, [`USER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USER) will also need read access to the built-in `postgres` database.
Aside from using a separate database, the test runner will otherwise use all of the same database settings you have in your settings file: [`ENGINE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASE-ENGINE), [`USER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USER), [`HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-HOST), etc. The test database is created by the user specified by [`USER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USER), so you’ll need to make sure that the given user account has sufficient privileges to create a new database on the system.
For fine-grained control over the character encoding of your test database, use the [`CHARSET`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEST_CHARSET) TEST option. If you’re using MySQL, you can also use the [`COLLATION`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEST_COLLATION) option to control the particular collation used by the test database. See the [settings documentation](https://docs.djangoproject.com/en/5.0/ref/settings/) for details of these and other advanced settings.
If using an SQLite in-memory database with SQLite,
Finding data from your production database when running tests?
If your code attempts to access the database when its modules are compiled, this will occur _before_ the test database is set up, with potentially unexpected results. For example, if you have a database query in module-level code and a real database exists, production data could pollute your tests. _It is a bad idea to have such import-time database queries in your code_ anyway - rewrite your code so that it doesn’t do this.
This also applies to customized implementations of [`ready()`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.AppConfig.ready "django.apps.AppConfig.ready").
See also
The [advanced multi-db testing topics](https://docs.djangoproject.com/en/5.0/topics/testing/advanced/#topics-testing-advanced-multidb).
### Order in which tests are executed[¶](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#order-in-which-tests-are-executed "Link to this heading")
In order to guarantee that all `TestCase` code starts with a clean database, the Django test runner reorders tests in the following way:
  * All [`TestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase") subclasses are run first.
  * Then, all other Django-based tests (test case classes based on [`SimpleTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase "django.test.SimpleTestCase"), including [`TransactionTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase")) are run with no particular ordering guaranteed nor enforced among them.
  * Then any other


Note
The new ordering of tests may reveal unexpected dependencies on test case ordering. This is the case with doctests that relied on state left in the database by a given [`TransactionTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase") test, they must be updated to be able to run independently.
Note
Failures detected when loading tests are ordered before all of the above for quicker feedback. This includes things like test modules that couldn’t be found or that couldn’t be loaded due to syntax errors.
You may randomize and/or reverse the execution order inside groups using the [`test --shuffle`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-shuffle) and [`--reverse`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-reverse) options. This can help with ensuring your tests are independent from each other.
### Rollback emulation[¶](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#rollback-emulation "Link to this heading")
Any initial data loaded in migrations will only be available in `TestCase` tests and not in `TransactionTestCase` tests, and additionally only on backends where transactions are supported (the most important exception being MyISAM). This is also true for tests which rely on `TransactionTestCase` such as [`LiveServerTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.LiveServerTestCase "django.test.LiveServerTestCase") and [`StaticLiveServerTestCase`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django.contrib.staticfiles.testing.StaticLiveServerTestCase "django.contrib.staticfiles.testing.StaticLiveServerTestCase").
Django can reload that data for you on a per-testcase basis by setting the `serialized_rollback` option to `True` in the body of the `TestCase` or `TransactionTestCase`, but note that this will slow down that test suite by approximately 3x.
Third-party apps or those developing against MyISAM will need to set this; in general, however, you should be developing your own projects against a transactional database and be using `TestCase` for most tests, and thus not need this setting.
The initial serialization is usually very quick, but if you wish to exclude some apps from this process (and speed up test runs slightly), you may add those apps to [`TEST_NON_SERIALIZED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEST_NON_SERIALIZED_APPS).
To prevent serialized data from being loaded twice, setting `serialized_rollback=True` disables the [`post_migrate`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.db.models.signals.post_migrate "django.db.models.signals.post_migrate") signal when flushing the test database.
### Other test conditions[¶](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#other-test-conditions "Link to this heading")
Regardless of the value of the [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) setting in your configuration file, all Django tests run with [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG)=False. This is to ensure that the observed output of your code matches what will be seen in a production setting.
Caches are not cleared after each test, and running `manage.py test fooapp` can insert data from the tests into the cache of a live system if you run your tests in production because, unlike databases, a separate “test cache” is not used. This behavior [may change](https://code.djangoproject.com/ticket/11505) in the future.
### Understanding the test output[¶](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#understanding-the-test-output "Link to this heading")
When you run your tests, you’ll see a number of messages as the test runner prepares itself. You can control the level of detail of these messages with the `verbosity` option on the command line:
```
Creating test database...
Creating table myapp_animal
Creating table myapp_mineral

```

This tells you that the test runner is creating a test database, as described in the previous section.
Once the test database has been created, Django will run your tests. If everything goes well, you’ll see something like this:
```
----------------------------------------------------------------------
Ran 22 tests in 0.221s

OK

```

If there are test failures, however, you’ll see full details about which tests failed:
```
======================================================================
FAIL: test_was_published_recently_with_future_poll (polls.tests.PollMethodTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/dev/mysite/polls/tests.py", line 16, in test_was_published_recently_with_future_poll
    self.assertIs(future_poll.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.003s

FAILED (failures=1)

```

A full explanation of this error output is beyond the scope of this document, but it’s pretty intuitive. You can consult the documentation of Python’s
Note that the return code for the test-runner script is 1 for any number of failed tests (whether the failure was caused by an error, a failed assertion, or an unexpected success). If all the tests pass, the return code is 0. This feature is useful if you’re using the test-runner script in a shell script and need to test for success or failure at that level.
### Speeding up the tests[¶](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#speeding-up-the-tests "Link to this heading")
#### Running tests in parallel[¶](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#running-tests-in-parallel "Link to this heading")
As long as your tests are properly isolated, you can run them in parallel to gain a speed up on multi-core hardware. See [`test --parallel`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-parallel).
#### Password hashing[¶](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#password-hashing "Link to this heading")
The default password hasher is rather slow by design. If you’re authenticating many users in your tests, you may want to use a custom settings file and set the [`PASSWORD_HASHERS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-PASSWORD_HASHERS) setting to a faster hashing algorithm:
```
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

```

Don’t forget to also include in [`PASSWORD_HASHERS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-PASSWORD_HASHERS) any hashing algorithm used in fixtures, if any.
#### Preserving the test database[¶](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#preserving-the-test-database "Link to this heading")
The [`test --keepdb`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-keepdb) option preserves the test database between test runs. It skips the create and destroy actions which can greatly decrease the time to run tests.
#### Avoiding disk access for media files[¶](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#avoiding-disk-access-for-media-files "Link to this heading")
New in Django 4.2.
The [`InMemoryStorage`](https://docs.djangoproject.com/en/5.0/ref/files/storage/#django.core.files.storage.InMemoryStorage "django.core.files.storage.InMemoryStorage") is a convenient way to prevent disk access for media files. All data is kept in memory, then it gets discarded after tests run.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/testing/)
[Testing tools ](https://docs.djangoproject.com/en/5.0/topics/testing/tools/)
[](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Pierre Vanhulst donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Writing and running tests](https://docs.djangoproject.com/en/5.0/topics/testing/overview/)
    * [Writing tests](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#writing-tests)
    * [Running tests](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#running-tests)
      * [The test database](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#the-test-database)
      * [Order in which tests are executed](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#order-in-which-tests-are-executed)
      * [Rollback emulation](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#rollback-emulation)
      * [Other test conditions](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#other-test-conditions)
      * [Understanding the test output](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#understanding-the-test-output)
      * [Speeding up the tests](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#speeding-up-the-tests)
        * [Running tests in parallel](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#running-tests-in-parallel)
        * [Password hashing](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#password-hashing)
        * [Preserving the test database](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#preserving-the-test-database)
        * [Avoiding disk access for media files](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#avoiding-disk-access-for-media-files)


### Browse
  * Prev: [Testing in Django](https://docs.djangoproject.com/en/5.0/topics/testing/)
  * Next: [Testing tools](https://docs.djangoproject.com/en/5.0/topics/testing/tools/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * [Testing in Django](https://docs.djangoproject.com/en/5.0/topics/testing/)
        * Writing and running tests


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
