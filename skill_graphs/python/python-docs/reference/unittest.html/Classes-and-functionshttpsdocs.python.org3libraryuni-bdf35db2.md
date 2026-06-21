
startTest(_test_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.startTest "Link to this definition")

Called when the test case _test_ is about to be run.

stopTest(_test_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.stopTest "Link to this definition")

Called after the test case _test_ has been executed, regardless of the outcome.

startTestRun()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.startTestRun "Link to this definition")

Called once before any tests are executed.
Added in version 3.1.

stopTestRun()[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.stopTestRun "Link to this definition")

Called once after all tests are executed.
Added in version 3.1.

addError(_test_ , _err_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.addError "Link to this definition")

Called when the test case _test_ raises an unexpected exception. _err_ is a tuple of the form returned by [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info"): `(type, value, traceback)`.
The default implementation appends a tuple `(test, formatted_err)` to the instance’s [`errors`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.errors "unittest.TestResult.errors") attribute, where _formatted_err_ is a formatted traceback derived from _err_.

addFailure(_test_ , _err_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.addFailure "Link to this definition")

Called when the test case _test_ signals a failure. _err_ is a tuple of the form returned by [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info"): `(type, value, traceback)`.
The default implementation appends a tuple `(test, formatted_err)` to the instance’s [`failures`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.failures "unittest.TestResult.failures") attribute, where _formatted_err_ is a formatted traceback derived from _err_.

addSuccess(_test_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.addSuccess "Link to this definition")

Called when the test case _test_ succeeds.
The default implementation does nothing.

addSkip(_test_ , _reason_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.addSkip "Link to this definition")

Called when the test case _test_ is skipped. _reason_ is the reason the test gave for skipping.
The default implementation appends a tuple `(test, reason)` to the instance’s [`skipped`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.skipped "unittest.TestResult.skipped") attribute.

addExpectedFailure(_test_ , _err_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.addExpectedFailure "Link to this definition")

Called when the test case _test_ fails or errors, but was marked with the [`expectedFailure()`](https://docs.python.org/3/library/unittest.html#unittest.expectedFailure "unittest.expectedFailure") decorator.
The default implementation appends a tuple `(test, formatted_err)` to the instance’s [`expectedFailures`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.expectedFailures "unittest.TestResult.expectedFailures") attribute, where _formatted_err_ is a formatted traceback derived from _err_.

addUnexpectedSuccess(_test_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.addUnexpectedSuccess "Link to this definition")

Called when the test case _test_ was marked with the [`expectedFailure()`](https://docs.python.org/3/library/unittest.html#unittest.expectedFailure "unittest.expectedFailure") decorator, but succeeded.
The default implementation appends the test to the instance’s [`unexpectedSuccesses`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.unexpectedSuccesses "unittest.TestResult.unexpectedSuccesses") attribute.

addSubTest(_test_ , _subtest_ , _outcome_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.addSubTest "Link to this definition")

Called when a subtest finishes. _test_ is the test case corresponding to the test method. _subtest_ is a custom [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instance describing the subtest.
If _outcome_ is [`None`](https://docs.python.org/3/library/constants.html#None "None"), the subtest succeeded. Otherwise, it failed with an exception where _outcome_ is a tuple of the form returned by [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info"): `(type, value, traceback)`.
The default implementation does nothing when the outcome is a success, and records subtest failures as normal failures.
Added in version 3.4.

addDuration(_test_ , _elapsed_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TestResult.addDuration "Link to this definition")

Called when the test case finishes. _elapsed_ is the time represented in seconds, and it includes the execution of cleanup functions.
Added in version 3.12.

_class_ unittest.TextTestResult(_stream_ , _descriptions_ , _verbosity_ , _*_ , _durations =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TextTestResult "Link to this definition")

A concrete implementation of [`TestResult`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") used by the [`TextTestRunner`](https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner "unittest.TextTestRunner"). Subclasses should accept `**kwargs` to ensure compatibility as the interface changes.
Added in version 3.2.
Changed in version 3.12: Added the _durations_ keyword parameter.

unittest.defaultTestLoader[¶](https://docs.python.org/3/library/unittest.html#unittest.defaultTestLoader "Link to this definition")

Instance of the [`TestLoader`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "unittest.TestLoader") class intended to be shared. If no customization of the `TestLoader` is needed, this instance can be used instead of repeatedly creating new instances.

_class_ unittest.TextTestRunner(_stream =None_, _descriptions =True_, _verbosity =1_, _failfast =False_, _buffer =False_, _resultclass =None_, _warnings =None_, _*_ , _tb_locals =False_, _durations =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner "Link to this definition")

A basic test runner implementation that outputs results to a stream. If _stream_ is `None`, the default, [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") is used as the output stream. This class has a few configurable parameters, but is essentially very simple. Graphical applications which run test suites should provide alternate implementations. Such implementations should accept `**kwargs` as the interface to construct runners changes when features are added to unittest.
By default this runner shows [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning"), [`PendingDeprecationWarning`](https://docs.python.org/3/library/exceptions.html#PendingDeprecationWarning "PendingDeprecationWarning"), [`ResourceWarning`](https://docs.python.org/3/library/exceptions.html#ResourceWarning "ResourceWarning") and [`ImportWarning`](https://docs.python.org/3/library/exceptions.html#ImportWarning "ImportWarning") even if they are [ignored by default](https://docs.python.org/3/library/warnings.html#warning-ignored). This behavior can be overridden using Python’s `-Wd` or `-Wa` options (see [Warning control](https://docs.python.org/3/using/cmdline.html#using-on-warnings)) and leaving _warnings_ to `None`.
Changed in version 3.2: Added the _warnings_ parameter.
Changed in version 3.2: The default stream is set to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") at instantiation time rather than import time.
Changed in version 3.5: Added the _tb_locals_ parameter.
Changed in version 3.12: Added the _durations_ parameter.

_makeResult()[¶](https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner._makeResult "Link to this definition")

This method returns the instance of `TestResult` used by [`run()`](https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner.run "unittest.TextTestRunner.run"). It is not intended to be called directly, but can be overridden in subclasses to provide a custom `TestResult`.
`_makeResult()` instantiates the class or callable passed in the `TextTestRunner` constructor as the `resultclass` argument. It defaults to [`TextTestResult`](https://docs.python.org/3/library/unittest.html#unittest.TextTestResult "unittest.TextTestResult") if no `resultclass` is provided. The result class is instantiated with the following arguments:
Copy```
stream, descriptions, verbosity

```


run(_test_)[¶](https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner.run "Link to this definition")

This method is the main public interface to the `TextTestRunner`. This method takes a [`TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") or [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") instance. A [`TestResult`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") is created by calling [`_makeResult()`](https://docs.python.org/3/library/unittest.html#unittest.TextTestRunner._makeResult "unittest.TextTestRunner._makeResult") and the test(s) are run and the results printed to stdout.

unittest.main(_module ='__main__'_, _defaultTest =None_, _argv =None_, _testRunner =None_, _testLoader =unittest.defaultTestLoader_, _exit =True_, _verbosity =1_, _failfast =None_, _catchbreak =None_, _buffer =None_, _warnings =None_)[¶](https://docs.python.org/3/library/unittest.html#unittest.main "Link to this definition")

A command-line program that loads a set of tests from _module_ and runs them; this is primarily for making test modules conveniently executable. The simplest use for this function is to include the following line at the end of a test script:
Copy```
if __name__ == '__main__':
    unittest.main()

```

You can run tests with more detailed information by passing in the verbosity argument:
Copy```
if __name__ == '__main__':
    unittest.main(verbosity=2)

```

The _defaultTest_ argument is either the name of a single test or an iterable of test names to run if no test names are specified via _argv_. If not specified or `None` and no test names are provided via _argv_ , all tests found in _module_ are run.
The _argv_ argument can be a list of options passed to the program, with the first element being the program name. If not specified or `None`, the values of [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv") are used.
The _testRunner_ argument can either be a test runner class or an already created instance of it. By default `main` calls [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit") with an exit code indicating success (0) or failure (1) of the tests run. An exit code of 5 indicates that no tests were run or skipped.
The _testLoader_ argument has to be a [`TestLoader`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "unittest.TestLoader") instance, and defaults to [`defaultTestLoader`](https://docs.python.org/3/library/unittest.html#unittest.defaultTestLoader "unittest.defaultTestLoader").
`main` supports being used from the interactive interpreter by passing in the argument `exit=False`. This displays the result on standard output without calling [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit"):
Copy```
>>> from unittest import main
>>> main(module='test_module', exit=False)

```

The _failfast_ , _catchbreak_ and _buffer_ parameters have the same effect as the same-name [command-line options](https://docs.python.org/3/library/unittest.html#command-line-options).
The _warnings_ argument specifies the [warning filter](https://docs.python.org/3/library/warnings.html#warning-filter) that should be used while running the tests. If it’s not specified, it will remain `None` if a `-W` option is passed to **python** (see [Warning control](https://docs.python.org/3/using/cmdline.html#using-on-warnings)), otherwise it will be set to `'default'`.
Calling `main` returns an object with the `result` attribute that contains the result of the tests run as a [`unittest.TestResult`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult").
Changed in version 3.1: The _exit_ parameter was added.
Changed in version 3.2: The _verbosity_ , _failfast_ , _catchbreak_ , _buffer_ and _warnings_ parameters were added.
Changed in version 3.4: The _defaultTest_ parameter was changed to also accept an iterable of test names.
#### load_tests Protocol[¶](https://docs.python.org/3/library/unittest.html#load-tests-protocol "Link to this heading")
Added in version 3.2.
Modules or packages can customize how tests are loaded from them during normal test runs or test discovery by implementing a function called `load_tests`.
If a test module defines `load_tests` it will be called by [`TestLoader.loadTestsFromModule()`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromModule "unittest.TestLoader.loadTestsFromModule") with the following arguments:
Copy```
load_tests(loader, standard_tests, pattern)

```

where _pattern_ is passed straight through from `loadTestsFromModule`. It defaults to `None`.
It should return a [`TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite").
_loader_ is the instance of [`TestLoader`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "unittest.TestLoader") doing the loading. _standard_tests_ are the tests that would be loaded by default from the module. It is common for test modules to only want to add or remove tests from the standard set of tests. The third argument is used when loading packages as part of test discovery.
A typical `load_tests` function that loads tests from a specific set of [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") classes may look like:
Copy```
test_cases = (TestCase1, TestCase2, TestCase3)

def load_tests(loader, tests, pattern):
    suite = TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite

```

If discovery is started in a directory containing a package, either from the command line or by calling [`TestLoader.discover()`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.discover "unittest.TestLoader.discover"), then the package `__init__.py` will be checked for `load_tests`. If that function does not exist, discovery will recurse into the package as though it were just another directory. Otherwise, discovery of the package’s tests will be left up to `load_tests` which is called with the following arguments:
Copy```
load_tests(loader, standard_tests, pattern)

```

This should return a [`TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") representing all the tests from the package. (`standard_tests` will only contain tests collected from `__init__.py`.)
Because the pattern is passed into `load_tests` the package is free to continue (and potentially modify) test discovery. A ‘do nothing’ `load_tests` function for a test package would look like:
Copy```
def load_tests(loader, standard_tests, pattern):
    # top level directory cached on loader instance
    this_dir = os.path.dirname(__file__)
    package_tests = loader.discover(start_dir=this_dir, pattern=pattern)
    standard_tests.addTests(package_tests)
    return standard_tests

```

Changed in version 3.5: Discovery no longer checks package names for matching _pattern_ due to the impossibility of package names matching the default pattern.
## Class and Module Fixtures[¶](https://docs.python.org/3/library/unittest.html#class-and-module-fixtures "Link to this heading")
Class and module level fixtures are implemented in [`TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite"). When the test suite encounters a test from a new class then [`tearDownClass()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDownClass "unittest.TestCase.tearDownClass") from the previous class (if there is one) is called, followed by [`setUpClass()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUpClass "unittest.TestCase.setUpClass") from the new class.
Similarly if a test is from a different module from the previous test then `tearDownModule` from the previous module is run, followed by `setUpModule` from the new module.
After all the tests have run the final `tearDownClass` and `tearDownModule` are run.
Note that shared fixtures do not play well with [potential] features like test parallelization and they break test isolation. They should be used with care.
The default ordering of tests created by the unittest test loaders is to group all tests from the same modules and classes together. This will lead to `setUpClass` / `setUpModule` (etc) being called exactly once per class and module. If you randomize the order, so that tests from different modules and classes are adjacent to each other, then these shared fixture functions may be called multiple times in a single test run.
Shared fixtures are not intended to work with suites with non-standard ordering. A `BaseTestSuite` still exists for frameworks that don’t want to support shared fixtures.
If there are any exceptions raised during one of the shared fixture functions the test is reported as an error. Because there is no corresponding test instance an `_ErrorHolder` object (that has the same interface as a [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase")) is created to represent the error. If you are just using the standard unittest test runner then this detail doesn’t matter, but if you are a framework author it may be relevant.
### setUpClass and tearDownClass[¶](https://docs.python.org/3/library/unittest.html#setupclass-and-teardownclass "Link to this heading")
These must be implemented as class methods:
Copy```
import unittest

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._connection = createExpensiveConnectionObject()

    @classmethod
    def tearDownClass(cls):
        cls._connection.destroy()

```

If you want the `setUpClass` and `tearDownClass` on base classes called then you must call up to them yourself. The implementations in [`TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase") are empty.
If an exception is raised during a `setUpClass` then the tests in the class are not run and the `tearDownClass` is not run. Skipped classes will not have `setUpClass` or `tearDownClass` run. If the exception is a [`SkipTest`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest") exception then the class will be reported as having been skipped instead of as an error.
### setUpModule and tearDownModule[¶](https://docs.python.org/3/library/unittest.html#setupmodule-and-teardownmodule "Link to this heading")
Copy```
def setUpModule():
    createConnection()

def tearDownModule():
    closeConnection()

```

If an exception is raised in a `setUpModule` then none of the tests in the module will be run and the `tearDownModule` will not be run. If the exception is a [`SkipTest`](https://docs.python.org/3/library/unittest.html#unittest.SkipTest "unittest.SkipTest") exception then the module will be reported as having been skipped instead of as an error.
To add cleanup code that must be run even in the case of an exception, use `addModuleCleanup`:

unittest.addModuleCleanup(_function_ , _/_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/unittest.html#unittest.addModuleCleanup "Link to this definition")

Add a function to be called after [`tearDownModule()`](https://docs.python.org/3/library/unittest.html#unittest.tearDownModule "unittest.tearDownModule") to cleanup resources used during the test class. Functions will be called in reverse order to the order they are added (LIFO). They are called with any arguments and keyword arguments passed into [`addModuleCleanup()`](https://docs.python.org/3/library/unittest.html#unittest.addModuleCleanup "unittest.addModuleCleanup") when they are added.
If [`setUpModule()`](https://docs.python.org/3/library/unittest.html#unittest.setUpModule "unittest.setUpModule") fails, meaning that [`tearDownModule()`](https://docs.python.org/3/library/unittest.html#unittest.tearDownModule "unittest.tearDownModule") is not called, then any cleanup functions added will still be called.
Added in version 3.8.

unittest.enterModuleContext(_cm_)[¶](https://docs.python.org/3/library/unittest.html#unittest.enterModuleContext "Link to this definition")

Enter the supplied [context manager](https://docs.python.org/3/glossary.html#term-context-manager). If successful, also add its [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__") method as a cleanup function by [`addModuleCleanup()`](https://docs.python.org/3/library/unittest.html#unittest.addModuleCleanup "unittest.addModuleCleanup") and return the result of the [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__") method.
Added in version 3.11.

unittest.doModuleCleanups()[¶](https://docs.python.org/3/library/unittest.html#unittest.doModuleCleanups "Link to this definition")

This function is called unconditionally after [`tearDownModule()`](https://docs.python.org/3/library/unittest.html#unittest.tearDownModule "unittest.tearDownModule"), or after [`setUpModule()`](https://docs.python.org/3/library/unittest.html#unittest.setUpModule "unittest.setUpModule") if `setUpModule()` raises an exception.
It is responsible for calling all the cleanup functions added by [`addModuleCleanup()`](https://docs.python.org/3/library/unittest.html#unittest.addModuleCleanup "unittest.addModuleCleanup"). If you need cleanup functions to be called _prior_ to [`tearDownModule()`](https://docs.python.org/3/library/unittest.html#unittest.tearDownModule "unittest.tearDownModule") then you can call `doModuleCleanups()` yourself.
`doModuleCleanups()` pops methods off the stack of cleanup functions one at a time, so it can be called at any time.
Added in version 3.8.
## Signal Handling[¶](https://docs.python.org/3/library/unittest.html#signal-handling "Link to this heading")
Added in version 3.2.
The [`-c/--catch`](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-c) command-line option to unittest, along with the `catchbreak` parameter to [`unittest.main()`](https://docs.python.org/3/library/unittest.html#unittest.main "unittest.main"), provide more friendly handling of control-C during a test run. With catch break behavior enabled control-C will allow the currently running test to complete, and the test run will then end and report all the results so far. A second control-c will raise a [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt") in the usual way.
The control-c handling signal handler attempts to remain compatible with code or tests that install their own [`signal.SIGINT`](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT") handler. If the `unittest` handler is called but _isn’t_ the installed `signal.SIGINT` handler, i.e. it has been replaced by the system under test and delegated to, then it calls the default handler. This will normally be the expected behavior by code that replaces an installed handler and delegates to it. For individual tests that need `unittest` control-c handling disabled the [`removeHandler()`](https://docs.python.org/3/library/unittest.html#unittest.removeHandler "unittest.removeHandler") decorator can be used.
There are a few utility functions for framework authors to enable control-c handling functionality within test frameworks.

unittest.installHandler()[¶](https://docs.python.org/3/library/unittest.html#unittest.installHandler "Link to this definition")

Install the control-c handler. When a [`signal.SIGINT`](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT") is received (usually in response to the user pressing control-c) all registered results have [`stop()`](https://docs.python.org/3/library/unittest.html#unittest.TestResult.stop "unittest.TestResult.stop") called.

unittest.registerResult(_result_)[¶](https://docs.python.org/3/library/unittest.html#unittest.registerResult "Link to this definition")

Register a [`TestResult`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") object for control-c handling. Registering a result stores a weak reference to it, so it doesn’t prevent the result from being garbage collected.
Registering a [`TestResult`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult") object has no side-effects if control-c handling is not enabled, so test frameworks can unconditionally register all results they create independently of whether or not handling is enabled.
