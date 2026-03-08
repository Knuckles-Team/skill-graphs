## Skipping tests and expected failures[¶](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures "Link to this heading")
Added in version 3.1.
Unittest supports skipping individual test methods and even whole classes of tests. In addition, it supports marking a test as an “expected failure,” a test that is broken and will fail, but shouldn’t be counted as a failure on a [`TestResult`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult").
Skipping a test is simply a matter of using the [`skip()`](https://docs.python.org/3/library/unittest.html#unittest.skip "unittest.skip") [decorator](https://docs.python.org/3/glossary.html#term-decorator) or one of its conditional variants, calling [`TestCase.skipTest()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.skipTest "unittest.TestCase.skipTest") within a [`setUp()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") or test method, or raising [`SkipTest`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest") directly.
Basic skipping looks like this:
Copy```
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass

```

This is the output of running the example above in verbose mode:
Copy```
test_format (__main__.MyTestCase.test_format) ... skipped 'not supported in this library version'
test_nothing (__main__.MyTestCase.test_nothing) ... skipped 'demonstrating skipping'
test_maybe_skipped (__main__.MyTestCase.test_maybe_skipped) ... skipped 'external resource not available'
test_windows_support (__main__.MyTestCase.test_windows_support) ... skipped 'requires Windows'

----------------------------------------------------------------------
Ran 4 tests in 0.005s

OK (skipped=4)

```

Classes can be skipped just like methods:
Copy```
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass

```

[`TestCase.setUp()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") can also skip the test. This is useful when a resource that needs to be set up is not available.
Expected failures use the [`expectedFailure()`](https://docs.python.org/3/library/unittest.html#unittest.expectedFailure "unittest.expectedFailure") decorator.
Copy```
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")

```

It’s easy to roll your own skipping decorators by making a decorator that calls [`skip()`](https://docs.python.org/3/library/unittest.html#unittest.skip "unittest.skip") on the test when it wants it to be skipped. This decorator skips the test unless the passed object has a certain attribute:
Copy```
def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))

```

The following decorators and exception implement test skipping and expected failures:

@unittest.skip(_reason_)[¶](https://docs.python.org/3/library/unittest.html#unittest.skip "Link to this definition")

Unconditionally skip the decorated test. _reason_ should describe why the test is being skipped.

@unittest.skipIf(_condition_ , _reason_)[¶](https://docs.python.org/3/library/unittest.html#unittest.skipIf "Link to this definition")

Skip the decorated test if _condition_ is true.

@unittest.skipUnless(_condition_ , _reason_)[¶](https://docs.python.org/3/library/unittest.html#unittest.skipUnless "Link to this definition")

Skip the decorated test unless _condition_ is true.

@unittest.expectedFailure[¶](https://docs.python.org/3/library/unittest.html#unittest.expectedFailure "Link to this definition")

Mark the test as an expected failure or error. If the test fails or errors in the test function itself (rather than in one of the _test fixture_ methods) then it will be considered a success. If the test passes, it will be considered a failure.

_exception_ unittest.SkipTest(_reason_)[¶](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "Link to this definition")

This exception is raised to skip a test.
Usually you can use [`TestCase.skipTest()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.skipTest "unittest.TestCase.skipTest") or one of the skipping decorators instead of raising this directly.
Skipped tests will not have [`setUp()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") or [`tearDown()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown") run around them. Skipped classes will not have [`setUpClass()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUpClass "unittest.TestCase.setUpClass") or [`tearDownClass()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDownClass "unittest.TestCase.tearDownClass") run. Skipped modules will not have [`setUpModule()`](https://docs.python.org/3/library/unittest.html#unittest.setUpModule "unittest.setUpModule") or [`tearDownModule()`](https://docs.python.org/3/library/unittest.html#unittest.tearDownModule "unittest.tearDownModule") run.
## Distinguishing test iterations using subtests[¶](https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests "Link to this heading")
Added in version 3.4.
When there are very small differences among your tests, for instance some parameters, unittest allows you to distinguish them inside the body of a test method using the [`subTest()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.subTest "unittest.TestCase.subTest") context manager.
For example, the following test:
Copy```
class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

```

will produce the following output:
Copy```
======================================================================
FAIL: test_even (__main__.NumbersTest.test_even) (i=1)
Test that numbers between 0 and 5 are all even.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 11, in test_even
    self.assertEqual(i % 2, 0)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1 != 0

======================================================================
FAIL: test_even (__main__.NumbersTest.test_even) (i=3)
Test that numbers between 0 and 5 are all even.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 11, in test_even
    self.assertEqual(i % 2, 0)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1 != 0

======================================================================
FAIL: test_even (__main__.NumbersTest.test_even) (i=5)
Test that numbers between 0 and 5 are all even.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 11, in test_even
    self.assertEqual(i % 2, 0)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 1 != 0

```

Without using a subtest, execution would stop after the first failure, and the error would be less easy to diagnose because the value of `i` wouldn’t be displayed:
Copy```
======================================================================
FAIL: test_even (__main__.NumbersTest.test_even)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "subtests.py", line 32, in test_even
    self.assertEqual(i % 2, 0)
AssertionError: 1 != 0

```
