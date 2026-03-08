## Skipping tests[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#skipping-tests "Link to this heading")
The unittest library provides the
For example, if your test requires a particular optional library in order to succeed, you could decorate the test case with
To supplement these test skipping behaviors, Django provides two additional skip decorators. Instead of testing a generic boolean, these decorators check the capabilities of the database, and skip the test if the database doesn’t support a specific named feature.
The decorators use a string identifier to describe database features. This string corresponds to attributes of the database connection features class. See

skipIfDBFeature(_* feature_name_strings_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#skipIfDBFeature)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.skipIfDBFeature "Link to this definition")

Skip the decorated test or `TestCase` if all of the named database features are supported.
For example, the following test will not be executed if the database supports transactions (e.g., it would _not_ run under PostgreSQL, but it would under MySQL with MyISAM tables):
```
class MyTests(TestCase):
    @skipIfDBFeature("supports_transactions")
    def test_transaction_behavior(self):
        # ... conditional test code
        pass

```


skipUnlessDBFeature(_* feature_name_strings_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/testcases/#skipUnlessDBFeature)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.skipUnlessDBFeature "Link to this definition")

Skip the decorated test or `TestCase` if any of the named database features are _not_ supported.
For example, the following test will only be executed if the database supports transactions (e.g., it would run under PostgreSQL, but _not_ under MySQL with MyISAM tables):
```
class MyTests(TestCase):
    @skipUnlessDBFeature("supports_transactions")
    def test_transaction_behavior(self):
        # ... conditional test code
        pass

```

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/testing/overview/)
[Advanced testing topics ](https://docs.djangoproject.com/en/5.0/topics/testing/advanced/)
[](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#top)
