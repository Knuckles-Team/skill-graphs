
This method accepts a coroutine that can be used as a cleanup function.

_async_ enterAsyncContext(_cm_)[¶](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.enterAsyncContext "Link to this definition")

Enter the supplied [asynchronous context manager](https://docs.python.org/3/glossary.html#term-asynchronous-context-manager). If successful, also add its [`__aexit__()`](https://docs.python.org/3/reference/datamodel.html#object.__aexit__ "object.__aexit__") method as a cleanup function by [`addAsyncCleanup()`](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.addAsyncCleanup "unittest.IsolatedAsyncioTestCase.addAsyncCleanup") and return the result of the [`__aenter__()`](https://docs.python.org/3/reference/datamodel.html#object.__aenter__ "object.__aenter__") method.
Added in version 3.11.

run(_result =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.run "Link to this definition")

Sets up a new event loop to run the test, collecting the result into the [`TestResult`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") object passed as _result_. If _result_ is omitted or `None`, a temporary result object is created (by calling the [`defaultTestResult()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.defaultTestResult "unittest.TestCase.defaultTestResult") method) and used. The result object is returned to `run()`’s caller. At the end of the test all the tasks in the event loop are cancelled.
An example illustrating the order:
Copy```
from unittest import IsolatedAsyncioTestCase

events = []


class Test(IsolatedAsyncioTestCase):


    def setUp(self):
        events.append("setUp")

    async def asyncSetUp(self):
        self._async_connection = await AsyncConnection()
        events.append("asyncSetUp")

    async def test_response(self):
        events.append("test_response")
        response = await self._async_connection.get("https://example.com")
        self.assertEqual(response.status_code, 200)
        self.addAsyncCleanup(self.on_cleanup)

    def tearDown(self):
        events.append("tearDown")

    async def asyncTearDown(self):
        await self._async_connection.close()
        events.append("asyncTearDown")

    async def on_cleanup(self):
        events.append("cleanup")

if __name__ == "__main__":
    unittest.main()

```

After running the test, `events` would contain `["setUp", "asyncSetUp", "test_response", "asyncTearDown", "tearDown", "cleanup"]`.

_class_ unittest.FunctionTestCase(_testFunc_ , _setUp =None_, _tearDown =None_, _description =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.FunctionTestCase "Link to this definition")

This class implements the portion of the [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") interface which allows the test runner to drive the test, but does not provide the methods which test code can use to check and report errors. This is used to create test cases using legacy test code, allowing it to be integrated into a `unittest`-based test framework.
### Grouping tests[¶](https://docs.python.org/3/library/unittest.html#grouping-tests "Link to this heading")

_class_ unittest.TestSuite(_tests =()_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "Link to this definition")

This class represents an aggregation of individual test cases and test suites. The class presents the interface needed by the test runner to allow it to be run as any other test case. Running a `TestSuite` instance is the same as iterating over the suite, running each test individually.
If _tests_ is given, it must be an iterable of individual test cases or other test suites that will be used to build the suite initially. Additional methods are provided to add test cases and suites to the collection later on.
`TestSuite` objects behave much like [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") objects, except they do not actually implement a test. Instead, they are used to aggregate tests into groups of tests that should be run together. Some additional methods are available to add tests to `TestSuite` instances:

addTest(_test_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.addTest "Link to this definition")

Add a [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") or `TestSuite` to the suite.

addTests(_tests_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.addTests "Link to this definition")

Add all the tests from an iterable of [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") and `TestSuite` instances to this test suite.
This is equivalent to iterating over _tests_ , calling [`addTest()`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.addTest "unittest.TestSuite.addTest") for each element.
`TestSuite` shares the following methods with [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase"):

run(_result_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.run "Link to this definition")

Run the tests associated with this suite, collecting the result into the test result object passed as _result_. Note that unlike [`TestCase.run()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.run "unittest.TestCase.run"), `TestSuite.run()` requires the result object to be passed in.

debug()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.debug "Link to this definition")

Run the tests associated with this suite without collecting the result. This allows exceptions raised by the test to be propagated to the caller and can be used to support running tests under a debugger.

countTestCases()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.countTestCases "Link to this definition")

Return the number of tests represented by this test object, including all individual tests and sub-suites.

__iter__()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.__iter__ "Link to this definition")

Tests grouped by a `TestSuite` are always accessed by iteration. Subclasses can lazily provide tests by overriding `__iter__()`. Note that this method may be called several times on a single suite (for example when counting tests or comparing for equality) so the tests returned by repeated iterations before [`TestSuite.run()`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.run "unittest.TestSuite.run") must be the same for each call iteration. After `TestSuite.run()`, callers should not rely on the tests returned by this method unless the caller uses a subclass that overrides `TestSuite._removeTestAtIndex()` to preserve test references.
Changed in version 3.2: In earlier versions the `TestSuite` accessed tests directly rather than through iteration, so overriding `__iter__()` wasn’t sufficient for providing tests.
Changed in version 3.4: In earlier versions the `TestSuite` held references to each [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") after [`TestSuite.run()`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.run "unittest.TestSuite.run"). Subclasses can restore that behavior by overriding `TestSuite._removeTestAtIndex()`.
In the typical usage of a `TestSuite` object, the [`run()`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite.run "unittest.TestSuite.run") method is invoked by a `TestRunner` rather than by the end-user test harness.
### Loading and running tests[¶](https://docs.python.org/3/library/unittest.html#loading-and-running-tests "Link to this heading")

_class_ unittest.TestLoader[¶](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "Link to this definition")

The `TestLoader` class is used to create test suites from classes and modules. Normally, there is no need to create an instance of this class; the `unittest` module provides an instance that can be shared as [`unittest.defaultTestLoader`](https://docs.python.org/3/library/unittest.html#unittest.defaultTestLoader "unittest.defaultTestLoader"). Using a subclass or instance, however, allows customization of some configurable properties.
`TestLoader` objects have the following attributes:

errors[¶](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.errors "Link to this definition")

A list of the non-fatal errors encountered while loading tests. Not reset by the loader at any point. Fatal errors are signalled by the relevant method raising an exception to the caller. Non-fatal errors are also indicated by a synthetic test that will raise the original error when run.
Added in version 3.5.
`TestLoader` objects have the following methods:

loadTestsFromTestCase(_testCaseClass_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromTestCase "Link to this definition")

Return a suite of all test cases contained in the [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase")-derived `testCaseClass`.
A test case instance is created for each method named by [`getTestCaseNames()`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.getTestCaseNames "unittest.TestLoader.getTestCaseNames"). By default these are the method names beginning with `test`. If `getTestCaseNames()` returns no methods, but the `runTest()` method is implemented, a single test case is created for that method instead.

loadTestsFromModule(_module_ , _*_ , _pattern =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromModule "Link to this definition")

Return a suite of all test cases contained in the given module. This method searches _module_ for classes derived from [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") and creates an instance of the class for each test method defined for the class.
Note
While using a hierarchy of [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase")-derived classes can be convenient in sharing fixtures and helper functions, defining test methods on base classes that are not intended to be instantiated directly does not play well with this method. Doing so, however, can be useful when the fixtures are different and defined in subclasses.
If a module provides a `load_tests` function it will be called to load the tests. This allows modules to customize test loading. This is the [load_tests protocol](https://docs.python.org/3/library/unittest.html#id1). The _pattern_ argument is passed as the third argument to `load_tests`.
Changed in version 3.2: Support for `load_tests` added.
Changed in version 3.5: Support for a keyword-only argument _pattern_ has been added.
Changed in version 3.12: The undocumented and unofficial _use_load_tests_ parameter has been removed.

loadTestsFromName(_name_ , _module =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromName "Link to this definition")

Return a suite of all test cases given a string specifier.
The specifier _name_ is a “dotted name” that may resolve either to a module, a test case class, a test method within a test case class, a [`TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") instance, or a callable object which returns a [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") or `TestSuite` instance. These checks are applied in the order listed here; that is, a method on a possible test case class will be picked up as “a test method within a test case class”, rather than “a callable object”.
For example, if you have a module `SampleTests` containing a [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase")-derived class `SampleTestCase` with three test methods (`test_one()`, `test_two()`, and `test_three()`), the specifier `'SampleTests.SampleTestCase'` would cause this method to return a suite which will run all three test methods. Using the specifier `'SampleTests.SampleTestCase.test_two'` would cause it to return a test suite which will run only the `test_two()` test method. The specifier can refer to modules and packages which have not been imported; they will be imported as a side-effect.
The method optionally resolves _name_ relative to the given _module_.
Changed in version 3.5: If an [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") or [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") occurs while traversing _name_ then a synthetic test that raises that error when run will be returned. These errors are included in the errors accumulated by self.errors.

loadTestsFromNames(_names_ , _module =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromNames "Link to this definition")

Similar to [`loadTestsFromName()`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromName "unittest.TestLoader.loadTestsFromName"), but takes a sequence of names rather than a single name. The return value is a test suite which supports all the tests defined for each name.

getTestCaseNames(_testCaseClass_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.getTestCaseNames "Link to this definition")

Return a sorted sequence of method names found within _testCaseClass_ ; this should be a subclass of [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase").

discover(_start_dir_ , _pattern ='test*.py'_, _top_level_dir =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.discover "Link to this definition")

Find all the test modules by recursing into subdirectories from the specified start directory, and return a TestSuite object containing them. Only test files that match _pattern_ will be loaded. (Using shell style pattern matching.) Only module names that are importable (i.e. are valid Python identifiers) will be loaded.
All test modules must be importable from the top level of the project. If the start directory is not the top level directory then _top_level_dir_ must be specified separately.
If importing a module fails, for example due to a syntax error, then this will be recorded as a single error and discovery will continue. If the import failure is due to [`SkipTest`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest") being raised, it will be recorded as a skip instead of an error.
If a package (a directory containing a file named `__init__.py`) is found, the package will be checked for a `load_tests` function. If this exists then it will be called `package.load_tests(loader, tests, pattern)`. Test discovery takes care to ensure that a package is only checked for tests once during an invocation, even if the load_tests function itself calls `loader.discover`.
If `load_tests` exists then discovery does _not_ recurse into the package, `load_tests` is responsible for loading all tests in the package.
The pattern is deliberately not stored as a loader attribute so that packages can continue discovery themselves.
_top_level_dir_ is stored internally, and used as a default to any nested calls to `discover()`. That is, if a package’s `load_tests` calls `loader.discover()`, it does not need to pass this argument.
_start_dir_ can be a dotted module name as well as a directory.
Added in version 3.2.
Changed in version 3.4: Modules that raise [`SkipTest`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest") on import are recorded as skips, not errors.
_start_dir_ can be a [namespace packages](https://docs.python.org/3/glossary.html#term-namespace-package).
Paths are sorted before being imported so that execution order is the same even if the underlying file system’s ordering is not dependent on file name.
Changed in version 3.5: Found packages are now checked for `load_tests` regardless of whether their path matches _pattern_ , because it is impossible for a package name to match the default pattern.
Changed in version 3.11: _start_dir_ can not be a [namespace packages](https://docs.python.org/3/glossary.html#term-namespace-package). It has been broken since Python 3.7, and Python 3.11 officially removes it.
Changed in version 3.13: _top_level_dir_ is only stored for the duration of _discover_ call.
Changed in version 3.14: _start_dir_ can once again be a [namespace package](https://docs.python.org/3/glossary.html#term-namespace-package).
The following attributes of a `TestLoader` can be configured either by subclassing or assignment on an instance:

testMethodPrefix[¶](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.testMethodPrefix "Link to this definition")

String giving the prefix of method names which will be interpreted as test methods. The default value is `'test'`.
This affects [`getTestCaseNames()`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.getTestCaseNames "unittest.TestLoader.getTestCaseNames") and all the `loadTestsFrom*` methods.

sortTestMethodsUsing[¶](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.sortTestMethodsUsing "Link to this definition")

Function to be used to compare method names when sorting them in [`getTestCaseNames()`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.getTestCaseNames "unittest.TestLoader.getTestCaseNames") and all the `loadTestsFrom*` methods.

suiteClass[¶](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.suiteClass "Link to this definition")

Callable object that constructs a test suite from a list of tests. No methods on the resulting object are needed. The default value is the [`TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") class.
This affects all the `loadTestsFrom*` methods.

testNamePatterns[¶](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.testNamePatterns "Link to this definition")

List of Unix shell-style wildcard test name patterns that test methods have to match to be included in test suites (see `-k` option).
If this attribute is not `None` (the default), all test methods to be included in test suites must match one of the patterns in this list. Note that matches are always performed using [`fnmatch.fnmatchcase()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatchcase "fnmatch.fnmatchcase"), so unlike patterns passed to the `-k` option, simple substring patterns will have to be converted using `*` wildcards.
This affects all the `loadTestsFrom*` methods.
Added in version 3.7.

_class_ unittest.TestResult[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult "Link to this definition")

This class is used to compile information about which tests have succeeded and which have failed.
A `TestResult` object stores the results of a set of tests. The [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") and [`TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") classes ensure that results are properly recorded; test authors do not need to worry about recording the outcome of tests.
Testing frameworks built on top of `unittest` may want access to the `TestResult` object generated by running a set of tests for reporting purposes; a `TestResult` instance is returned by the `TestRunner.run()` method for this purpose.
`TestResult` instances have the following attributes that will be of interest when inspecting the results of running a set of tests:

errors[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.errors "Link to this definition")

A list containing 2-tuples of [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instances and strings holding formatted tracebacks. Each tuple represents a test which raised an unexpected exception.

failures[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.failures "Link to this definition")

A list containing 2-tuples of [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instances and strings holding formatted tracebacks. Each tuple represents a test where a failure was explicitly signalled using the [assert* methods](https://docs.python.org/3/library/unittest.html#assert-methods).

skipped[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.skipped "Link to this definition")

A list containing 2-tuples of [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instances and strings holding the reason for skipping the test.
Added in version 3.1.

expectedFailures[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.expectedFailures "Link to this definition")

A list containing 2-tuples of [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instances and strings holding formatted tracebacks. Each tuple represents an expected failure or error of the test case.

unexpectedSuccesses[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.unexpectedSuccesses "Link to this definition")

A list containing [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instances that were marked as expected failures, but succeeded.

collectedDurations[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.collectedDurations "Link to this definition")

A list containing 2-tuples of test case names and floats representing the elapsed time of each test which was run.
Added in version 3.12.

shouldStop[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.shouldStop "Link to this definition")

Set to `True` when the execution of tests should stop by [`stop()`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.stop "unittest.TestResult.stop").

testsRun[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.testsRun "Link to this definition")

The total number of tests run so far.

buffer[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.buffer "Link to this definition")

If set to true, `sys.stdout` and `sys.stderr` will be buffered in between [`startTest()`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.startTest "unittest.TestResult.startTest") and [`stopTest()`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.stopTest "unittest.TestResult.stopTest") being called. Collected output will only be echoed onto the real `sys.stdout` and `sys.stderr` if the test fails or errors. Any output is also attached to the failure / error message.
Added in version 3.2.

failfast[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.failfast "Link to this definition")

If set to true [`stop()`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.stop "unittest.TestResult.stop") will be called on the first failure or error, halting the test run.
Added in version 3.2.

tb_locals[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.tb_locals "Link to this definition")

If set to true then local variables will be shown in tracebacks.
Added in version 3.5.

wasSuccessful()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.wasSuccessful "Link to this definition")

Return `True` if all tests run so far have passed, otherwise returns `False`.
Changed in version 3.4: Returns `False` if there were any [`unexpectedSuccesses`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.unexpectedSuccesses "unittest.TestResult.unexpectedSuccesses") from tests marked with the [`expectedFailure()`](https://docs.python.org/3/library/unittest.html#unittest.expectedFailure "unittest.expectedFailure") decorator.

stop()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.stop "Link to this definition")

This method can be called to signal that the set of tests being run should be aborted by setting the [`shouldStop`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.shouldStop "unittest.TestResult.shouldStop") attribute to `True`. `TestRunner` objects should respect this flag and return without running any additional tests.
For example, this feature is used by the [`TextTestRunner`](https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner "unittest.TextTestRunner") class to stop the test framework when the user signals an interrupt from the keyboard. Interactive tools which provide `TestRunner` implementations can use this in a similar manner.
The following methods of the `TestResult` class are used to maintain the internal data structures, and may be extended in subclasses to support additional reporting requirements. This is particularly useful in building tools which support interactive reporting while tests are being run.
