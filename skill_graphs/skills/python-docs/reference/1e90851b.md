## Classes and functions[¶](https://docs.python.org/3/library/unittest.html#classes-and-functions "Link to this heading")
This section describes in depth the API of `unittest`.
### Test cases[¶](https://docs.python.org/3/library/unittest.html#test-cases "Link to this heading")

_class_ unittest.TestCase(_methodName ='runTest'_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase "Link to this definition")

Instances of the `TestCase` class represent the logical test units in the `unittest` universe. This class is intended to be used as a base class, with specific tests being implemented by concrete subclasses. This class implements the interface needed by the test runner to allow it to drive the tests, and methods that the test code can use to check for and report various kinds of failure.
Each instance of `TestCase` will run a single base method: the method named _methodName_. In most uses of `TestCase`, you will neither change the _methodName_ nor reimplement the default `runTest()` method.
Changed in version 3.2: `TestCase` can be instantiated successfully without providing a _methodName_. This makes it easier to experiment with `TestCase` from the interactive interpreter.
`TestCase` instances provide three groups of methods: one group used to run the test, another used by the test implementation to check conditions and report failures, and some inquiry methods allowing information about the test itself to be gathered.
Methods in the first group (running the test) are:

setUp()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "Link to this definition")

Method called to prepare the test fixture. This is called immediately before calling the test method; other than [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError") or [`SkipTest`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest"), any exception raised by this method will be considered an error rather than a test failure. The default implementation does nothing.

tearDown()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "Link to this definition")

Method called immediately after the test method has been called and the result recorded. This is called even if the test method raised an exception, so the implementation in subclasses may need to be particularly careful about checking internal state. Any exception, other than [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError") or [`SkipTest`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest"), raised by this method will be considered an additional error rather than a test failure (thus increasing the total number of reported errors). This method will only be called if the [`setUp()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") succeeds, regardless of the outcome of the test method. The default implementation does nothing.

setUpClass()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUpClass "Link to this definition")

A class method called before tests in an individual class are run. `setUpClass` is called with the class as the only argument and must be decorated as a [`classmethod()`](https://docs.python.org/3/library/functions.html#classmethod "classmethod"):
Copy```
@classmethod
def setUpClass(cls):
    ...

```

See [Class and Module Fixtures](https://docs.python.org/3/library/unittest.html#class-and-module-fixtures) for more details.
Added in version 3.2.

tearDownClass()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDownClass "Link to this definition")

A class method called after tests in an individual class have run. `tearDownClass` is called with the class as the only argument and must be decorated as a [`classmethod()`](https://docs.python.org/3/library/functions.html#classmethod "classmethod"):
Copy```
@classmethod
def tearDownClass(cls):
    ...

```

See [Class and Module Fixtures](https://docs.python.org/3/library/unittest.html#class-and-module-fixtures) for more details.
Added in version 3.2.

run(_result =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.run "Link to this definition")

Run the test, collecting the result into the [`TestResult`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") object passed as _result_. If _result_ is omitted or `None`, a temporary result object is created (by calling the [`defaultTestResult()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.defaultTestResult "unittest.TestCase.defaultTestResult") method) and used. The result object is returned to `run()`’s caller.
The same effect may be had by simply calling the `TestCase` instance.
Changed in version 3.3: Previous versions of `run` did not return the result. Neither did calling an instance.

skipTest(_reason_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.skipTest "Link to this definition")

Calling this during a test method or [`setUp()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") skips the current test. See [Skipping tests and expected failures](https://docs.python.org/3/library/unittest.html#unittest-skipping) for more information.
Added in version 3.1.

subTest(_msg =None_, _** params_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.subTest "Link to this definition")

Return a context manager which executes the enclosed code block as a subtest. _msg_ and _params_ are optional, arbitrary values which are displayed whenever a subtest fails, allowing you to identify them clearly.
A test case can contain any number of subtest declarations, and they can be arbitrarily nested.
See [Distinguishing test iterations using subtests](https://docs.python.org/3/library/unittest.html#subtests) for more information.
Added in version 3.4.

debug()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug "Link to this definition")

Run the test without collecting the result. This allows exceptions raised by the test to be propagated to the caller, and can be used to support running tests under a debugger.
The `TestCase` class provides several assert methods to check for and report failures. The following table lists the most commonly used methods (see the tables below for more assert methods):
Method | Checks that | New in
---|---|---
[`assertEqual(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual") | `a == b` |
[`assertNotEqual(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual "unittest.TestCase.assertNotEqual") | `a != b` |
[`assertTrue(x)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue "unittest.TestCase.assertTrue") | `bool(x) is True` |
[`assertFalse(x)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertFalse "unittest.TestCase.assertFalse") | `bool(x) is False` |
[`assertIs(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs "unittest.TestCase.assertIs") | `a is b` | 3.1
[`assertIsNot(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot "unittest.TestCase.assertIsNot") | `a is not b` | 3.1
[`assertIsNone(x)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNone "unittest.TestCase.assertIsNone") | `x is None` | 3.1
[`assertIsNotNone(x)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNotNone "unittest.TestCase.assertIsNotNone") | `x is not None` | 3.1
[`assertIn(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn "unittest.TestCase.assertIn") | `a in b` | 3.1
[`assertNotIn(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIn "unittest.TestCase.assertNotIn") | `a not in b` | 3.1
[`assertIsInstance(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsInstance "unittest.TestCase.assertIsInstance") | `isinstance(a, b)` | 3.2
[`assertNotIsInstance(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsInstance "unittest.TestCase.assertNotIsInstance") | `not isinstance(a, b)` | 3.2
[`assertIsSubclass(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsSubclass "unittest.TestCase.assertIsSubclass") | `issubclass(a, b)` | 3.14
[`assertNotIsSubclass(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsSubclass "unittest.TestCase.assertNotIsSubclass") | `not issubclass(a, b)` | 3.14
All the assert methods accept a _msg_ argument that, if specified, is used as the error message on failure (see also [`longMessage`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.longMessage "unittest.TestCase.longMessage")). Note that the _msg_ keyword argument can be passed to [`assertRaises()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "unittest.TestCase.assertRaises"), [`assertRaisesRegex()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegex "unittest.TestCase.assertRaisesRegex"), [`assertWarns()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns "unittest.TestCase.assertWarns"), [`assertWarnsRegex()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarnsRegex "unittest.TestCase.assertWarnsRegex") only when they are used as a context manager.

assertEqual(_first_ , _second_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "Link to this definition")

Test that _first_ and _second_ are equal. If the values do not compare equal, the test will fail.
In addition, if _first_ and _second_ are the exact same type and one of list, tuple, dict, set, frozenset or str or any type that a subclass registers with [`addTypeEqualityFunc()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addTypeEqualityFunc "unittest.TestCase.addTypeEqualityFunc") the type-specific equality function will be called in order to generate a more useful default error message (see also the [list of type-specific methods](https://docs.python.org/3/library/unittest.html#type-specific-methods)).
Changed in version 3.1: Added the automatic calling of type-specific equality function.
Changed in version 3.2: [`assertMultiLineEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertMultiLineEqual "unittest.TestCase.assertMultiLineEqual") added as the default type equality function for comparing strings.

assertNotEqual(_first_ , _second_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual "Link to this definition")

Test that _first_ and _second_ are not equal. If the values do compare equal, the test will fail.

assertTrue(_expr_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue "Link to this definition")


assertFalse(_expr_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertFalse "Link to this definition")

Test that _expr_ is true (or false).
Note that this is equivalent to `bool(expr) is True` and not to `expr is True` (use `assertIs(expr, True)` for the latter). This method should also be avoided when more specific methods are available (e.g. `assertEqual(a, b)` instead of `assertTrue(a == b)`), because they provide a better error message in case of failure.

assertIs(_first_ , _second_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs "Link to this definition")


assertIsNot(_first_ , _second_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot "Link to this definition")

Test that _first_ and _second_ are (or are not) the same object.
Added in version 3.1.

assertIsNone(_expr_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNone "Link to this definition")


assertIsNotNone(_expr_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNotNone "Link to this definition")

Test that _expr_ is (or is not) `None`.
Added in version 3.1.

assertIn(_member_ , _container_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn "Link to this definition")


assertNotIn(_member_ , _container_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIn "Link to this definition")

Test that _member_ is (or is not) in _container_.
Added in version 3.1.

assertIsInstance(_obj_ , _cls_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsInstance "Link to this definition")


assertNotIsInstance(_obj_ , _cls_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsInstance "Link to this definition")

Test that _obj_ is (or is not) an instance of _cls_ (which can be a class or a tuple of classes, as supported by [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance")). To check for the exact type, use [`assertIs(type(obj), cls)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs "unittest.TestCase.assertIs").
Added in version 3.2.

assertIsSubclass(_cls_ , _superclass_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsSubclass "Link to this definition")


assertNotIsSubclass(_cls_ , _superclass_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsSubclass "Link to this definition")

Test that _cls_ is (or is not) a subclass of _superclass_ (which can be a class or a tuple of classes, as supported by [`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass "issubclass")). To check for the exact type, use [`assertIs(cls, superclass)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs "unittest.TestCase.assertIs").
Added in version 3.14.
It is also possible to check the production of exceptions, warnings, and log messages using the following methods:
Method | Checks that | New in
---|---|---
[`assertRaises(exc, fun, *args, **kwds)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "unittest.TestCase.assertRaises") | `fun(*args, **kwds)` raises _exc_ |
[`assertRaisesRegex(exc, r, fun, *args, **kwds)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegex "unittest.TestCase.assertRaisesRegex") | `fun(*args, **kwds)` raises _exc_ and the message matches regex _r_ | 3.1
[`assertWarns(warn, fun, *args, **kwds)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns "unittest.TestCase.assertWarns") | `fun(*args, **kwds)` raises _warn_ | 3.2
[`assertWarnsRegex(warn, r, fun, *args, **kwds)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarnsRegex "unittest.TestCase.assertWarnsRegex") | `fun(*args, **kwds)` raises _warn_ and the message matches regex _r_ | 3.2
[`assertLogs(logger, level)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLogs "unittest.TestCase.assertLogs") | The `with` block logs on _logger_ with minimum _level_ | 3.4
[`assertNoLogs(logger, level)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNoLogs "unittest.TestCase.assertNoLogs") |

The `with` block does not log on
     _logger_ with minimum _level_ | 3.10

assertRaises(_exception_ , _callable_ , _* args_, _** kwds_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "Link to this definition")


assertRaises(_exception_ , _*_ , _msg =None_)

Test that an exception is raised when _callable_ is called with any positional or keyword arguments that are also passed to `assertRaises()`. The test passes if _exception_ is raised, is an error if another exception is raised, or fails if no exception is raised. To catch any of a group of exceptions, a tuple containing the exception classes may be passed as _exception_.
If only the _exception_ and possibly the _msg_ arguments are given, return a context manager so that the code under test can be written inline rather than as a function:
Copy```
with self.assertRaises(SomeException):
    do_something()

```

When used as a context manager, `assertRaises()` accepts the additional keyword argument _msg_.
The context manager will store the caught exception object in its `exception` attribute. This can be useful if the intention is to perform additional checks on the exception raised:
Copy```
with self.assertRaises(SomeException) as cm:
    do_something()

the_exception = cm.exception
self.assertEqual(the_exception.error_code, 3)

```

Changed in version 3.1: Added the ability to use `assertRaises()` as a context manager.
Changed in version 3.2: Added the `exception` attribute.
Changed in version 3.3: Added the _msg_ keyword argument when used as a context manager.

assertRaisesRegex(_exception_ , _regex_ , _callable_ , _* args_, _** kwds_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegex "Link to this definition")


assertRaisesRegex(_exception_ , _regex_ , _*_ , _msg =None_)

Like [`assertRaises()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "unittest.TestCase.assertRaises") but also tests that _regex_ matches on the string representation of the raised exception. _regex_ may be a regular expression object or a string containing a regular expression suitable for use by [`re.search()`](https://docs.python.org/3/library/re.html#re.search "re.search"). Examples:
Copy```
self.assertRaisesRegex(ValueError, "invalid literal for.*XYZ'$",
                       int, 'XYZ')

```

or:
Copy```
with self.assertRaisesRegex(ValueError, 'literal'):
   int('XYZ')

```

Added in version 3.1: Added under the name `assertRaisesRegexp`.
Changed in version 3.2: Renamed to `assertRaisesRegex()`.
Changed in version 3.3: Added the _msg_ keyword argument when used as a context manager.

assertWarns(_warning_ , _callable_ , _* args_, _** kwds_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns "Link to this definition")


assertWarns(_warning_ , _*_ , _msg =None_)

Test that a warning is triggered when _callable_ is called with any positional or keyword arguments that are also passed to `assertWarns()`. The test passes if _warning_ is triggered and fails if it isn’t. Any exception is an error. To catch any of a group of warnings, a tuple containing the warning classes may be passed as _warnings_.
If only the _warning_ and possibly the _msg_ arguments are given, return a context manager so that the code under test can be written inline rather than as a function:
Copy```
with self.assertWarns(SomeWarning):
    do_something()

```

When used as a context manager, `assertWarns()` accepts the additional keyword argument _msg_.
The context manager will store the caught warning object in its `warning` attribute, and the source line which triggered the warnings in the `filename` and `lineno` attributes. This can be useful if the intention is to perform additional checks on the warning caught:
Copy```
with self.assertWarns(SomeWarning) as cm:
    do_something()

self.assertIn('myfile.py', cm.filename)
self.assertEqual(320, cm.lineno)

```

This method works regardless of the warning filters in place when it is called.
Added in version 3.2.
Changed in version 3.3: Added the _msg_ keyword argument when used as a context manager.

assertWarnsRegex(_warning_ , _regex_ , _callable_ , _* args_, _** kwds_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarnsRegex "Link to this definition")


assertWarnsRegex(_warning_ , _regex_ , _*_ , _msg =None_)

Like [`assertWarns()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns "unittest.TestCase.assertWarns") but also tests that _regex_ matches on the message of the triggered warning. _regex_ may be a regular expression object or a string containing a regular expression suitable for use by [`re.search()`](https://docs.python.org/3/library/re.html#re.search "re.search"). Example:
Copy```
self.assertWarnsRegex(DeprecationWarning,
                      r'legacy_function\(\) is deprecated',
                      legacy_function, 'XYZ')

```

or:
Copy```
with self.assertWarnsRegex(RuntimeWarning, 'unsafe frobnicating'):
    frobnicate('/etc/passwd')

```

Added in version 3.2.
Changed in version 3.3: Added the _msg_ keyword argument when used as a context manager.

assertLogs(_logger =None_, _level =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLogs "Link to this definition")

A context manager to test that at least one message is logged on the _logger_ or one of its children, with at least the given _level_.
If given, _logger_ should be a [`logging.Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") object or a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") giving the name of a logger. The default is the root logger, which will catch all messages that were not blocked by a non-propagating descendent logger.
If given, _level_ should be either a numeric logging level or its string equivalent (for example either `"ERROR"` or [`logging.ERROR`](https://docs.python.org/3/library/logging.html#logging.ERROR "logging.ERROR")). The default is [`logging.INFO`](https://docs.python.org/3/library/logging.html#logging.INFO "logging.INFO").
The test passes if at least one message emitted inside the `with` block matches the _logger_ and _level_ conditions, otherwise it fails.
The object returned by the context manager is a recording helper which keeps tracks of the matching log messages. It has two attributes:

records[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.records "Link to this definition")

A list of [`logging.LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") objects of the matching log messages.

output[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.output "Link to this definition")

A list of [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") objects with the formatted output of matching messages.
Example:
Copy```
with self.assertLogs('foo', level='INFO') as cm:
    logging.getLogger('foo').info('first message')
    logging.getLogger('foo.bar').error('second message')
self.assertEqual(cm.output, ['INFO:foo:first message',
                             'ERROR:foo.bar:second message'])

```

Added in version 3.4.

assertNoLogs(_logger =None_, _level =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNoLogs "Link to this definition")

A context manager to test that no messages are logged on the _logger_ or one of its children, with at least the given _level_.
If given, _logger_ should be a [`logging.Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") object or a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") giving the name of a logger. The default is the root logger, which will catch all messages.
If given, _level_ should be either a numeric logging level or its string equivalent (for example either `"ERROR"` or [`logging.ERROR`](https://docs.python.org/3/library/logging.html#logging.ERROR "logging.ERROR")). The default is [`logging.INFO`](https://docs.python.org/3/library/logging.html#logging.INFO "logging.INFO").
Unlike [`assertLogs()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLogs "unittest.TestCase.assertLogs"), nothing will be returned by the context manager.
Added in version 3.10.
There are also other methods used to perform more specific checks, such as:
Method | Checks that | New in
---|---|---
[`assertAlmostEqual(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual "unittest.TestCase.assertAlmostEqual") | `round(a-b, 7) == 0` |
[`assertNotAlmostEqual(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotAlmostEqual "unittest.TestCase.assertNotAlmostEqual") | `round(a-b, 7) != 0` |
[`assertGreater(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreater "unittest.TestCase.assertGreater") | `a > b` | 3.1
[`assertGreaterEqual(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreaterEqual "unittest.TestCase.assertGreaterEqual") | `a >= b` | 3.1
[`assertLess(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLess "unittest.TestCase.assertLess") | `a < b` | 3.1
[`assertLessEqual(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLessEqual "unittest.TestCase.assertLessEqual") | `a <= b` | 3.1
[`assertRegex(s, r)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRegex "unittest.TestCase.assertRegex") | `r.search(s)` | 3.1
