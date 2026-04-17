## Reusing old test code[¶](https://docs.python.org/3/library/unittest.html#re-using-old-test-code "Link to this heading")
Some users will find that they have existing test code that they would like to run from `unittest`, without converting every old test function to a [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") subclass.
For this reason, `unittest` provides a [`FunctionTestCase`](https://docs.python.org/3/library/unittest.html#unittest.FunctionTestCase "unittest.FunctionTestCase") class. This subclass of [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") can be used to wrap an existing test function. Set-up and tear-down functions can also be provided.
Given the following test function:
Copy```
def testSomething():
    something = makeSomething()
    assert something.name is not None
    # ...

```

one can create an equivalent test case instance as follows, with optional set-up and tear-down methods:
Copy```
testcase = unittest.FunctionTestCase(testSomething,
                                     setUp=makeSomethingDB,
                                     tearDown=deleteSomethingDB)

```

Note
Even though [`FunctionTestCase`](https://docs.python.org/3/library/unittest.html#unittest.FunctionTestCase "unittest.FunctionTestCase") can be used to quickly convert an existing test base over to a `unittest`-based system, this approach is not recommended. Taking the time to set up proper [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") subclasses will make future test refactorings infinitely easier.
In some cases, the existing tests may have been written using the [`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.") module. If so, `doctest` provides a [`DocTestSuite`](https://docs.python.org/3/library/doctest.html#doctest.DocTestSuite "doctest.DocTestSuite") class that can automatically build [`unittest.TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") instances from the existing `doctest`-based tests.
