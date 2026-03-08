## Unittest API[¶](https://docs.python.org/3/library/doctest.html#unittest-api "Link to this heading")
As your collection of doctest’ed modules grows, you’ll want a way to run all their doctests systematically. `doctest` provides two functions that can be used to create [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") test suites from modules and text files containing doctests. To integrate with `unittest` test discovery, include a [load_tests](https://docs.python.org/3/library/unittest.html#load-tests-protocol) function in your test module:
Copy```
import unittest
import doctest
import my_module_with_doctests

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(my_module_with_doctests))
    return tests

```

There are two main functions for creating [`unittest.TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") instances from text files and modules with doctests:

doctest.DocFileSuite(_* paths_, _module_relative =True_, _package =None_, _setUp =None_, _tearDown =None_, _globs =None_, _optionflags =0_, _parser =DocTestParser()_, _encoding =None_)[¶](https://docs.python.org/3/library/doctest.html#doctest.DocFileSuite "Link to this definition")

Convert doctest tests from one or more text files to a [`unittest.TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite").
The returned [`unittest.TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") is to be run by the unittest framework and runs the interactive examples in each file. If an example in any file fails, then the synthesized unit test fails, and a [`failureException`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.failureException "unittest.TestCase.failureException") exception is raised showing the name of the file containing the test and a (sometimes approximate) line number. If all the examples in a file are skipped, then the synthesized unit test is also marked as skipped.
Pass one or more paths (as strings) to text files to be examined.
Options may be provided as keyword arguments:
Optional argument _module_relative_ specifies how the filenames in _paths_ should be interpreted:
  * If _module_relative_ is `True` (the default), then each filename in _paths_ specifies an OS-independent module-relative path. By default, this path is relative to the calling module’s directory; but if the _package_ argument is specified, then it is relative to that package. To ensure OS-independence, each filename should use `/` characters to separate path segments, and may not be an absolute path (i.e., it may not begin with `/`).
  * If _module_relative_ is `False`, then each filename in _paths_ specifies an OS-specific path. The path may be absolute or relative; relative paths are resolved with respect to the current working directory.


Optional argument _package_ is a Python package or the name of a Python package whose directory should be used as the base directory for module-relative filenames in _paths_. If no package is specified, then the calling module’s directory is used as the base directory for module-relative filenames. It is an error to specify _package_ if _module_relative_ is `False`.
Optional argument _setUp_ specifies a set-up function for the test suite. This is called before running the tests in each file. The _setUp_ function will be passed a [`DocTest`](https://docs.python.org/3/library/doctest.html#doctest.DocTest "doctest.DocTest") object. The _setUp_ function can access the test globals as the [`globs`](https://docs.python.org/3/library/doctest.html#doctest.DocTest.globs "doctest.DocTest.globs") attribute of the test passed.
Optional argument _tearDown_ specifies a tear-down function for the test suite. This is called after running the tests in each file. The _tearDown_ function will be passed a [`DocTest`](https://docs.python.org/3/library/doctest.html#doctest.DocTest "doctest.DocTest") object. The _tearDown_ function can access the test globals as the [`globs`](https://docs.python.org/3/library/doctest.html#doctest.DocTest.globs "doctest.DocTest.globs") attribute of the test passed.
Optional argument _globs_ is a dictionary containing the initial global variables for the tests. A new copy of this dictionary is created for each test. By default, _globs_ is a new empty dictionary.
Optional argument _optionflags_ specifies the default doctest options for the tests, created by or-ing together individual option flags. See section [Option Flags](https://docs.python.org/3/library/doctest.html#doctest-options). See function [`set_unittest_reportflags()`](https://docs.python.org/3/library/doctest.html#doctest.set_unittest_reportflags "doctest.set_unittest_reportflags") below for a better way to set reporting options.
Optional argument _parser_ specifies a [`DocTestParser`](https://docs.python.org/3/library/doctest.html#doctest.DocTestParser "doctest.DocTestParser") (or subclass) that should be used to extract tests from the files. It defaults to a normal parser (i.e., `DocTestParser()`).
Optional argument _encoding_ specifies an encoding that should be used to convert the file to unicode.
The global `__file__` is added to the globals provided to doctests loaded from a text file using `DocFileSuite()`.

doctest.DocTestSuite(_module =None_, _globs =None_, _extraglobs =None_, _test_finder =None_, _setUp =None_, _tearDown =None_, _optionflags =0_, _checker =None_)[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestSuite "Link to this definition")

Convert doctest tests for a module to a [`unittest.TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite").
The returned [`unittest.TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") is to be run by the unittest framework and runs each doctest in the module. Each docstring is run as a separate unit test. If any of the doctests fail, then the synthesized unit test fails, and a [`unittest.TestCase.failureException`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.failureException "unittest.TestCase.failureException") exception is raised showing the name of the file containing the test and a (sometimes approximate) line number. If all the examples in a docstring are skipped, then the
Optional argument _module_ provides the module to be tested. It can be a module object or a (possibly dotted) module name. If not specified, the module calling this function is used.
Optional argument _globs_ is a dictionary containing the initial global variables for the tests. A new copy of this dictionary is created for each test. By default, _globs_ is the module’s [`__dict__`](https://docs.python.org/3/reference/datamodel.html#module.__dict__ "module.__dict__").
Optional argument _extraglobs_ specifies an extra set of global variables, which is merged into _globs_. By default, no extra globals are used.
Optional argument _test_finder_ is the [`DocTestFinder`](https://docs.python.org/3/library/doctest.html#doctest.DocTestFinder "doctest.DocTestFinder") object (or a drop-in replacement) that is used to extract doctests from the module.
Optional arguments _setUp_ , _tearDown_ , and _optionflags_ are the same as for function [`DocFileSuite()`](https://docs.python.org/3/library/doctest.html#doctest.DocFileSuite "doctest.DocFileSuite") above, but they are called for each docstring.
This function uses the same search technique as [`testmod()`](https://docs.python.org/3/library/doctest.html#doctest.testmod "doctest.testmod").
Changed in version 3.5: `DocTestSuite()` returns an empty [`unittest.TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") if _module_ contains no docstrings instead of raising [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").
Under the covers, [`DocTestSuite()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestSuite "doctest.DocTestSuite") creates a [`unittest.TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") out of `doctest.DocTestCase` instances, and `DocTestCase` is a subclass of [`unittest.TestCase`](https://docs.python.org/3/library/unittest.html#unittest.TestCase "unittest.TestCase"). `DocTestCase` isn’t documented here (it’s an internal detail), but studying its code can answer questions about the exact details of [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") integration.
Similarly, [`DocFileSuite()`](https://docs.python.org/3/library/doctest.html#doctest.DocFileSuite "doctest.DocFileSuite") creates a [`unittest.TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") out of `doctest.DocFileCase` instances, and `DocFileCase` is a subclass of `DocTestCase`.
So both ways of creating a [`unittest.TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") run instances of `DocTestCase`. This is important for a subtle reason: when you run `doctest` functions yourself, you can control the `doctest` options in use directly, by passing option flags to `doctest` functions. However, if you’re writing a [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") framework, `unittest` ultimately controls when and how tests get run. The framework author typically wants to control `doctest` reporting options (perhaps, e.g., specified by command line options), but there’s no way to pass options through `unittest` to `doctest` test runners.
For this reason, `doctest` also supports a notion of `doctest` reporting flags specific to [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") support, via this function:

doctest.set_unittest_reportflags(_flags_)[¶](https://docs.python.org/3/library/doctest.html#doctest.set_unittest_reportflags "Link to this definition")

Set the `doctest` reporting flags to use.
Argument _flags_ takes the [bitwise OR](https://docs.python.org/3/reference/expressions.html#bitwise) of option flags. See section [Option Flags](https://docs.python.org/3/library/doctest.html#doctest-options). Only “reporting flags” can be used.
This is a module-global setting, and affects all future doctests run by module [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python."): the `runTest()` method of `DocTestCase` looks at the option flags specified for the test case when the `DocTestCase` instance was constructed. If no reporting flags were specified (which is the typical and expected case), `doctest`’s `unittest` reporting flags are [bitwise ORed](https://docs.python.org/3/reference/expressions.html#bitwise) into the option flags, and the option flags so augmented are passed to the [`DocTestRunner`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner "doctest.DocTestRunner") instance created to run the doctest. If any reporting flags were specified when the `DocTestCase` instance was constructed, `doctest`’s `unittest` reporting flags are ignored.
The value of the [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") reporting flags in effect before the function was called is returned by the function.
## Advanced API[¶](https://docs.python.org/3/library/doctest.html#advanced-api "Link to this heading")
The basic API is a simple wrapper that’s intended to make doctest easy to use. It is fairly flexible, and should meet most users’ needs; however, if you require more fine-grained control over testing, or wish to extend doctest’s capabilities, then you should use the advanced API.
The advanced API revolves around two container classes, which are used to store the interactive examples extracted from doctest cases:
  * [`Example`](https://docs.python.org/3/library/doctest.html#doctest.Example "doctest.Example"): A single Python [statement](https://docs.python.org/3/glossary.html#term-statement), paired with its expected output.
  * [`DocTest`](https://docs.python.org/3/library/doctest.html#doctest.DocTest "doctest.DocTest"): A collection of [`Example`](https://docs.python.org/3/library/doctest.html#doctest.Example "doctest.Example")s, typically extracted from a single docstring or text file.


Additional processing classes are defined to find, parse, and run, and check doctest examples:
  * [`DocTestFinder`](https://docs.python.org/3/library/doctest.html#doctest.DocTestFinder "doctest.DocTestFinder"): Finds all docstrings in a given module, and uses a [`DocTestParser`](https://docs.python.org/3/library/doctest.html#doctest.DocTestParser "doctest.DocTestParser") to create a [`DocTest`](https://docs.python.org/3/library/doctest.html#doctest.DocTest "doctest.DocTest") from every docstring that contains interactive examples.
  * [`DocTestParser`](https://docs.python.org/3/library/doctest.html#doctest.DocTestParser "doctest.DocTestParser"): Creates a [`DocTest`](https://docs.python.org/3/library/doctest.html#doctest.DocTest "doctest.DocTest") object from a string (such as an object’s docstring).
  * [`DocTestRunner`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner "doctest.DocTestRunner"): Executes the examples in a [`DocTest`](https://docs.python.org/3/library/doctest.html#doctest.DocTest "doctest.DocTest"), and uses an [`OutputChecker`](https://docs.python.org/3/library/doctest.html#doctest.OutputChecker "doctest.OutputChecker") to verify their output.
  * [`OutputChecker`](https://docs.python.org/3/library/doctest.html#doctest.OutputChecker "doctest.OutputChecker"): Compares the actual output from a doctest example with the expected output, and decides whether they match.


The relationships among these processing classes are summarized in the following diagram:
Copy```
                            list of:
+------+                   +---------+
|module| --DocTestFinder-> | DocTest | --DocTestRunner-> results
+------+    |        ^     +---------+     |       ^    (printed)
            |        |     | Example |     |       |
            v        |     |   ...   |     v       |
           DocTestParser   | Example |   OutputChecker
                           +---------+

```

### DocTest Objects[¶](https://docs.python.org/3/library/doctest.html#doctest-objects "Link to this heading")

_class_ doctest.DocTest(_examples_ , _globs_ , _name_ , _filename_ , _lineno_ , _docstring_)[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTest "Link to this definition")

A collection of doctest examples that should be run in a single namespace. The constructor arguments are used to initialize the attributes of the same names.
`DocTest` defines the following attributes. They are initialized by the constructor, and should not be modified directly.

examples[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTest.examples "Link to this definition")

A list of [`Example`](https://docs.python.org/3/library/doctest.html#doctest.Example "doctest.Example") objects encoding the individual interactive Python examples that should be run by this test.

globs[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTest.globs "Link to this definition")

The namespace (aka globals) that the examples should be run in. This is a dictionary mapping names to values. Any changes to the namespace made by the examples (such as binding new variables) will be reflected in [`globs`](https://docs.python.org/3/library/doctest.html#doctest.DocTest.globs "doctest.DocTest.globs") after the test is run.

name[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTest.name "Link to this definition")

A string name identifying the `DocTest`. Typically, this is the name of the object or file that the test was extracted from.

filename[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTest.filename "Link to this definition")

The name of the file that this `DocTest` was extracted from; or `None` if the filename is unknown, or if the `DocTest` was not extracted from a file.

lineno[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTest.lineno "Link to this definition")

The line number within [`filename`](https://docs.python.org/3/library/doctest.html#doctest.DocTest.filename "doctest.DocTest.filename") where this `DocTest` begins, or `None` if the line number is unavailable. This line number is zero-based with respect to the beginning of the file.

docstring[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTest.docstring "Link to this definition")

The string that the test was extracted from, or `None` if the string is unavailable, or if the test was not extracted from a string.
### Example Objects[¶](https://docs.python.org/3/library/doctest.html#example-objects "Link to this heading")

_class_ doctest.Example(_source_ , _want_ , _exc_msg =None_, _lineno =0_, _indent =0_, _options =None_)[¶](https://docs.python.org/3/library/doctest.html#doctest.Example "Link to this definition")

A single interactive example, consisting of a Python statement and its expected output. The constructor arguments are used to initialize the attributes of the same names.
`Example` defines the following attributes. They are initialized by the constructor, and should not be modified directly.

source[¶](https://docs.python.org/3/library/doctest.html#doctest.Example.source "Link to this definition")

A string containing the example’s source code. This source code consists of a single Python statement, and always ends with a newline; the constructor adds a newline when necessary.

want[¶](https://docs.python.org/3/library/doctest.html#doctest.Example.want "Link to this definition")

The expected output from running the example’s source code (either from stdout, or a traceback in case of exception). [`want`](https://docs.python.org/3/library/doctest.html#doctest.Example.want "doctest.Example.want") ends with a newline unless no output is expected, in which case it’s an empty string. The constructor adds a newline when necessary.

exc_msg[¶](https://docs.python.org/3/library/doctest.html#doctest.Example.exc_msg "Link to this definition")

The exception message generated by the example, if the example is expected to generate an exception; or `None` if it is not expected to generate an exception. This exception message is compared against the return value of [`traceback.format_exception_only()`](https://docs.python.org/3/library/traceback.html#traceback.format_exception_only "traceback.format_exception_only"). [`exc_msg`](https://docs.python.org/3/library/doctest.html#doctest.Example.exc_msg "doctest.Example.exc_msg") ends with a newline unless it’s `None`. The constructor adds a newline if needed.

lineno[¶](https://docs.python.org/3/library/doctest.html#doctest.Example.lineno "Link to this definition")

The line number within the string containing this example where the example begins. This line number is zero-based with respect to the beginning of the containing string.

indent[¶](https://docs.python.org/3/library/doctest.html#doctest.Example.indent "Link to this definition")

The example’s indentation in the containing string, i.e., the number of space characters that precede the example’s first prompt.

options[¶](https://docs.python.org/3/library/doctest.html#doctest.Example.options "Link to this definition")

A dictionary mapping from option flags to `True` or `False`, which is used to override default options for this example. Any option flags not contained in this dictionary are left at their default value (as specified by the [`DocTestRunner`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner "doctest.DocTestRunner")’s [optionflags](https://docs.python.org/3/library/doctest.html#doctest-options)). By default, no options are set.
### DocTestFinder objects[¶](https://docs.python.org/3/library/doctest.html#doctestfinder-objects "Link to this heading")

_class_ doctest.DocTestFinder(_verbose =False_, _parser =DocTestParser()_, _recurse =True_, _exclude_empty =True_)[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestFinder "Link to this definition")

A processing class used to extract the [`DocTest`](https://docs.python.org/3/library/doctest.html#doctest.DocTest "doctest.DocTest")s that are relevant to a given object, from its docstring and the docstrings of its contained objects. `DocTest`s can be extracted from modules, classes, functions, methods, staticmethods, classmethods, and properties.
The optional argument _verbose_ can be used to display the objects searched by the finder. It defaults to `False` (no output).
The optional argument _parser_ specifies the [`DocTestParser`](https://docs.python.org/3/library/doctest.html#doctest.DocTestParser "doctest.DocTestParser") object (or a drop-in replacement) that is used to extract doctests from docstrings.
If the optional argument _recurse_ is false, then [`DocTestFinder.find()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestFinder.find "doctest.DocTestFinder.find") will only examine the given object, and not any contained objects.
If the optional argument _exclude_empty_ is false, then [`DocTestFinder.find()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestFinder.find "doctest.DocTestFinder.find") will include tests for objects with empty docstrings.
`DocTestFinder` defines the following method:

find(_obj[, name][, module][, globs][, extraglobs]_)[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestFinder.find "Link to this definition")

Return a list of the [`DocTest`](https://docs.python.org/3/library/doctest.html#doctest.DocTest "doctest.DocTest")s that are defined by _obj_ ’s docstring, or by any of its contained objects’ docstrings.
The optional argument _name_ specifies the object’s name; this name will be used to construct names for the returned [`DocTest`](https://docs.python.org/3/library/doctest.html#doctest.DocTest "doctest.DocTest")s. If _name_ is not specified, then `obj.__name__` is used.
The optional parameter _module_ is the module that contains the given object. If the module is not specified or is `None`, then the test finder will attempt to automatically determine the correct module. The object’s module is used:
  * As a default namespace, if _globs_ is not specified.
  * To prevent the DocTestFinder from extracting DocTests from objects that are imported from other modules. (Contained objects with modules other than _module_ are ignored.)
  * To find the name of the file containing the object.
  * To help find the line number of the object within its file.


If _module_ is `False`, no attempt to find the module will be made. This is obscure, of use mostly in testing doctest itself: if _module_ is `False`, or is `None` but cannot be found automatically, then all objects are considered to belong to the (non-existent) module, so all contained objects will (recursively) be searched for doctests.
The globals for each [`DocTest`](https://docs.python.org/3/library/doctest.html#doctest.DocTest "doctest.DocTest") is formed by combining _globs_ and _extraglobs_ (bindings in _extraglobs_ override bindings in _globs_). A new shallow copy of the globals dictionary is created for each `DocTest`. If _globs_ is not specified, then it defaults to the module’s [`__dict__`](https://docs.python.org/3/reference/datamodel.html#module.__dict__ "module.__dict__"), if specified, or `{}` otherwise. If _extraglobs_ is not specified, then it defaults to `{}`.
### DocTestParser objects[¶](https://docs.python.org/3/library/doctest.html#doctestparser-objects "Link to this heading")

_class_ doctest.DocTestParser[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestParser "Link to this definition")

A processing class used to extract interactive examples from a string, and use them to create a [`DocTest`](https://docs.python.org/3/library/doctest.html#doctest.DocTest "doctest.DocTest") object.
`DocTestParser` defines the following methods:

get_doctest(_string_ , _globs_ , _name_ , _filename_ , _lineno_)[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestParser.get_doctest "Link to this definition")

Extract all doctest examples from the given string, and collect them into a [`DocTest`](https://docs.python.org/3/library/doctest.html#doctest.DocTest "doctest.DocTest") object.
_globs_ , _name_ , _filename_ , and _lineno_ are attributes for the new `DocTest` object. See the documentation for [`DocTest`](https://docs.python.org/3/library/doctest.html#doctest.DocTest "doctest.DocTest") for more information.

get_examples(_string_ , _name ='<string>'_)[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestParser.get_examples "Link to this definition")

Extract all doctest examples from the given string, and return them as a list of [`Example`](https://docs.python.org/3/library/doctest.html#doctest.Example "doctest.Example") objects. Line numbers are 0-based. The optional argument _name_ is a name identifying this string, and is only used for error messages.

parse(_string_ , _name ='<string>'_)[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestParser.parse "Link to this definition")

Divide the given string into examples and intervening text, and return them as a list of alternating [`Example`](https://docs.python.org/3/library/doctest.html#doctest.Example "doctest.Example")s and strings. Line numbers for the `Example`s are 0-based. The optional argument _name_ is a name identifying this string, and is only used for error messages.
### TestResults objects[¶](https://docs.python.org/3/library/doctest.html#testresults-objects "Link to this heading")

_class_ doctest.TestResults(_failed_ , _attempted_)[¶](https://docs.python.org/3/library/doctest.html#doctest.TestResults "Link to this definition")


failed[¶](https://docs.python.org/3/library/doctest.html#doctest.TestResults.failed "Link to this definition")

Number of failed tests.

attempted[¶](https://docs.python.org/3/library/doctest.html#doctest.TestResults.attempted "Link to this definition")

Number of attempted tests.

skipped[¶](https://docs.python.org/3/library/doctest.html#doctest.TestResults.skipped "Link to this definition")

Number of skipped tests.
Added in version 3.13.
### DocTestRunner objects[¶](https://docs.python.org/3/library/doctest.html#doctestrunner-objects "Link to this heading")

_class_ doctest.DocTestRunner(_checker =None_, _verbose =None_, _optionflags =0_)[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner "Link to this definition")

A processing class used to execute and verify the interactive examples in a [`DocTest`](https://docs.python.org/3/library/doctest.html#doctest.DocTest "doctest.DocTest").
The comparison between expected outputs and actual outputs is done by an [`OutputChecker`](https://docs.python.org/3/library/doctest.html#doctest.OutputChecker "doctest.OutputChecker"). This comparison may be customized with a number of option flags; see section [Option Flags](https://docs.python.org/3/library/doctest.html#doctest-options) for more information. If the option flags are insufficient, then the comparison may also be customized by passing a subclass of `OutputChecker` to the constructor.
The test runner’s display output can be controlled in two ways. First, an output function can be passed to [`run()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.run "doctest.DocTestRunner.run"); this function will be called with strings that should be displayed. It defaults to `sys.stdout.write`. If capturing the output is not sufficient, then the display output can be also customized by subclassing DocTestRunner, and overriding the methods [`report_start()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.report_start "doctest.DocTestRunner.report_start"), [`report_success()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.report_success "doctest.DocTestRunner.report_success"), [`report_unexpected_exception()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.report_unexpected_exception "doctest.DocTestRunner.report_unexpected_exception"), and [`report_failure()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.report_failure "doctest.DocTestRunner.report_failure").
The optional keyword argument _checker_ specifies the [`OutputChecker`](https://docs.python.org/3/library/doctest.html#doctest.OutputChecker "doctest.OutputChecker") object (or drop-in replacement) that should be used to compare the expected outputs to the actual outputs of doctest examples.
The optional keyword argument _verbose_ controls the `DocTestRunner`’s verbosity. If _verbose_ is `True`, then information is printed about each example, as it is run. If _verbose_ is `False`, then only failures are printed. If _verbose_ is unspecified, or `None`, then verbose output is used iff the command-line switch `-v` is used.
The optional keyword argument _optionflags_ can be used to control how the test runner compares expected output to actual output, and how it displays failures. For more information, see section [Option Flags](https://docs.python.org/3/library/doctest.html#doctest-options).
The test runner accumulates statistics. The aggregated number of attempted, failed and skipped examples is also available via the [`tries`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.tries "doctest.DocTestRunner.tries"), [`failures`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.failures "doctest.DocTestRunner.failures") and [`skips`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.skips "doctest.DocTestRunner.skips") attributes. The [`run()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.run "doctest.DocTestRunner.run") and [`summarize()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.summarize "doctest.DocTestRunner.summarize") methods return a [`TestResults`](https://docs.python.org/3/library/doctest.html#doctest.TestResults "doctest.TestResults") instance.
`DocTestRunner` defines the following methods:

report_start(_out_ , _test_ , _example_)[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.report_start "Link to this definition")

Report that the test runner is about to process the given example. This method is provided to allow subclasses of `DocTestRunner` to customize their output; it should not be called directly.
_example_ is the example about to be processed. _test_ is the test containing _example_. _out_ is the output function that was passed to [`DocTestRunner.run()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.run "doctest.DocTestRunner.run").

report_success(_out_ , _test_ , _example_ , _got_)[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.report_success "Link to this definition")

Report that the given example ran successfully. This method is provided to allow subclasses of `DocTestRunner` to customize their output; it should not be called directly.
_example_ is the example about to be processed. _got_ is the actual output from the example. _test_ is the test containing _example_. _out_ is the output function that was passed to [`DocTestRunner.run()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.run "doctest.DocTestRunner.run").

report_failure(_out_ , _test_ , _example_ , _got_)[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.report_failure "Link to this definition")

Report that the given example failed. This method is provided to allow subclasses of `DocTestRunner` to customize their output; it should not be called directly.
_example_ is the example about to be processed. _got_ is the actual output from the example. _test_ is the test containing _example_. _out_ is the output function that was passed to [`DocTestRunner.run()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.run "doctest.DocTestRunner.run").

report_unexpected_exception(_out_ , _test_ , _example_ , _exc_info_)[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.report_unexpected_exception "Link to this definition")

Report that the given example raised an unexpected exception. This method is provided to allow subclasses of `DocTestRunner` to customize their output; it should not be called directly.
_example_ is the example about to be processed. _exc_info_ is a tuple containing information about the unexpected exception (as returned by [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info")). _test_ is the test containing _example_. _out_ is the output function that was passed to [`DocTestRunner.run()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.run "doctest.DocTestRunner.run").

run(_test_ , _compileflags =None_, _out =None_, _clear_globs =True_)[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.run "Link to this definition")

Run the examples in _test_ (a [`DocTest`](https://docs.python.org/3/library/doctest.html#doctest.DocTest "doctest.DocTest") object), and display the results using the writer function _out_. Return a [`TestResults`](https://docs.python.org/3/library/doctest.html#doctest.TestResults "doctest.TestResults") instance.
The examples are run in the namespace `test.globs`. If _clear_globs_ is true (the default), then this namespace will be cleared after the test runs, to help with garbage collection. If you would like to examine the namespace after the test completes, then use _clear_globs=False_.
_compileflags_ gives the set of flags that should be used by the Python compiler when running the examples. If not specified, then it will default to the set of future-import flags that apply to _globs_.
The output of each example is checked using the `DocTestRunner`’s output checker, and the results are formatted by the `DocTestRunner.report_*()` methods.

summarize(_verbose =None_)[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.summarize "Link to this definition")

Print a summary of all the test cases that have been run by this DocTestRunner, and return a [`TestResults`](https://docs.python.org/3/library/doctest.html#doctest.TestResults "doctest.TestResults") instance.
The optional _verbose_ argument controls how detailed the summary is. If the verbosity is not specified, then the `DocTestRunner`’s verbosity is used.
[`DocTestParser`](https://docs.python.org/3/library/doctest.html#doctest.DocTestParser "doctest.DocTestParser") has the following attributes:

tries[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.tries "Link to this definition")

Number of attempted examples.

failures[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.failures "Link to this definition")

Number of failed examples.

skips[¶](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.skips "Link to this definition")

Number of skipped examples.
Added in version 3.13.
### OutputChecker objects[¶](https://docs.python.org/3/library/doctest.html#outputchecker-objects "Link to this heading")

_class_ doctest.OutputChecker[¶](https://docs.python.org/3/library/doctest.html#doctest.OutputChecker "Link to this definition")

A class used to check the whether the actual output from a doctest example matches the expected output. `OutputChecker` defines two methods: [`check_output()`](https://docs.python.org/3/library/doctest.html#doctest.OutputChecker.check_output "doctest.OutputChecker.check_output"), which compares a given pair of outputs, and returns `True` if they match; and [`output_difference()`](https://docs.python.org/3/library/doctest.html#doctest.OutputChecker.output_difference "doctest.OutputChecker.output_difference"), which returns a string describing the differences between two outputs.
`OutputChecker` defines the following methods:

check_output(_want_ , _got_ , _optionflags_)[¶](https://docs.python.org/3/library/doctest.html#doctest.OutputChecker.check_output "Link to this definition")

Return `True` iff the actual output from an example (_got_) matches the expected output (_want_). These strings are always considered to match if they are identical; but depending on what option flags the test runner is using, several non-exact match types are also possible. See section [Option Flags](https://docs.python.org/3/library/doctest.html#doctest-options) for more information about option flags.

output_difference(_example_ , _got_ , _optionflags_)[¶](https://docs.python.org/3/library/doctest.html#doctest.OutputChecker.output_difference "Link to this definition")

Return a string describing the differences between the expected output for a given example (_example_) and the actual output (_got_). _optionflags_ is the set of option flags used to compare _want_ and _got_.
