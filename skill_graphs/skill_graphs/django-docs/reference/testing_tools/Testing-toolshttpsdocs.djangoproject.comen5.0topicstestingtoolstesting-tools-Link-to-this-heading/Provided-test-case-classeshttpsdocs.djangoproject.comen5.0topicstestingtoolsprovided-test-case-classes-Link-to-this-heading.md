## Provided test case classes[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#provided-test-case-classes "Link to this heading")
Normal Python unit test classes extend a base class of
[![Hierarchy of Django unit testing classes \(TestCase subclasses\)](https://docs.djangoproject.com/en/5.0/_images/django_unittest_classes_hierarchy.svg) ](https://docs.djangoproject.com/en/5.0/_images/django_unittest_classes_hierarchy.svg)
Hierarchy of Django unit testing classes[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#id4 "Link to this image")
You can convert a normal `unittest.TestCase` to the subclass. All of the standard Python unit test functionality will be available, and it will be augmented with some useful additions as described in each section below.
###  `SimpleTestCase`[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#simpletestcase "Link to this heading")

_class_ SimpleTestCase[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase "Link to this definition")

A subclass of
  * Some useful assertions like:
    * Checking that a callable [`raises a certain exception`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertRaisesMessage "django.test.SimpleTestCase.assertRaisesMessage").
    * Checking that a callable [`triggers a certain warning`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertWarnsMessage "django.test.SimpleTestCase.assertWarnsMessage").
    * Testing form field [`rendering and error treatment`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertFieldOutput "django.test.SimpleTestCase.assertFieldOutput").
    * Testing [`HTML responses for the presence/lack of a given fragment`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertContains "django.test.SimpleTestCase.assertContains").
    * Verifying that a template [`has/hasn't been used to generate a given response content`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertTemplateUsed "django.test.SimpleTestCase.assertTemplateUsed").
    * Verifying that two [`URLs`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertURLEqual "django.test.SimpleTestCase.assertURLEqual") are equal.
    * Verifying an HTTP [`redirect`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertRedirects "django.test.SimpleTestCase.assertRedirects") is performed by the app.
    * Robustly testing two [`HTML fragments`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual") for equality/inequality or [`containment`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertInHTML "django.test.SimpleTestCase.assertInHTML").
    * Robustly testing two [`XML fragments`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertXMLEqual "django.test.SimpleTestCase.assertXMLEqual") for equality/inequality.
    * Robustly testing two [`JSON fragments`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertJSONEqual "django.test.SimpleTestCase.assertJSONEqual") for equality.
  * The ability to run tests with [modified settings](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#overriding-settings).
  * Using the [`client`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.client "django.test.SimpleTestCase.client") [`Client`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client "django.test.Client").


If your tests make any database queries, use subclasses [`TransactionTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase") or [`TestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase").

SimpleTestCase.databases[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.databases "Link to this definition")

[`SimpleTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase "django.test.SimpleTestCase") disallows database queries by default. This helps to avoid executing write queries which will affect other tests since each `SimpleTestCase` test isn’t run in a transaction. If you aren’t concerned about this problem, you can disable this behavior by setting the `databases` class attribute to `'__all__'` on your test class.
Warning
`SimpleTestCase` and its subclasses (e.g. `TestCase`, …) rely on `setUpClass()` and `tearDownClass()` to perform some class-wide initialization (e.g. overriding settings). If you need to override those methods, don’t forget to call the `super` implementation:
```
class MyTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        ...

    @classmethod
    def tearDownClass(cls):
        ...
        super().tearDownClass()

```

Be sure to account for Python’s behavior if an exception is raised during `setUpClass()`. If that happens, neither the tests in the class nor `tearDownClass()` are run. In the case of [`django.test.TestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase"), this will leak the transaction created in `super()` which results in various symptoms including a segmentation fault on some platforms (reported on macOS). If you want to intentionally raise an exception such as `setUpClass()`, be sure to do it before calling `super()` to avoid this.
###  `TransactionTestCase`[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#transactiontestcase "Link to this heading")

_class_ TransactionTestCase[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#TransactionTestCase)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase "Link to this definition")

`TransactionTestCase` inherits from [`SimpleTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase "django.test.SimpleTestCase") to add some database-specific features:
  * Resetting the database to a known state at the beginning of each test to ease testing and using the ORM.
  * Database [`fixtures`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase.fixtures "django.test.TransactionTestCase.fixtures").
  * Test [skipping based on database backend features](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#skipping-tests).
  * The remaining specialized [`assert*`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase.assertQuerySetEqual "django.test.TransactionTestCase.assertQuerySetEqual") methods.


Django’s [`TestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase") class is a more commonly used subclass of `TransactionTestCase` that makes use of database transaction facilities to speed up the process of resetting the database to a known state at the beginning of each test. A consequence of this, however, is that some database behaviors cannot be tested within a Django `TestCase` class. For instance, you cannot test that a block of code is executing within a transaction, as is required when using [`select_for_update()`](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#django.db.models.query.QuerySet.select_for_update "django.db.models.query.QuerySet.select_for_update"). In those cases, you should use `TransactionTestCase`.
`TransactionTestCase` and `TestCase` are identical except for the manner in which the database is reset to a known state and the ability for test code to test the effects of commit and rollback:
  * A `TransactionTestCase` resets the database after the test runs by truncating all tables. A `TransactionTestCase` may call commit and rollback and observe the effects of these calls on the database.
  * A `TestCase`, on the other hand, does not truncate tables after a test. Instead, it encloses the test code in a database transaction that is rolled back at the end of the test. This guarantees that the rollback at the end of the test restores the database to its initial state.


Warning
`TestCase` running on a database that does not support rollback (e.g. MySQL with the MyISAM storage engine), and all instances of `TransactionTestCase`, will roll back at the end of the test by deleting all data from the test database.
Apps [will not see their data reloaded](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#test-case-serialized-rollback); if you need this functionality (for example, third-party apps should enable this) you can set `serialized_rollback = True` inside the `TestCase` body.
###  `TestCase`[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#testcase "Link to this heading")

_class_ TestCase[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#TestCase)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase "Link to this definition")

This is the most common class to use for writing tests in Django. It inherits from [`TransactionTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase") (and by extension [`SimpleTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase "django.test.SimpleTestCase")). If your Django application doesn’t use a database, use [`SimpleTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase "django.test.SimpleTestCase").
The class:
  * Wraps the tests within two nested [`atomic()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.atomic "django.db.transaction.atomic") blocks: one for the whole class and one for each test. Therefore, if you want to test some specific database transaction behavior, use [`TransactionTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase").
  * Checks deferrable database constraints at the end of each test.


It also provides an additional method:

_classmethod_ TestCase.setUpTestData()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#TestCase.setUpTestData)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase.setUpTestData "Link to this definition")

The class-level `atomic` block described above allows the creation of initial data at the class level, once for the whole `TestCase`. This technique allows for faster tests as compared to using `setUp()`.
For example:
```
from django.test import TestCase


class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.foo = Foo.objects.create(bar="Test")
        ...

    def test1(self):
        # Some test using self.foo
        ...

    def test2(self):
        # Some other test using self.foo
        ...

```

Note that if the tests are run on a database with no transaction support (for instance, MySQL with the MyISAM engine), `setUpTestData()` will be called before each test, negating the speed benefits.
Objects assigned to class attributes in `setUpTestData()` must support creating deep copies with

_classmethod_ TestCase.captureOnCommitCallbacks(_using =DEFAULT_DB_ALIAS_, _execute =False_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#TestCase.captureOnCommitCallbacks)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase.captureOnCommitCallbacks "Link to this definition")

Returns a context manager that captures [`transaction.on_commit()`](https://docs.djangoproject.com/en/5.0/topics/db/transactions/#django.db.transaction.on_commit "django.db.transaction.on_commit") callbacks for the given database connection. It returns a list that contains, on exit of the context, the captured callback functions. From this list you can make assertions on the callbacks or call them to invoke their side effects, emulating a commit.
`using` is the alias of the database connection to capture callbacks for.
If `execute` is `True`, all the callbacks will be called as the context manager exits, if no exception occurred. This emulates a commit after the wrapped block of code.
For example:
```
from django.core import mail
from django.test import TestCase


class ContactTests(TestCase):
    def test_post(self):
        with self.captureOnCommitCallbacks(execute=True) as callbacks:
            response = self.client.post(
                "/contact/",
                {"message": "I like your site"},
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(callbacks), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Contact Form")
        self.assertEqual(mail.outbox[0].body, "I like your site")

```

###  `LiveServerTestCase`[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#liveservertestcase "Link to this heading")

_class_ LiveServerTestCase[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#LiveServerTestCase)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.LiveServerTestCase "Link to this definition")

`LiveServerTestCase` does basically the same as [`TransactionTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase "django.test.TransactionTestCase") with one extra feature: it launches a live Django server in the background on setup, and shuts it down on teardown. This allows the use of automated test clients other than the [Django dummy client](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#test-client) such as, for example, the
The live server listens on `localhost` and binds to port 0 which uses a free port assigned by the operating system. The server’s URL can be accessed with `self.live_server_url` during the tests.
To demonstrate how to use `LiveServerTestCase`, let’s write a Selenium test. First of all, you need to install the
/ 
```
$ python -m pip install "selenium >= 4.8.0"

```

```
...\> py -m pip install "selenium >= 4.8.0"

```

Then, add a `LiveServerTestCase`-based test to your app’s tests module (for example: `myapp/tests.py`). For this example, we’ll assume you’re using the [`staticfiles`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#module-django.contrib.staticfiles "django.contrib.staticfiles: An app for handling static files.") app and want to have static files served during the execution of your tests similar to what we get at development time with `DEBUG=True`, i.e. without having to collect them using [`collectstatic`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django-admin-collectstatic). We’ll use the [`StaticLiveServerTestCase`](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#django.contrib.staticfiles.testing.StaticLiveServerTestCase "django.contrib.staticfiles.testing.StaticLiveServerTestCase") subclass which provides that functionality. Replace it with `django.test.LiveServerTestCase` if you don’t need that.
The code for this test may look as follows:
```
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ["user-data.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get(f"{self.live_server_url}/login/")
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("myuser")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("secret")
        self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()

```

Finally, you may run the test as follows:
/ 
```
$ ./manage.py test myapp.tests.MySeleniumTests.test_login

```

```
...\> manage.py test myapp.tests.MySeleniumTests.test_login

```

This example will automatically open Firefox then go to the login page, enter the credentials and press the “Log in” button. Selenium offers other drivers in case you do not have Firefox installed or wish to use another browser. The example above is just a tiny fraction of what the Selenium client can do; check out the
Note
When using an in-memory SQLite database to run the tests, the same database connection will be shared by two threads in parallel: the thread in which the live server is run and the thread in which the test case is run. It’s important to prevent simultaneous database queries via this shared connection by the two threads, as that may sometimes randomly cause the tests to fail. So you need to ensure that the two threads don’t access the database at the same time. In particular, this means that in some cases (for example, just after clicking a link or submitting a form), you might need to check that a response is received by Selenium and that the next page is loaded before proceeding with further test execution. Do this, for example, by making Selenium wait until the `<body>` HTML tag is found in the response (requires Selenium > 2.13):
```
def test_login(self):
    from selenium.webdriver.support.wait import WebDriverWait

    timeout = 2
    ...
    self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()
    # Wait until the response is received
    WebDriverWait(self.selenium, timeout).until(
        lambda driver: driver.find_element(By.TAG_NAME, "body")
    )

```

The tricky thing here is that there’s really no such thing as a “page load,” especially in modern web apps that generate HTML dynamically after the server generates the initial document. So, checking for the presence of `<body>` in the response might not necessarily be appropriate for all use cases. Please refer to the
