[`assertNotRegex(s, r)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotRegex "unittest.TestCase.assertNotRegex") | `not r.search(s)` | 3.2
[`assertCountEqual(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertCountEqual "unittest.TestCase.assertCountEqual") | _a_ and _b_ have the same elements in the same number, regardless of their order. | 3.2
[`assertStartsWith(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertStartsWith "unittest.TestCase.assertStartsWith") | `a.startswith(b)` | 3.14
[`assertNotStartsWith(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotStartsWith "unittest.TestCase.assertNotStartsWith") | `not a.startswith(b)` | 3.14
[`assertEndsWith(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEndsWith "unittest.TestCase.assertEndsWith") | `a.endswith(b)` | 3.14
[`assertNotEndsWith(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEndsWith "unittest.TestCase.assertNotEndsWith") | `not a.endswith(b)` | 3.14
[`assertHasAttr(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertHasAttr "unittest.TestCase.assertHasAttr") | `hastattr(a, b)` | 3.14
[`assertNotHasAttr(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotHasAttr "unittest.TestCase.assertNotHasAttr") | `not hastattr(a, b)` | 3.14

assertAlmostEqual(_first_ , _second_ , _places =7_, _msg =None_, _delta =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual "Link to this definition")


assertNotAlmostEqual(_first_ , _second_ , _places =7_, _msg =None_, _delta =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotAlmostEqual "Link to this definition")

Test that _first_ and _second_ are approximately (or not approximately) equal by computing the difference, rounding to the given number of decimal _places_ (default 7), and comparing to zero. Note that these methods round the values to the given number of _decimal places_ (i.e. like the [`round()`](https://docs.python.org/3/library/functions.html#round "round") function) and not _significant digits_.
If _delta_ is supplied instead of _places_ then the difference between _first_ and _second_ must be less or equal to (or greater than) _delta_.
Supplying both _delta_ and _places_ raises a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").
Changed in version 3.2: `assertAlmostEqual()` automatically considers almost equal objects that compare equal. `assertNotAlmostEqual()` automatically fails if the objects compare equal. Added the _delta_ keyword argument.

assertGreater(_first_ , _second_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreater "Link to this definition")


assertGreaterEqual(_first_ , _second_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertGreaterEqual "Link to this definition")


assertLess(_first_ , _second_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLess "Link to this definition")


assertLessEqual(_first_ , _second_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLessEqual "Link to this definition")

Test that _first_ is respectively >, >=, < or <= than _second_ depending on the method name. If not, the test will fail:
Copy```
>>> self.assertGreaterEqual(3, 4)
AssertionError: "3" unexpectedly not greater than or equal to "4"

```

Added in version 3.1.

assertRegex(_text_ , _regex_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRegex "Link to this definition")


assertNotRegex(_text_ , _regex_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotRegex "Link to this definition")

Test that a _regex_ search matches (or does not match) _text_. In case of failure, the error message will include the pattern and the _text_ (or the pattern and the part of _text_ that unexpectedly matched). _regex_ may be a regular expression object or a string containing a regular expression suitable for use by [`re.search()`](https://docs.python.org/3/library/re.html#re.search "re.search").
Added in version 3.1: Added under the name `assertRegexpMatches`.
Changed in version 3.2: The method `assertRegexpMatches()` has been renamed to `assertRegex()`.
Added in version 3.2: `assertNotRegex()`.

assertCountEqual(_first_ , _second_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertCountEqual "Link to this definition")

Test that sequence _first_ contains the same elements as _second_ , regardless of their order. When they don’t, an error message listing the differences between the sequences will be generated.
Duplicate elements are _not_ ignored when comparing _first_ and _second_. It verifies whether each element has the same count in both sequences. Equivalent to: `assertEqual(Counter(list(first)), Counter(list(second)))` but works with sequences of unhashable objects as well.
Added in version 3.2.

assertStartsWith(_s_ , _prefix_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertStartsWith "Link to this definition")


assertNotStartsWith(_s_ , _prefix_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotStartsWith "Link to this definition")

Test that the Unicode or byte string _s_ starts (or does not start) with a _prefix_. _prefix_ can also be a tuple of strings to try.
Added in version 3.14.

assertEndsWith(_s_ , _suffix_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEndsWith "Link to this definition")


assertNotEndsWith(_s_ , _suffix_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEndsWith "Link to this definition")

Test that the Unicode or byte string _s_ ends (or does not end) with a _suffix_. _suffix_ can also be a tuple of strings to try.
Added in version 3.14.

assertHasAttr(_obj_ , _name_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertHasAttr "Link to this definition")


assertNotHasAttr(_obj_ , _name_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotHasAttr "Link to this definition")

Test that the object _obj_ has (or has not) an attribute _name_.
Added in version 3.14.
The [`assertEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual") method dispatches the equality check for objects of the same type to different type-specific methods. These methods are already implemented for most of the built-in types, but it’s also possible to register new methods using [`addTypeEqualityFunc()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addTypeEqualityFunc "unittest.TestCase.addTypeEqualityFunc"):

addTypeEqualityFunc(_typeobj_ , _function_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addTypeEqualityFunc "Link to this definition")

Registers a type-specific method called by [`assertEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual") to check if two objects of exactly the same _typeobj_ (not subclasses) compare equal. _function_ must take two positional arguments and a third msg=None keyword argument just as `assertEqual()` does. It must raise [`self.failureException(msg)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.failureException "unittest.TestCase.failureException") when inequality between the first two parameters is detected – possibly providing useful information and explaining the inequalities in details in the error message.
Added in version 3.1.
The list of type-specific methods automatically used by [`assertEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual") are summarized in the following table. Note that it’s usually not necessary to invoke these methods directly.
Method | Used to compare | New in
---|---|---
[`assertMultiLineEqual(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertMultiLineEqual "unittest.TestCase.assertMultiLineEqual") | strings | 3.1
[`assertSequenceEqual(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSequenceEqual "unittest.TestCase.assertSequenceEqual") | sequences | 3.1
[`assertListEqual(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertListEqual "unittest.TestCase.assertListEqual") | lists | 3.1
[`assertTupleEqual(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTupleEqual "unittest.TestCase.assertTupleEqual") | tuples | 3.1
[`assertSetEqual(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSetEqual "unittest.TestCase.assertSetEqual") | sets or frozensets | 3.1
[`assertDictEqual(a, b)`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertDictEqual "unittest.TestCase.assertDictEqual") | dicts | 3.1

assertMultiLineEqual(_first_ , _second_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertMultiLineEqual "Link to this definition")

Test that the multiline string _first_ is equal to the string _second_. When not equal a diff of the two strings highlighting the differences will be included in the error message. This method is used by default when comparing strings with [`assertEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual").
Added in version 3.1.

assertSequenceEqual(_first_ , _second_ , _msg =None_, _seq_type =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSequenceEqual "Link to this definition")

Tests that two sequences are equal. If a _seq_type_ is supplied, both _first_ and _second_ must be instances of _seq_type_ or a failure will be raised. If the sequences are different an error message is constructed that shows the difference between the two.
This method is not called directly by [`assertEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual"), but it’s used to implement [`assertListEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertListEqual "unittest.TestCase.assertListEqual") and [`assertTupleEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTupleEqual "unittest.TestCase.assertTupleEqual").
Added in version 3.1.

assertListEqual(_first_ , _second_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertListEqual "Link to this definition")


assertTupleEqual(_first_ , _second_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTupleEqual "Link to this definition")

Tests that two lists or tuples are equal. If not, an error message is constructed that shows only the differences between the two. An error is also raised if either of the parameters are of the wrong type. These methods are used by default when comparing lists or tuples with [`assertEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual").
Added in version 3.1.

assertSetEqual(_first_ , _second_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSetEqual "Link to this definition")

Tests that two sets are equal. If not, an error message is constructed that lists the differences between the sets. This method is used by default when comparing sets or frozensets with [`assertEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual").
Fails if either of _first_ or _second_ does not have a [`difference()`](https://docs.python.org/3/library/stdtypes.html#frozenset.difference "frozenset.difference") method.
Added in version 3.1.

assertDictEqual(_first_ , _second_ , _msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertDictEqual "Link to this definition")

Test that two dictionaries are equal. If not, an error message is constructed that shows the differences in the dictionaries. This method will be used by default to compare dictionaries in calls to [`assertEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual").
Added in version 3.1.
Finally the `TestCase` provides the following methods and attributes:

fail(_msg =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.fail "Link to this definition")

Signals a test failure unconditionally, with _msg_ or `None` for the error message.

failureException[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.failureException "Link to this definition")

This class attribute gives the exception raised by the test method. If a test framework needs to use a specialized exception, possibly to carry additional information, it must subclass this exception in order to “play fair” with the framework. The initial value of this attribute is [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError").

longMessage[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.longMessage "Link to this definition")

This class attribute determines what happens when a custom failure message is passed as the msg argument to an assertXYY call that fails. `True` is the default value. In this case, the custom message is appended to the end of the standard failure message. When set to `False`, the custom message replaces the standard message.
The class setting can be overridden in individual test methods by assigning an instance attribute, self.longMessage, to `True` or `False` before calling the assert methods.
The class setting gets reset before each test call.
Added in version 3.1.

maxDiff[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.maxDiff "Link to this definition")

This attribute controls the maximum length of diffs output by assert methods that report diffs on failure. It defaults to 80*8 characters. Assert methods affected by this attribute are [`assertSequenceEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertSequenceEqual "unittest.TestCase.assertSequenceEqual") (including all the sequence comparison methods that delegate to it), [`assertDictEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertDictEqual "unittest.TestCase.assertDictEqual") and [`assertMultiLineEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertMultiLineEqual "unittest.TestCase.assertMultiLineEqual").
Setting `maxDiff` to `None` means that there is no maximum length of diffs.
Added in version 3.2.
Testing frameworks can use the following methods to collect information on the test:

countTestCases()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.countTestCases "Link to this definition")

Return the number of tests represented by this test object. For `TestCase` instances, this will always be `1`.

defaultTestResult()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.defaultTestResult "Link to this definition")

Return an instance of the test result class that should be used for this test case class (if no other result instance is provided to the [`run()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.run "unittest.TestCase.run") method).
For `TestCase` instances, this will always be an instance of [`TestResult`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult"); subclasses of `TestCase` should override this as necessary.

id()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.id "Link to this definition")

Return a string identifying the specific test case. This is usually the full name of the test method, including the module and class name.

shortDescription()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.shortDescription "Link to this definition")

Returns a description of the test, or `None` if no description has been provided. The default implementation of this method returns the first line of the test method’s docstring, if available, or `None`.
Changed in version 3.1: In 3.1 this was changed to add the test name to the short description even in the presence of a docstring. This caused compatibility issues with unittest extensions and adding the test name was moved to the [`TextTestResult`](https://docs.python.org/3/library/unittest.html#unittest.TextTestResult "unittest.TextTestResult") in Python 3.2.

addCleanup(_function_ , _/_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addCleanup "Link to this definition")

Add a function to be called after [`tearDown()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown") to cleanup resources used during the test. Functions will be called in reverse order to the order they are added (LIFO). They are called with any arguments and keyword arguments passed into `addCleanup()` when they are added.
If [`setUp()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") fails, meaning that [`tearDown()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown") is not called, then any cleanup functions added will still be called.
Added in version 3.1.

enterContext(_cm_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.enterContext "Link to this definition")

Enter the supplied [context manager](https://docs.python.org/3/glossary.html#term-context-manager). If successful, also add its [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__") method as a cleanup function by [`addCleanup()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addCleanup "unittest.TestCase.addCleanup") and return the result of the [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__") method.
Added in version 3.11.

doCleanups()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.doCleanups "Link to this definition")

This method is called unconditionally after [`tearDown()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown"), or after [`setUp()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") if `setUp()` raises an exception.
It is responsible for calling all the cleanup functions added by [`addCleanup()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addCleanup "unittest.TestCase.addCleanup"). If you need cleanup functions to be called _prior_ to [`tearDown()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown") then you can call `doCleanups()` yourself.
`doCleanups()` pops methods off the stack of cleanup functions one at a time, so it can be called at any time.
Added in version 3.1.

_classmethod_ addClassCleanup(_function_ , _/_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addClassCleanup "Link to this definition")

Add a function to be called after [`tearDownClass()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDownClass "unittest.TestCase.tearDownClass") to cleanup resources used during the test class. Functions will be called in reverse order to the order they are added (LIFO). They are called with any arguments and keyword arguments passed into `addClassCleanup()` when they are added.
If [`setUpClass()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUpClass "unittest.TestCase.setUpClass") fails, meaning that [`tearDownClass()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDownClass "unittest.TestCase.tearDownClass") is not called, then any cleanup functions added will still be called.
Added in version 3.8.

_classmethod_ enterClassContext(_cm_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.enterClassContext "Link to this definition")

Enter the supplied [context manager](https://docs.python.org/3/glossary.html#term-context-manager). If successful, also add its [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__") method as a cleanup function by [`addClassCleanup()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addClassCleanup "unittest.TestCase.addClassCleanup") and return the result of the [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__") method.
Added in version 3.11.

_classmethod_ doClassCleanups()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestCase.doClassCleanups "Link to this definition")

This method is called unconditionally after [`tearDownClass()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDownClass "unittest.TestCase.tearDownClass"), or after [`setUpClass()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUpClass "unittest.TestCase.setUpClass") if `setUpClass()` raises an exception.
It is responsible for calling all the cleanup functions added by [`addClassCleanup()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.addClassCleanup "unittest.TestCase.addClassCleanup"). If you need cleanup functions to be called _prior_ to [`tearDownClass()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDownClass "unittest.TestCase.tearDownClass") then you can call `doClassCleanups()` yourself.
`doClassCleanups()` pops methods off the stack of cleanup functions one at a time, so it can be called at any time.
Added in version 3.8.

_class_ unittest.IsolatedAsyncioTestCase(_methodName ='runTest'_)[¶](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase "Link to this definition")

This class provides an API similar to [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") and also accepts coroutines as test functions.
Added in version 3.8.

loop_factory[¶](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.loop_factory "Link to this definition")

The _loop_factory_ passed to [`asyncio.Runner`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.Runner "asyncio.Runner"). Override in subclasses with [`asyncio.EventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.EventLoop "asyncio.EventLoop") to avoid using the asyncio policy system.
Added in version 3.13.

_async_ asyncSetUp()[¶](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.asyncSetUp "Link to this definition")

Method called to prepare the test fixture. This is called after [`TestCase.setUp()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp"). This is called immediately before calling the test method; other than [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError") or [`SkipTest`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest"), any exception raised by this method will be considered an error rather than a test failure. The default implementation does nothing.

_async_ asyncTearDown()[¶](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.asyncTearDown "Link to this definition")

Method called immediately after the test method has been called and the result recorded. This is called before [`tearDown()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown"). This is called even if the test method raised an exception, so the implementation in subclasses may need to be particularly careful about checking internal state. Any exception, other than [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError") or [`SkipTest`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest"), raised by this method will be considered an additional error rather than a test failure (thus increasing the total number of reported errors). This method will only be called if the [`asyncSetUp()`](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.asyncSetUp "unittest.IsolatedAsyncioTestCase.asyncSetUp") succeeds, regardless of the outcome of the test method. The default implementation does nothing.

addAsyncCleanup(_function_ , _/_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.addAsyncCleanup "Link to this definition")
