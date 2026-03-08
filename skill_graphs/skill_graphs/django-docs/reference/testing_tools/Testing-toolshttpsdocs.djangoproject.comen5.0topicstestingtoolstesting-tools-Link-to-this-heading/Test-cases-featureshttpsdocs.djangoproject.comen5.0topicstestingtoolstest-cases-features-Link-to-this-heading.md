## Test cases features[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#test-cases-features "Link to this heading")
### Default test client[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#default-test-client "Link to this heading")

SimpleTestCase.client[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.client "Link to this definition")

Every test case in a `django.test.*TestCase` instance has access to an instance of a Django test client. This client can be accessed as `self.client`. This client is recreated for each test, so you don’t have to worry about state (such as cookies) carrying over from one test to another.
This means, instead of instantiating a `Client` in each test:
```
import unittest
from django.test import Client


class SimpleTest(unittest.TestCase):
    def test_details(self):
        client = Client()
        response = client.get("/customer/details/")
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        client = Client()
        response = client.get("/customer/index/")
        self.assertEqual(response.status_code, 200)

```

…you can refer to `self.client`, like so:
```
from django.test import TestCase


class SimpleTest(TestCase):
    def test_details(self):
        response = self.client.get("/customer/details/")
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get("/customer/index/")
        self.assertEqual(response.status_code, 200)

```

### Customizing the test client[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#customizing-the-test-client "Link to this heading")

SimpleTestCase.client_class[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.client_class "Link to this definition")

If you want to use a different `Client` class (for example, a subclass with customized behavior), use the [`client_class`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.client_class "django.test.SimpleTestCase.client_class") class attribute:
```
from django.test import Client, TestCase


class MyTestClient(Client):
    # Specialized methods for your environment
    ...


class MyTest(TestCase):
    client_class = MyTestClient

    def test_my_stuff(self):
        # Here self.client is an instance of MyTestClient...
        call_some_test_code()

```

### Fixture loading[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#fixture-loading "Link to this heading")

TransactionTestCase.fixtures[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase.fixtures "Link to this definition")

A test case class for a database-backed website isn’t much use if there isn’t any data in the database. Tests are more readable and it’s more maintainable to create objects using the ORM, for example in [`TestCase.setUpTestData()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase.setUpTestData "django.test.TestCase.setUpTestData"), however, you can also use [fixtures](https://docs.djangoproject.com/en/5.0/topics/db/fixtures/#fixtures-explanation).
A fixture is a collection of data that Django knows how to import into a database. For example, if your site has user accounts, you might set up a fixture of fake user accounts in order to populate your database during tests.
The most straightforward way of creating a fixture is to use the [`manage.py dumpdata`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-dumpdata) command. This assumes you already have some data in your database. See the [`dumpdata documentation`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-dumpdata) for more details.
Once you’ve created a fixture and placed it in a `fixtures` directory in one of your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS), you can use it in your unit tests by specifying a `fixtures` class attribute on your [`django.test.TestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase") subclass:
```
from django.test import TestCase
from myapp.models import Animal


class AnimalTestCase(TestCase):
    fixtures = ["mammals.json", "birds"]

    def setUp(self):
        # Test definitions as before.
        call_setup_methods()

    def test_fluffy_animals(self):
        # A test that uses the fixtures.
        call_some_test_code()

```

Here’s specifically what will happen:
  * At the start of each test, before `setUp()` is run, Django will flush the database, returning the database to the state it was in directly after [`migrate`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-migrate) was called.
  * Then, all the named fixtures are installed. In this example, Django will install any JSON fixture named `mammals`, followed by any fixture named `birds`. See the [Fixtures](https://docs.djangoproject.com/en/5.0/topics/db/fixtures/#fixtures-explanation) topic for more details on defining and installing fixtures.


For performance reasons, [`TestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase") loads fixtures once for the entire test class, before [`setUpTestData()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase.setUpTestData "django.test.TestCase.setUpTestData"), instead of before each test, and it uses transactions to clean the database before each test. In any case, you can be certain that the outcome of a test will not be affected by another test or by the order of test execution.
By default, fixtures are only loaded into the `default` database. If you are using multiple databases and set [`TransactionTestCase.databases`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase.databases "django.test.TransactionTestCase.databases"), fixtures will be loaded into all specified databases.
### URLconf configuration[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#urlconf-configuration "Link to this heading")
If your application provides views, you may want to include tests that use the test client to exercise those views. However, an end user is free to deploy the views in your application at any URL of their choosing. This means that your tests can’t rely upon the fact that your views will be available at a particular URL. Decorate your test class or test method with `@override_settings(ROOT_URLCONF=...)` for URLconf configuration.
### Multi-database support[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#multi-database-support "Link to this heading")

TransactionTestCase.databases[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase.databases "Link to this definition")

Django sets up a test database corresponding to every database that is defined in the [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES) definition in your settings and referred to by at least one test through `databases`.
However, a big part of the time taken to run a Django `TestCase` is consumed by the call to `flush` that ensures that you have a clean database at the start of each test run. If you have multiple databases, multiple flushes are required (one for each database), which can be a time consuming activity – especially if your tests don’t need to test multi-database activity.
As an optimization, Django only flushes the `default` database at the start of each test run. If your setup contains multiple databases, and you have a test that requires every database to be clean, you can use the `databases` attribute on the test suite to request extra databases to be flushed.
For example:
```
class TestMyViews(TransactionTestCase):
    databases = {"default", "other"}

    def test_index_page_view(self):
        call_some_test_code()

```

This test case class will flush the `default` and `other` test databases before running `test_index_page_view`. You can also use `'__all__'` to specify that all of the test databases must be flushed.
The `databases` flag also controls which databases the [`TransactionTestCase.fixtures`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase.fixtures "django.test.TransactionTestCase.fixtures") are loaded into. By default, fixtures are only loaded into the `default` database.
Queries against databases not in `databases` will give assertion errors to prevent state leaking between tests.

TestCase.databases[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase.databases "Link to this definition")

By default, only the `default` database will be wrapped in a transaction during a `TestCase`’s execution and attempts to query other databases will result in assertion errors to prevent state leaking between tests.
Use the `databases` class attribute on the test class to request transaction wrapping against non-`default` databases.
For example:
```
class OtherDBTests(TestCase):
    databases = {"other"}

    def test_other_db_query(self): ...

```

This test will only allow queries against the `other` database. Just like for [`SimpleTestCase.databases`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.databases "django.test.SimpleTestCase.databases") and [`TransactionTestCase.databases`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase.databases "django.test.TransactionTestCase.databases"), the `'__all__'` constant can be used to specify that the test should allow queries to all databases.
### Overriding settings[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#overriding-settings "Link to this heading")
Warning
Use the functions below to temporarily alter the value of settings in tests. Don’t manipulate `django.conf.settings` directly as Django won’t restore the original values after such manipulations.

SimpleTestCase.settings()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.settings)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.settings "Link to this definition")

For testing purposes it’s often useful to change a setting temporarily and revert to the original value after running the testing code. For this use case Django provides a standard Python context manager (see [`settings()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.settings "django.test.SimpleTestCase.settings"), which can be used like this:
```
from django.test import TestCase


class LoginTestCase(TestCase):
    def test_login(self):
        # First check for the default behavior
        response = self.client.get("/sekrit/")
        self.assertRedirects(response, "/accounts/login/?next=/sekrit/")

        # Then override the LOGIN_URL setting
        with self.settings(LOGIN_URL="/other/login/"):
            response = self.client.get("/sekrit/")
            self.assertRedirects(response, "/other/login/?next=/sekrit/")

```

This example will override the [`LOGIN_URL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LOGIN_URL) setting for the code in the `with` block and reset its value to the previous state afterward.

SimpleTestCase.modify_settings()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.modify_settings)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.modify_settings "Link to this definition")

It can prove unwieldy to redefine settings that contain a list of values. In practice, adding or removing values is often sufficient. Django provides the [`modify_settings()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.modify_settings "django.test.SimpleTestCase.modify_settings") context manager for easier settings changes:
```
from django.test import TestCase


class MiddlewareTestCase(TestCase):
    def test_cache_middleware(self):
        with self.modify_settings(
            MIDDLEWARE={
                "append": "django.middleware.cache.FetchFromCacheMiddleware",
                "prepend": "django.middleware.cache.UpdateCacheMiddleware",
                "remove": [
                    "django.contrib.sessions.middleware.SessionMiddleware",
                    "django.contrib.auth.middleware.AuthenticationMiddleware",
                    "django.contrib.messages.middleware.MessageMiddleware",
                ],
            }
        ):
            response = self.client.get("/")
            # ...

```

For each action, you can supply either a list of values or a string. When the value already exists in the list, `append` and `prepend` have no effect; neither does `remove` when the value doesn’t exist.

override_settings(_** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/utils/#override_settings)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.override_settings "Link to this definition")

In case you want to override a setting for a test method, Django provides the [`override_settings()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.override_settings "django.test.override_settings") decorator (see
```
from django.test import TestCase, override_settings


class LoginTestCase(TestCase):
    @override_settings(LOGIN_URL="/other/login/")
    def test_login(self):
        response = self.client.get("/sekrit/")
        self.assertRedirects(response, "/other/login/?next=/sekrit/")

```

The decorator can also be applied to [`TestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase") classes:
```
from django.test import TestCase, override_settings


@override_settings(LOGIN_URL="/other/login/")
class LoginTestCase(TestCase):
    def test_login(self):
        response = self.client.get("/sekrit/")
        self.assertRedirects(response, "/other/login/?next=/sekrit/")

```


modify_settings(_* args_, _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/utils/#modify_settings)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.modify_settings "Link to this definition")

Likewise, Django provides the [`modify_settings()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.modify_settings "django.test.modify_settings") decorator:
```
from django.test import TestCase, modify_settings


class MiddlewareTestCase(TestCase):
    @modify_settings(
        MIDDLEWARE={
            "append": "django.middleware.cache.FetchFromCacheMiddleware",
            "prepend": "django.middleware.cache.UpdateCacheMiddleware",
        }
    )
    def test_cache_middleware(self):
        response = self.client.get("/")
        # ...

```

The decorator can also be applied to test case classes:
```
from django.test import TestCase, modify_settings


@modify_settings(
    MIDDLEWARE={
        "append": "django.middleware.cache.FetchFromCacheMiddleware",
        "prepend": "django.middleware.cache.UpdateCacheMiddleware",
    }
)
class MiddlewareTestCase(TestCase):
    def test_cache_middleware(self):
        response = self.client.get("/")
        # ...

```

Note
When given a class, these decorators modify the class directly and return it; they don’t create and return a modified copy of it. So if you try to tweak the above examples to assign the return value to a different name than `LoginTestCase` or `MiddlewareTestCase`, you may be surprised to find that the original test case classes are still equally affected by the decorator. For a given class, [`modify_settings()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.modify_settings "django.test.modify_settings") is always applied after [`override_settings()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.override_settings "django.test.override_settings").
Warning
The settings file contains some settings that are only consulted during initialization of Django internals. If you change them with `override_settings`, the setting is changed if you access it via the `django.conf.settings` module, however, Django’s internals access it differently. Effectively, using [`override_settings()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.override_settings "django.test.override_settings") or [`modify_settings()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.modify_settings "django.test.modify_settings") with these settings is probably not going to do what you expect it to do.
We do not recommend altering the [`DATABASES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES) setting. Altering the [`CACHES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES) setting is possible, but a bit tricky if you are using internals that make using of caching, like [`django.contrib.sessions`](https://docs.djangoproject.com/en/5.0/topics/http/sessions/#module-django.contrib.sessions "django.contrib.sessions: Provides session management for Django projects."). For example, you will have to reinitialize the session backend in a test that uses cached sessions and overrides [`CACHES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES).
Finally, avoid aliasing your settings as module-level constants as `override_settings()` won’t work on such values since they are only evaluated the first time the module is imported.
You can also simulate the absence of a setting by deleting it after settings have been overridden, like this:
```
@override_settings()
def test_something(self):
    del settings.LOGIN_URL
    ...

```

When overriding settings, make sure to handle the cases in which your app’s code uses a cache or similar feature that retains state even if the setting is changed. Django provides the [`django.test.signals.setting_changed`](https://docs.djangoproject.com/en/5.0/ref/signals/#django.test.signals.setting_changed "django.test.signals.setting_changed") signal that lets you register callbacks to clean up and otherwise reset state when settings are changed.
Django itself uses this signal to reset various data:
Overridden settings | Data reset
---|---
USE_TZ, TIME_ZONE | Databases timezone
TEMPLATES | Template engines
SERIALIZATION_MODULES | Serializers cache
LOCALE_PATHS, LANGUAGE_CODE | Default translation and loaded translations
DEFAULT_FILE_STORAGE, STATICFILES_STORAGE, STATIC_ROOT, STATIC_URL, STORAGES | Storages configuration
### Isolating apps[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#isolating-apps "Link to this heading")

utils.isolate_apps(_* app_labels_, _attr_name =None_, _kwarg_name =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.utils.isolate_apps "Link to this definition")

Registers the models defined within a wrapped context into their own isolated [`apps`](https://docs.djangoproject.com/en/5.0/ref/applications/#django.apps.apps "django.apps.apps") registry. This functionality is useful when creating model classes for tests, as the classes will be cleanly deleted afterward, and there is no risk of name collisions.
The app labels which the isolated registry should contain must be passed as individual arguments. You can use `isolate_apps()` as a decorator or a context manager. For example:
```
from django.db import models
from django.test import SimpleTestCase
from django.test.utils import isolate_apps


class MyModelTests(SimpleTestCase):
    @isolate_apps("app_label")
    def test_model_definition(self):
        class TestModel(models.Model):
            pass

        ...

```

… or:
```
with isolate_apps("app_label"):

    class TestModel(models.Model):
        pass

    ...

```

The decorator form can also be applied to classes.
Two optional keyword arguments can be specified:
  * `attr_name`: attribute assigned the isolated registry if used as a class decorator.
  * `kwarg_name`: keyword argument passing the isolated registry if used as a function decorator.


The temporary `Apps` instance used to isolate model registration can be retrieved as an attribute when used as a class decorator by using the `attr_name` parameter:
```
@isolate_apps("app_label", attr_name="apps")
class TestModelDefinition(SimpleTestCase):
    def test_model_definition(self):
        class TestModel(models.Model):
            pass

        self.assertIs(self.apps.get_model("app_label", "TestModel"), TestModel)

```

… or alternatively as an argument on the test method when used as a method decorator by using the `kwarg_name` parameter:
```
class TestModelDefinition(SimpleTestCase):
    @isolate_apps("app_label", kwarg_name="apps")
    def test_model_definition(self, apps):
        class TestModel(models.Model):
            pass

        self.assertIs(apps.get_model("app_label", "TestModel"), TestModel)

```

### Emptying the test outbox[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#emptying-the-test-outbox "Link to this heading")
If you use any of Django’s custom `TestCase` classes, the test runner will clear the contents of the test email outbox at the start of each test case.
For more detail on email services during tests, see [Email services](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#email-services) below.
### Assertions[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#assertions "Link to this heading")
As Python’s normal [`TestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase "django.test.TestCase") class provides a number of custom assertion methods that are useful for testing web applications:
The failure messages given by most of these assertion methods can be customized with the `msg_prefix` argument. This string will be prefixed to any failure message generated by the assertion. This allows you to provide additional details that may help you to identify the location and cause of a failure in your test suite.

SimpleTestCase.assertRaisesMessage(_expected_exception_ , _expected_message_ , _callable_ , _* args_, _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertRaisesMessage)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertRaisesMessage "Link to this definition")


SimpleTestCase.assertRaisesMessage(_expected_exception_ , _expected_message_)

Asserts that execution of `callable` raises `expected_exception` and that `expected_message` is found in the exception’s message. Any other outcome is reported as a failure. It’s a simpler version of `expected_message` isn’t treated as a regular expression.
If only the `expected_exception` and `expected_message` parameters are given, returns a context manager so that the code being tested can be written inline rather than as a function:
```
with self.assertRaisesMessage(ValueError, "invalid literal for int()"):
    int("a")

```


SimpleTestCase.assertWarnsMessage(_expected_warning_ , _expected_message_ , _callable_ , _* args_, _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertWarnsMessage)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertWarnsMessage "Link to this definition")


SimpleTestCase.assertWarnsMessage(_expected_warning_ , _expected_message_)

Analogous to [`SimpleTestCase.assertRaisesMessage()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertRaisesMessage "django.test.SimpleTestCase.assertRaisesMessage") but for

SimpleTestCase.assertFieldOutput(_fieldclass_ , _valid_ , _invalid_ , _field_args =None_, _field_kwargs =None_, _empty_value =''_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertFieldOutput)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertFieldOutput "Link to this definition")

Asserts that a form field behaves correctly with various inputs.

Parameters:

  * **fieldclass** – the class of the field to be tested.
  * **valid** – a dictionary mapping valid inputs to their expected cleaned values.
  * **invalid** – a dictionary mapping invalid inputs to one or more raised error messages.
  * **field_args** – the args passed to instantiate the field.
  * **field_kwargs** – the kwargs passed to instantiate the field.
  * **empty_value** – the expected clean output for inputs in `empty_values`.


For example, the following code tests that an `EmailField` accepts `a@a.com` as a valid email address, but rejects `aaa` with a reasonable error message:
```
self.assertFieldOutput(
    EmailField, {"a@a.com": "a@a.com"}, {"aaa": ["Enter a valid email address."]}
)

```


SimpleTestCase.assertFormError(_form_ , _field_ , _errors_ , _msg_prefix =''_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertFormError)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertFormError "Link to this definition")

Asserts that a field on a form raises the provided list of errors.
`form` is a `Form` instance. The form must be [bound](https://docs.djangoproject.com/en/5.0/ref/forms/api/#ref-forms-api-bound-unbound) but not necessarily validated (`assertFormError()` will automatically call `full_clean()` on the form).
`field` is the name of the field on the form to check. To check the form’s [`non-field errors`](https://docs.djangoproject.com/en/5.0/ref/forms/api/#django.forms.Form.non_field_errors "django.forms.Form.non_field_errors"), use `field=None`.
`errors` is a list of all the error strings that the field is expected to have. You can also pass a single error string if you only expect one error which means that `errors='error message'` is the same as `errors=['error message']`.

SimpleTestCase.assertFormSetError(_formset_ , _form_index_ , _field_ , _errors_ , _msg_prefix =''_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertFormSetError)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertFormSetError "Link to this definition")

Asserts that the `formset` raises the provided list of errors when rendered.
`formset` is a `FormSet` instance. The formset must be bound but not necessarily validated (`assertFormSetError()` will automatically call the `full_clean()` on the formset).
`form_index` is the number of the form within the `FormSet` (starting from 0). Use `form_index=None` to check the formset’s non-form errors, i.e. the errors you get when calling `formset.non_form_errors()`. In that case you must also use `field=None`.
`field` and `errors` have the same meaning as the parameters to `assertFormError()`.
Deprecated since version 4.2: The `assertFormsetError()` assertion method is deprecated. Use `assertFormSetError()` instead.

SimpleTestCase.assertContains(_response_ , _text_ , _count =None_, _status_code =200_, _msg_prefix =''_, _html =False_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertContains)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertContains "Link to this definition")

Asserts that a [`response`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") produced the given [`status_code`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.status_code "django.http.HttpResponse.status_code") and that `text` appears in its [`content`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.content "django.http.HttpResponse.content"). If `count` is provided, `text` must occur exactly `count` times in the response.
Set `html` to `True` to handle `text` as HTML. The comparison with the response content will be based on HTML semantics instead of character-by-character equality. Whitespace is ignored in most cases, attribute ordering is not significant. See [`assertHTMLEqual()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual") for more details.

SimpleTestCase.assertNotContains(_response_ , _text_ , _status_code =200_, _msg_prefix =''_, _html =False_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertNotContains)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertNotContains "Link to this definition")

Asserts that a [`response`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") produced the given [`status_code`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.status_code "django.http.HttpResponse.status_code") and that `text` does _not_ appear in its [`content`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.content "django.http.HttpResponse.content").
Set `html` to `True` to handle `text` as HTML. The comparison with the response content will be based on HTML semantics instead of character-by-character equality. Whitespace is ignored in most cases, attribute ordering is not significant. See [`assertHTMLEqual()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual") for more details.

SimpleTestCase.assertTemplateUsed(_response_ , _template_name_ , _msg_prefix =''_, _count =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertTemplateUsed)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertTemplateUsed "Link to this definition")

Asserts that the template with the given name was used in rendering the response.
`response` must be a response instance returned by the [`test client`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Response "django.test.Response").
`template_name` should be a string such as `'admin/index.html'`.
The `count` argument is an integer indicating the number of times the template should be rendered. Default is `None`, meaning that the template should be rendered one or more times.
You can use this as a context manager, like this:
```
with self.assertTemplateUsed("index.html"):
    render_to_string("index.html")
with self.assertTemplateUsed(template_name="index.html"):
    render_to_string("index.html")

```


SimpleTestCase.assertTemplateNotUsed(_response_ , _template_name_ , _msg_prefix =''_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertTemplateNotUsed)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertTemplateNotUsed "Link to this definition")

Asserts that the template with the given name was _not_ used in rendering the response.
You can use this as a context manager in the same way as [`assertTemplateUsed()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertTemplateUsed "django.test.SimpleTestCase.assertTemplateUsed").

SimpleTestCase.assertURLEqual(_url1_ , _url2_ , _msg_prefix =''_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertURLEqual)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertURLEqual "Link to this definition")

Asserts that two URLs are the same, ignoring the order of query string parameters except for parameters with the same name. For example, `/path/?x=1&y=2` is equal to `/path/?y=2&x=1`, but `/path/?a=1&a=2` isn’t equal to `/path/?a=2&a=1`.

SimpleTestCase.assertRedirects(_response_ , _expected_url_ , _status_code =302_, _target_status_code =200_, _msg_prefix =''_, _fetch_redirect_response =True_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertRedirects)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertRedirects "Link to this definition")

Asserts that the [`response`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") returned a [`status_code`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.status_code "django.http.HttpResponse.status_code") redirect status, redirected to `expected_url` (including any `GET` data), and that the final page was received with `target_status_code`.
If your request used the `follow` argument, the `expected_url` and `target_status_code` will be the url and status code for the final point of the redirect chain.
If `fetch_redirect_response` is `False`, the final page won’t be loaded. Since the test client can’t fetch external URLs, this is particularly useful if `expected_url` isn’t part of your Django app.
Scheme is handled correctly when making comparisons between two URLs. If there isn’t any scheme specified in the location where we are redirected to, the original request’s scheme is used. If present, the scheme in `expected_url` is the one used to make the comparisons to.

SimpleTestCase.assertHTMLEqual(_html1_ , _html2_ , _msg =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertHTMLEqual)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "Link to this definition")

Asserts that the strings `html1` and `html2` are equal. The comparison is based on HTML semantics. The comparison takes following things into account:
  * Whitespace before and after HTML tags is ignored.
  * All types of whitespace are considered equivalent.
  * All open tags are closed implicitly, e.g. when a surrounding tag is closed or the HTML document ends.
  * Empty tags are equivalent to their self-closing version.
  * The ordering of attributes of an HTML element is not significant.
  * Boolean attributes (like `checked`) without an argument are equal to attributes that equal in name and value (see the examples).
  * Text, character references, and entity references that refer to the same character are equivalent.


The following examples are valid tests and don’t raise any `AssertionError`:
```
self.assertHTMLEqual(
    "<p>Hello <b>&#x27;world&#x27;!</p>",
    """<p>
        Hello   <b>&#39;world&#39;! </b>
    </p>""",
)
self.assertHTMLEqual(
    '<input type="checkbox" checked="checked" id="id_accept_terms" />',
    '<input id="id_accept_terms" type="checkbox" checked>',
)

```

`html1` and `html2` must contain HTML. An `AssertionError` will be raised if one of them cannot be parsed.
Output in case of error can be customized with the `msg` argument.

SimpleTestCase.assertHTMLNotEqual(_html1_ , _html2_ , _msg =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertHTMLNotEqual)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLNotEqual "Link to this definition")

Asserts that the strings `html1` and `html2` are _not_ equal. The comparison is based on HTML semantics. See [`assertHTMLEqual()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual") for details.
`html1` and `html2` must contain HTML. An `AssertionError` will be raised if one of them cannot be parsed.
Output in case of error can be customized with the `msg` argument.

SimpleTestCase.assertXMLEqual(_xml1_ , _xml2_ , _msg =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertXMLEqual)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertXMLEqual "Link to this definition")

Asserts that the strings `xml1` and `xml2` are equal. The comparison is based on XML semantics. Similarly to [`assertHTMLEqual()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual"), the comparison is made on parsed content, hence only semantic differences are considered, not syntax differences. When invalid XML is passed in any parameter, an `AssertionError` is always raised, even if both strings are identical.
XML declaration, document type, processing instructions, and comments are ignored. Only the root element and its children are compared.
Output in case of error can be customized with the `msg` argument.

SimpleTestCase.assertXMLNotEqual(_xml1_ , _xml2_ , _msg =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertXMLNotEqual)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertXMLNotEqual "Link to this definition")

Asserts that the strings `xml1` and `xml2` are _not_ equal. The comparison is based on XML semantics. See [`assertXMLEqual()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertXMLEqual "django.test.SimpleTestCase.assertXMLEqual") for details.
Output in case of error can be customized with the `msg` argument.

SimpleTestCase.assertInHTML(_needle_ , _haystack_ , _count =None_, _msg_prefix =''_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertInHTML)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertInHTML "Link to this definition")

Asserts that the HTML fragment `needle` is contained in the `haystack` once.
If the `count` integer argument is specified, then additionally the number of `needle` occurrences will be strictly verified.
Whitespace in most cases is ignored, and attribute ordering is not significant. See [`assertHTMLEqual()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertHTMLEqual "django.test.SimpleTestCase.assertHTMLEqual") for more details.

SimpleTestCase.assertJSONEqual(_raw_ , _expected_data_ , _msg =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertJSONEqual)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertJSONEqual "Link to this definition")

Asserts that the JSON fragments `raw` and `expected_data` are equal. Usual JSON non-significant whitespace rules apply as the heavyweight is delegated to the
Output in case of error can be customized with the `msg` argument.

SimpleTestCase.assertJSONNotEqual(_raw_ , _expected_data_ , _msg =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#SimpleTestCase.assertJSONNotEqual)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertJSONNotEqual "Link to this definition")

Asserts that the JSON fragments `raw` and `expected_data` are _not_ equal. See [`assertJSONEqual()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertJSONEqual "django.test.SimpleTestCase.assertJSONEqual") for further details.
Output in case of error can be customized with the `msg` argument.

TransactionTestCase.assertQuerySetEqual(_qs_ , _values_ , _transform =None_, _ordered =True_, _msg =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#TransactionTestCase.assertQuerySetEqual)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase.assertQuerySetEqual "Link to this definition")

Asserts that a queryset `qs` matches a particular iterable of values `values`.
If `transform` is provided, `values` is compared to a list produced by applying `transform` to each member of `qs`.
By default, the comparison is also ordering dependent. If `qs` doesn’t provide an implicit ordering, you can set the `ordered` parameter to `False`, which turns the comparison into a `collections.Counter` comparison. If the order is undefined (if the given `qs` isn’t ordered and the comparison is against more than one ordered value), a `ValueError` is raised.
Output in case of error can be customized with the `msg` argument.
Deprecated since version 4.2: The `assertQuerysetEqual()` assertion method is deprecated. Use `assertQuerySetEqual()` instead.

TransactionTestCase.assertNumQueries(_num_ , _func_ , _* args_, _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#TransactionTestCase.assertNumQueries)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase.assertNumQueries "Link to this definition")

Asserts that when `func` is called with `*args` and `**kwargs` that `num` database queries are executed.
If a `"using"` key is present in `kwargs` it is used as the database alias for which to check the number of queries:
```
self.assertNumQueries(7, using="non_default_db")

```

If you wish to call a function with a `using` parameter you can do it by wrapping the call with a `lambda` to add an extra parameter:
```
self.assertNumQueries(7, lambda: my_function(using=7))

```

You can also use this as a context manager:
```
with self.assertNumQueries(2):
    Person.objects.create(name="Aaron")
    Person.objects.create(name="Daniel")

```

### Tagging tests[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#tagging-tests "Link to this heading")
You can tag your tests so you can easily run a particular subset. For example, you might label fast or slow tests:
```
from django.test import tag


class SampleTestCase(TestCase):
    @tag("fast")
    def test_fast(self): ...

    @tag("slow")
    def test_slow(self): ...

    @tag("slow", "core")
    def test_slow_but_core(self): ...

```

You can also tag a test case class:
```
@tag("slow", "core")
class SampleTestCase(TestCase): ...

```

Subclasses inherit tags from superclasses, and methods inherit tags from their class. Given:
```
@tag("foo")
class SampleTestCaseChild(SampleTestCase):
    @tag("bar")
    def test(self): ...

```

`SampleTestCaseChild.test` will be labeled with `'slow'`, `'core'`, `'bar'`, and `'foo'`.
Then you can choose which tests to run. For example, to run only fast tests:
/ 
```
$ ./manage.py test --tag=fast

```

```
...\> manage.py test --tag=fast

```

Or to run fast tests and the core one (even though it’s slow):
/ 
```
$ ./manage.py test --tag=fast --tag=core

```

```
...\> manage.py test --tag=fast --tag=core

```

You can also exclude tests by tag. To run core tests if they are not slow:
/ 
```
$ ./manage.py test --tag=core --exclude-tag=slow

```

```
...\> manage.py test --tag=core --exclude-tag=slow

```

[`test --exclude-tag`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-exclude-tag) has precedence over [`test --tag`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-test-tag), so if a test has two tags and you select one of them and exclude the other, the test won’t be run.
