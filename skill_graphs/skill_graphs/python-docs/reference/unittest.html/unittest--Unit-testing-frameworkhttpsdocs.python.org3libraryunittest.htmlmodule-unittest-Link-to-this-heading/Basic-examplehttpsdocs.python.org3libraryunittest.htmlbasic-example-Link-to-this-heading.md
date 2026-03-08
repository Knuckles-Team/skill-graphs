## Basic example[¶](https://docs.python.org/3/library/unittest.html#basic-example "Link to this heading")
The `unittest` module provides a rich set of tools for constructing and running tests. This section demonstrates that a small subset of the tools suffice to meet the needs of most users.
Here is a short script to test three string methods:
Copy```
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

```

A test case is created by subclassing [`unittest.TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase"). The three individual tests are defined with methods whose names start with the letters `test`. This naming convention informs the test runner about which methods represent tests.
The crux of each test is a call to [`assertEqual()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual "unittest.TestCase.assertEqual") to check for an expected result; [`assertTrue()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue "unittest.TestCase.assertTrue") or [`assertFalse()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertFalse "unittest.TestCase.assertFalse") to verify a condition; or [`assertRaises()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "unittest.TestCase.assertRaises") to verify that a specific exception gets raised. These methods are used instead of the [`assert`](https://docs.python.org/3/reference/simple_stmts.html#assert) statement so the test runner can accumulate all test results and produce a report.
The [`setUp()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp "unittest.TestCase.setUp") and [`tearDown()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.tearDown "unittest.TestCase.tearDown") methods allow you to define instructions that will be executed before and after each test method. They are covered in more detail in the section [Organizing test code](https://docs.python.org/3/library/unittest.html#organizing-tests).
The final block shows a simple way to run the tests. [`unittest.main()`](https://docs.python.org/3/library/unittest.html#unittest.main "unittest.main") provides a command-line interface to the test script. When run from the command line, the above script produces an output that looks like this:
Copy```
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

```

Passing the `-v` option to your test script will instruct [`unittest.main()`](https://docs.python.org/3/library/unittest.html#unittest.main "unittest.main") to enable a higher level of verbosity, and produce the following output:
Copy```
test_isupper (__main__.TestStringMethods.test_isupper) ... ok
test_split (__main__.TestStringMethods.test_split) ... ok
test_upper (__main__.TestStringMethods.test_upper) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK

```

The above examples show the most commonly used `unittest` features which are sufficient to meet many everyday testing needs. The remainder of the documentation explores the full feature set from first principles.
Changed in version 3.11: The behavior of returning a value from a test method (other than the default `None` value), is now deprecated.
## Command-Line Interface[¶](https://docs.python.org/3/library/unittest.html#command-line-interface "Link to this heading")
The unittest module can be used from the command line to run tests from modules, classes or even individual test methods:
Copy```
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method

```

You can pass in a list with any combination of module names, and fully qualified class or method names.
Test modules can be specified by file path as well:
Copy```
python -m unittest tests/test_something.py

```

This allows you to use the shell filename completion to specify the test module. The file specified must still be importable as a module. The path is converted to a module name by removing the ‘.py’ and converting path separators into ‘.’. If you want to execute a test file that isn’t importable as a module you should execute the file directly instead.
You can run tests with more detail (higher verbosity) by passing in the -v flag:
Copy```
python -m unittest -v test_module

```

When executed without arguments [Test Discovery](https://docs.python.org/3/library/unittest.html#unittest-test-discovery) is started:
Copy```
python -m unittest

```

For a list of all the command-line options:
Copy```
python -m unittest -h

```

Changed in version 3.2: In earlier versions it was only possible to run individual test methods and not modules or classes.
Added in version 3.14: Output is colorized by default and can be [controlled using environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color).
### Command-line options[¶](https://docs.python.org/3/library/unittest.html#command-line-options "Link to this heading")
**unittest** supports these command-line options:

-b, --buffer[¶](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-b "Link to this definition")

The standard output and standard error streams are buffered during the test run. Output during a passing test is discarded. Output is echoed normally on test fail or error and is added to the failure messages.

-c, --catch[¶](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-c "Link to this definition")

`Control`-`C` during the test run waits for the current test to end and then reports all the results so far. A second `Control`-`C` raises the normal [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt") exception.
See [Signal Handling](https://docs.python.org/3/library/unittest.html#signal-handling) for the functions that provide this functionality.

-f, --failfast[¶](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-f "Link to this definition")

Stop the test run on the first error or failure.

-k[¶](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-k "Link to this definition")

Only run test methods and classes that match the pattern or substring. This option may be used multiple times, in which case all test cases that match any of the given patterns are included.
Patterns that contain a wildcard character (`*`) are matched against the test name using [`fnmatch.fnmatchcase()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatchcase "fnmatch.fnmatchcase"); otherwise simple case-sensitive substring matching is used.
Patterns are matched against the fully qualified test method name as imported by the test loader.
For example, `-k foo` matches `foo_tests.SomeTest.test_something`, `bar_tests.SomeTest.test_foo`, but not `bar_tests.FooTest.test_something`.

--locals[¶](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-locals "Link to this definition")

Show local variables in tracebacks.

--durations N[¶](https://docs.python.org/3/library/unittest.html#cmdoption-unittest-durations "Link to this definition")

Show the N slowest test cases (N=0 for all).
Added in version 3.2: The command-line options `-b`, `-c` and `-f` were added.
Added in version 3.5: The command-line option `--locals`.
Added in version 3.7: The command-line option `-k`.
Added in version 3.12: The command-line option `--durations`.
The command line can also be used for test discovery, for running all of the tests in a project or just a subset.
